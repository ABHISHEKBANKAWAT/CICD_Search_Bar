# import libraries
import pandas as pd
from src import processing
import spacy
from tqdm import tqdm


# tokenizer
spacy_tokenizer=spacy.load('en_core_web_sm')


# Function to read project topics data and return a mapping

def get_project_topics_map(project_topics_df):
    '''
    The function reads projects video titles or topic names data, processes it to return 
    a project and video titles dictionary

    Input:
    project_topics_df: Project topics dataframe
    Output:
    project_topics_dic: Projects and topics dictionary
    '''
    try:
        
        project_topics_df.dropna(inplace=True)

        project_topics_df['topics'] = project_topics_df.groupby('title')['topic_name'].transform(lambda x : ' '.join(map(str,x)))
        project_topics_df.drop('topic_name', axis=1, inplace=True)
        project_topics_df = project_topics_df.drop_duplicates()

        # project title mapping
        project_topics_dic =  dict(zip(project_topics_df.title,project_topics_df.topics))

    except Exception as e:
        print(e)

    else:
        return project_topics_dic



# Function to get abbreviations data mapping
def get_abbreviation_mapping(abbreviations_df):
    '''
    The function reads abbreviation context data and returns a mapping 
    Input:
    abbreviations_df: abbreviation-context dataframe

    Output:
    abb_dic: dictionary
    '''
    try:
        # sub preprocessing of data
        abbreviations_df['clean_acronyms']= abbreviations_df["acronym"].apply(lambda x: processing.sub_preprocessing(x))
        # sub preprocessing of data
        abbreviations_df['clean_context']= abbreviations_df["context"].apply(lambda x: processing.sub_preprocessing(x))
        abb_dic=dict(zip(abbreviations_df.clean_acronyms, abbreviations_df.clean_context))
    
    except Exception as e:
        print(e)

    else:
        return abb_dic





# Generate overall data
def generate_data(project_description_df, project_topics_df):
    '''
    The function collects data regarding the projects from different sources
    description and video titles
    combines them up and returns raw data for processing.

    Input:
    project_description_df: Description DataFrame
    project_topics_df: video titles dataframe
    
    Output:
    raw_data: combined raw data ready to be processed '''

    try:
        # project topics mapping (video titles)
        project_topics_dic = get_project_topics_map(project_topics_df)

        # Add video titles (topics) column
        project_description_df['topics'] = project_description_df['title'].map(project_topics_dic)

        # fill nulls
        project_description_df = project_description_df.fillna(" ")

        # merging the different text columns containing the project information
        project_description_df['Description']=project_description_df['title']+' '+project_description_df['learn']+' '+project_description_df['description'] + ' ' + project_description_df['topics'] + " "+ project_description_df['domain']
        project_description_df=project_description_df.drop(columns=['learn','description']) #title,Description,id,domain

    except Exception as e:
        print(e)

    else:
        return project_description_df
        


