# import libraries

import pandas as pd
from pymongo import MongoClient
  
conn = MongoClient("mongodb+srv://admin:Projectpro123@main-cluster.ypfc7yk.mongodb.net/?retryWrites=true&w=majority")

#database name : MainDB
db = conn.MainDB

# 1. Project Description Data
def get_project_description():
    '''
    The function retrives project description data from MongoDB
    -------------
    Parameters:
    Returns:
    project_description: DataFrame
    '''
    try:
        # Switched to collection names: project_description
        collection = db['project_description'] 
        # To find() all the entries inside collection name 'project_description' and store it in dataframe
        project_description = pd.DataFrame(list(collection.find()))
        project_description=project_description.drop(columns='_id')
        
    except Exception as e:
        print(e)

    else:
        return project_description



# get video titles
def get_video_titles():
    '''
    The function retrievs video titles data from Mongo DB
    --------
    Parameters:
    Returns:
    project_topics: DataFrame

    '''
    try:
        # Switched to collection names: project_topics
        collection = db['project_topics'] 
        # To find() all the entries inside collection name 'project_topics' and store it in dataframe
        project_topics = pd.DataFrame(list(collection.find()))
        project_topics=project_topics.drop(columns='_id')
        
    except Exception as e:
        print(e)

    else:
        return project_topics



# Abbreviations data

def get_abbreviations():
    '''
    The function retrieves abbreviations data
    ---------
    Parameters:
    Returns:
    Abbreviations: DataFrame
    '''
    try:
        # Switched to collection names: Abbreviations
        collection = db['Abbreviations'] 
        # To find() all the entries inside collection name 'Abbreviations' and store it in dataframe
        Abbreviations = pd.DataFrame(list(collection.find()))
        Abbreviations=Abbreviations.drop(columns='_id')
    
    except Exception as e:
        print(e)
    
    else:
        return Abbreviations