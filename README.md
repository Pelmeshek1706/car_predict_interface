# car_predict_interface
# Prediction car price  
#### made by [@pelmeshek1706](https://telegram.me/pelmeshek1706)

The project was created for application in the sphere of car buying/selling services in order to find out the average market value for a particular car brand. 

The user can enter the name of his car (<code>Make, Model</code>), the year of manufacture (<code>Year</code>), the number of miles driven on the car (<code>Mileage</code>), whether the car is certified or used (<code>Used/New</code>), all the variables are pulled from the car database (</code>machine_db.csv</code>). 

## Requirements:
- joblib 1.3.2 +
- xgboost 1.6.0+
- pandas 2.0.3 +

## All neaded files to use interface:
- *machine_db.csv* - db with machines and information about them. necessary to get parameters.
- *column_names.txt* - file with the names of all columns. needed to get the prediction
- *xgbregressor.pkl* - trained model

## Example usage:

 - Enter name car like 'Porsche 911 Turbo S' : *Porsche 911 Turbo S*
 - Enter year yor model: *2020*
 - Enter mileage: *1250*
 - Are your car is new? *no*

 info about your car:

- name - *porsche*, model - *911turbos*, year - *2020*
- Rating - *4.85*, reviews - *29.0*
- Min - *19*, max - *24* 
- mileage - *1250*, status - *used* 
- drivetrain - *awd*, fuel - *gasoline* 


- Price for your car: *161093.32*+-4030.68 


Data that I used - [Car dataset](https://www.kaggle.com/datasets/chancev/carsforsale)
