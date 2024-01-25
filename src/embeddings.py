
from src import processing
import numpy as np
from tqdm import tqdm
import faiss
from sentence_transformers import SentenceTransformer



def create_embeddings(data):
    '''
    This function creates sentence embeddings using pretrained
    all-MiniLM-L6-v2 model for SBert    

    Input:
    data: input text to create embeddings


    Output:
    listToStr: text after removing stopwords from NLTK and Spacy
    '''

    try:
        # all-MiniLM-L6-v2 is the best pre trained model
        model= SentenceTransformer('all-MiniLM-L6-v2') # using pre trained model for Sbert
        sentence_embeddings=model.encode(data)
    except Exception as e:
        print(e)
        print("Embeddings are not created. Check create_embeddings function.")
    else:
            return sentence_embeddings   
    
