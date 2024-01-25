# importing libraries
import pandas as pd
import numpy as np
import re

import sys
import os
import string
#Library to tokenise and remove stopwords 
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
#Library to remove stopwords 
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")
from src import utils





# tokenizer
spacy_tokenizer=spacy.load('en_core_web_sm')


# defining functions for different pre processing methods
def separate_words_if_capital(data):
    '''
    This function separates joined words from the text
    eg. DataScience--> Data Science

    Input:
    data: text to  separate the words

    Output:
    separated data without joined capital words

    '''
    try:
        separated_data=re.sub(r"(?<=[a-z])(?=[A-Z])"," ", data)
        # to introduce space between all capitalised letters
    except Exception as e:
            print(e)
            print("Words are still not separated with space")
    else:
        return separated_data

def lower_case(data):
    '''
    This function converts text to lower case.

    Input:
    data: text to convert to lower case

    Output:
    lower_data: lower case text
    
    '''
    try:
        lower_data=data.lower()   # converting the text to lower case
    except Exception as e:
            print(e)
            print("Data not converted to lower case")
    else:
        return lower_data    
        
#string.punctuation contains : #!”#$%&\()*+,-/:;<=>?@[\\]^_`{|}~
def remove_punctuations(data):
    '''
    This function removes all the puncutiations present in string.punctuation
    Removes #!”#$%&\()*+,-/:;<=>?@[\\]^_`{|}~ from the text

    Input:
    data: text to remove punctuation from

    Output:
    transformed_data: text after removing punctuations
    '''
    try:
        trans = str.maketrans(string.punctuation, ' '*len(string.punctuation))
        transformed_data=data.translate(trans)  # removing all the defined punctuations from the text
    except Exception as e:
            print(e)
            print("Punctuations not removed")
    else:
        return transformed_data

        
def white_space(data):
    '''
    This function remove extra spaces from the text.

    Input:
    data: text to remove white spaces from

    Output:
    space_removed_data: text after removing spaces
    
    '''
    try:
        space_removed_data=' '.join(data.split())   # removing white spaces from text
    except Exception as e:
            print(e)
            print("White spaces were not removed")
    else: 
        return space_removed_data
        
        
def remove_non_textual_data(data):
    '''
    This function removes non textual data such as removing links, bullet points, tick marks from the input.

    Input: 
    data: text to remove non textual data from

    Output:
    text_data: text data after removing non textual data
    
    '''
    try:
        regex_compiled=re.compile(r'(?:|:|;|&|\(|\)|\?|-|!|\n|/|,|_|"|"|\n+|\t|\t+|•|●|:black_circle:|✓|https\S|e.g.|nbsp|\'|’|➔|\#|@|\+|\*|\?|\[|\^|\]|\$|\(|\)|\{|\}|\=|\!|\-|~|`|%|\|\<|\>)')
        text_data=re.sub(regex_compiled,'',data)   # removing links, bullet points, tick marks, non text data
    except Exception as e:
            print(e)
            print("Non-textual data is still present")
    else:
        return text_data
        
def remove_numbers(data):
    '''
    This function removes all the numbers from the input text.

    Input:
    data: text to remove numbers

    Output:
    removed_numbers_text: text after removing numbers
    '''

# Iterate over the characters in string and join all characters except digits, to create a new string.
    try:
            removed_numbers_text= ''.join((item for item in data if not item.isdigit()))
    except Exception as e:
            print(e)
            print("Numbers from the data were not removed")
    else:
            return removed_numbers_text       


# function to add abreviation context
def add_abbreviation_context(text, abb_dic):
  '''The functions adds context in the text for various abbreviations from previously defined sub-processed
     abb_dic (dictionary) of the form {abb1: context1, abb2: context2}
     
     Input: text (string)
     Output: text (context added string)'''
  try:
    for key in abb_dic.keys():
      if key in text.split(" "):
        text = text +" "+ abb_dic[key]
  except Exception as e:
    print(e)
    print("There is a problem while adding context to various abbreviations")
  else:
    return text


