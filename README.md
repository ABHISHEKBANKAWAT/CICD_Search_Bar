# ProjectPro-Search-Bar with SBERT and FAISS

### Project Files Description:

* data
  
  * project_mappings.csv - Index mapping for every project

* output

  * search.index - FAISS object for inference

* src

  * dataset.py - python script to fetch datasets from MongoDB
  * embeddings.py - python script to create embeddings using SBERT
  * processing.py - python script to preprocess data 
  * query_search.py - python inference script to generate search results
  * utils.py - python script for generating overall dataset

* app.py - streamlit app python script

* engine.py - creates embeddings for the overall projects text data and generates and saves index (FAISS object) for inference.


### Execution Steps:

* Install requirements with the command "pip3 install -r requirements.txt"

* Run engine.py to create embeddings and save the FAISS object with the command "python3 engine.py"

* Run app.py with the command "streamlit run app.py"

### CI/CD Pipeline
* This pipeline periodically checks for any change in training data or code and proceed with functional and ML tests. If all tests check out, the changes get applied in production
* Important branches (not to be deleted)
  * `prod`: this is the release branch
  * `stage`: this is the branch where all other pull requests need to be merged manually after peer-review
* Servers
  * Jenkins Server: http://35.93.71.86:8080/
  * SearchBar Server: http://54.186.23.242:8501/
* Jenkins configurations:
  * login username: `admin`
  * login password: `<contact this repo admin>`
  * Jenkins codebase: https://github.com/kedardezyre/camille_projects/tree/jenkinsserver
* Additional notes (Still Work In Progress): https://github.com/projectpro-product/sbert-search-bar/blob/prod/tutorial.md

