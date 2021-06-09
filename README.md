# Dependency Parser [Hindi]
done as a course project of Intro to NLP | Spring 2021
In this project, a dependency parser (Hindi) for which the training dataset was given. A dependency parser identifies the syntactic dependency between words in a
sentence. There are few well-developed tools for Indian languages.

## data
http://ltrc.iiit.ac.in/treebank_H2014/ 

## Preprocessing 
* coding + manual editing for processing before getting to the final data
* on initial data, use extract_data.py, extract_head.py, extract_dependency.py in order
* then get the indexes from arceager.py
* put the indexes in chean.py and run extract_k_u_dependency.py
## for running the model 
* Datasets to be used are in src folder, directly loaded into notebooks.
* All experiments + model fitting + predictions + classification reports are being done in the jupyter notebooks inside. To re run, simply restart and run all. To change the parameters such as list_file (contains tokens) and input files - train and test, refer to cell 3.