# function for tokenization of pre processed text
def tokenizer(text):
    '''
    This function tokenizes the text using pretrained spacy model en_core_web_sm

    Input:
    text: input text to tokenize

    Output:
    tokenised_text: text after tokenization
    '''
    try:
            tokenised_text=[]
            for token in spacy_tokenizer(text):
                tokenised_text.append(token)
    except Exception as e:
            print(e)
            print("tokenization is not completed")
    else:
            return tokenised_text

# function to lemmatize and find root words
def extract_lemma(text):
    '''
    This function lemmatize the text

    Input:
    text: input text for lemmatization


    Output:
    listToStr: text after lemmatization
    '''

    try:
            text_lemma=[]
            text_cleaned=spacy_tokenizer(text)
            for token in text_cleaned:  
                text_lemma.append(token.lemma_)
            listToStr = ' '.join([str(elem) for elem in text_lemma])
    except Exception as e:
            print(e)
            print("lemmatization not completed")
    else:
            return listToStr




# function to remove stop words using list comprhension and returns a string
def remove_stopwords(text):
    '''
    This function removes stop words from input text.
    Used stopwords are from nltk and spacy combined.

    Input:
    text: input text to remove stopwords


    Output:
    listToStr: text after removing stopwords from NLTK and Spacy
    '''

    try:
            #nltk and spacy combined stopwords
            stpwrds=set(stopwords.words('english')).union(STOP_WORDS) 
            #create list of words
            text_cleaned=[token for token in text if not (str(token).lower() in stpwrds)]
            #joins the list back to make string
            listToStr = ' '.join([str(elem) for elem in text_cleaned])
    except Exception as e:
            print(e)
            print("Stopwords not removed")
    else:
            return listToStr



# main function for pre processing the data : returns final pre processed text in processed_data
def sub_preprocessing(data):
    '''
    This function does the preprocessing
    (Separate words, lower case, remove extra space, remove non textual data) on the text data.

    Input:
    data: input text data


    Output:
    processed_data: text after preprocessing
    '''

    try:
            separated_data=separate_words_if_capital(data)
            data_lower=lower_case(separated_data)
            punctuation_removed_data = remove_punctuations(data_lower)
            space_removed_data = white_space(punctuation_removed_data)
            text_data = remove_non_textual_data(space_removed_data)
            processed_data=remove_numbers(text_data)
    except Exception as e:
            print(e)
            print('There is some problem in sub preprocessing')
    else:    
            return processed_data

# calling all functions to pre process , cleaning the text and convert to dataframe
def final_preprocessing(df,content_col, abb_dic):
    '''
    This function does all the preproceesing steps.
    tokenization, removing stopwrods, lemmatization etc

    Input:
    df: input dataframe
    content_col: column name which contains text data


    Output:
    df: dataframe after the preprocessing
    '''

    try:
            df['Processed_text']=df.apply(lambda x: sub_preprocessing(x[content_col]), axis=1)
            df['Processed_text']=df.apply(lambda x: add_abbreviation_context(x['Processed_text'], abb_dic), axis=1) 
            df['Processed_text']=df.apply(lambda x: tokenizer(x['Processed_text']), axis=1)
            df['Processed_text']=df.apply(lambda x: remove_stopwords(x['Processed_text']), axis=1)
            df['Processed_text']=df.apply(lambda x: extract_lemma(x['Processed_text']), axis=1)
            
    except Exception as e:
            print(e)
            print('There is some problem while preprocessing the data.')
    else:
        return df


# Function to preprocess the input query
def query_processing(query, abb_dic):
  try:
    query = sub_preprocessing(query)
    query = add_abbreviation_context(query, abb_dic)
    query = tokenizer(query)
    query = remove_stopwords(query)
    query = extract_lemma(query)

  except Exception as e:
          print(e)
          print('There is some problem while preprocessing the query.')
  else:
      return query  



      