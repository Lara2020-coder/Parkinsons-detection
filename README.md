
# Parkinson detection (from data to the model deployement) using Azure Machine Learning  

## Summary of the project
**This project is part of the Udacity Azure ML Nanodegree.**

In this project we had the opportunity to use the knowledge we obtained from the Nanodegree to solve a problem of our choice. 
Where We start by creating two models: one using Automated ML and one customized model whose hyperparameters are tuned using HyperDrive. we then compare the performance of both models and finally deploy the best performing one.

![Diagrame](Diagram.png "Diagrame")

## Dataset

### Overview
Parkinson's disease is a brain disorder that leads to shaking, stiffness, and difficulty with walking, balance, coordination, and talking it may also result in mental and behavioral changes, sleep problems,... (It is important to make an exact diagnosis as soon as possible). Several disorders can cause symptoms similar to those of Parkinson's disease and there are also different ways to do the diagnosis (medical test, response to drug treatment,..) for more information https://www.nia.nih.gov/health/parkinsons-disease#:~:text=Parkinson's%20disease%20is%20a%20brain,have%20difficulty%20walking%20and%20talking
This lead to the main goal of this project which is  an attempt to create a classifier to predict if a person has Parkinson disease based on biomedical voice measurements from different people
**NB: the data used here is old but the goal is to demonstrate that the Machine Learning discipline applied in the field of medicine will save more lives**

### Datasource
The dataset used in this project was created by Max Little of the University of Oxford, in collaboration with the National Centre for Voice and Speech, Denver, Colorado, who recorded the speech signals. It is composed of a range of biomedical voice measurements from 31 people, 23 with Parkinson's disease (PD). Each column in the table is a particular voice measure, and each row corresponds one of 195 voice recording from these individuals ("name" column). for more information https://archive.ics.uci.edu/ml/datasets/parkinsons
**NB : The following paper need to be quoted 'Exploiting Nonlinear Recurrence and Fractal Scaling Properties for Voice Disorder Detection', Little MA, McSharry PE, Roberts SJ, Costello DAE, Moroz IM. BioMedical Engineering OnLine 2007, 6:23 (26 June 2007)**

### Task
The main Goal of this task is to discriminate healthy people from those with parkinson disease(PD), according to "status" column which is set to 0 for healthy and 1 for PD to do this i used the different voice measure included in the dataset (columns)

### Access
The data was loaded first in this repository so that it can be used directly into the different notebook via the link below  https://raw.githubusercontent.com/hananeouhammouch/Parkinsons-detection/master/parkinsons.data

## Automated ML
To configure the Automated ML run we used the setting bellow :
![Automl_config](Automl_config.PNG "Automl_confige")

|Setting |Reasons ?|
|-|-|
|**experiment_timeout_minutes**|Maximum amount of time in minutes that all iterations combined can take before the experiment terminates (15 minute because the dataset include only 195 lines)|
|**max_concurrent_iterations**|To help manage child runs in parallele mode, we create a dedicated cluster per experiment, and match the number of this setting (4) to the number of nodes in the cluster(5-1))|
|**n_cross_validations**|Number of cross validation (5) splits to ensure that they will be no overfiting |
|**primary_metric**|This is the metric that we want to optimize (accuracy) |
|**task**|classification |
|**compute_target**|To define the compute cluster we will be using |
|**training_data**|To specify the training dataset stored in the datastore  |
|**label_column_name**|To specify the dependent variable that we are trying to classify |

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?
Before running, AutoML Start first by checking over the input data to ensure high quality is being used to train the model where he uses class balancing detection, Missing Feature values imputation, and high cardinality feature detection.

After the execution, the AutoML Result not only includes the best model resulting from the running of multiple classification algorithms but he also delivers interesting information to understand more why this choice of model was made in this case of problem by learning what features are directly impacting the model and why.

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
