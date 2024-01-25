from src import processing, utils, dataset, embeddings
import pandas as pd
import numpy as np
import json

def fetch_project_info(df,dataframe_idx):
  '''
  The function takes in dataframe and returned ids from 
  nmslib index and matches to actual dataframe to return 
  project ids and titles
  Note: project mappings df  (title) should be similar to the 
  original raw projects df fetched to train the models.
  
  Input:
  df: project mappings df
  dataframe_idx: index to be searched'''

  try:
    info = df.iloc[dataframe_idx]
    meta_dict = dict()
    meta_dict['title'] = info['title']

  except Exception as e:
    print(e)
  else:
    return meta_dict

# define abbreviations to complete preprocessing

abbreviations_df = dataset.get_abbreviations()
abb_dic = utils.get_abbreviation_mapping(abbreviations_df)

def search(input, index, top_k, df):
  '''
  The function searches top_k nearest neighbours for the search query 
  from faiss index.

  Input:
  input: search query input (str)
  index: faiss index generated
  top_k: number of relevant search results to be returned
  df: project mappings dataframe to give out project id and titles

  Output:
  results: Dictionary of jsom dumps of project ids and titles
  '''
  
  query = processing.query_processing(input, abb_dic)
  query_vector = embeddings.create_embeddings([query])
  top_k = index.search(query_vector, top_k)
  top_k_ids = top_k[1].tolist()[0]
  top_k_ids = list(np.unique(top_k_ids))
  
  # fetch project ids from the project data scraped
  results =  [fetch_project_info(df, idx) for idx in top_k_ids]

  results = pd.DataFrame(results)
  
  results = results[['title']]
  
  return results