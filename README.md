# Fuel_Consumption_Model
The goal of this project is to build a ML model that predicts how much Carbondioxide a car emits.

You can find dataset here: https://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64/resource/80894b62-7b45-4150-946d-ab756814c4be

## Project Description:

FUEL CONSUMPTION RATING
Fuel consumption has implications on climate change and the general environment hence the 
need for accurate prediction and classification of motor vehicles.
The task is to predict the CO2 emission of the vehicles.

## The Dataset
MY2010-2014 Fuel Consumption Ratings 5-cycle.csv.1

## Solution
Development Phase: I created a supervised ml model to predict the amount of CO2 emissions of vehicles. I used XGBoost to train this model.

Deployment Phase: I will use BentoML for containerization and deploy the model locally to a swagger UI. See images attached : 'Bento', 'docker_img_'

## How To Run:
0. Clone this repo.
1. Download the dataset. See 'The Dataset' section above.
2. Run command:
   ```pipenv install```
   if it does not execute try ```pip install pipenv``` , then ```pipenv install``` 
   Then check into virtual environment with  ```pipenv shell```
3. Train the model:
   ```python train.py```
4. Check for any saved models in bentoml:
   ``` bentoml models list```
   Run this:
   ```bentoml models get fuel_consumption_model:latest```
5. Run:
   ```vim bentofile.yaml```
   Run:
   ```vim service.py```
 6. Deploying service locally.
    Build service:
    ```bentoml serve --production --reload```
    Visit Swagger UI:
    ```http://localhost:3000/```
    
    
   
