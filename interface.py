import pandas as pd
import joblib
import xgboost as xgb

with open('column_names.txt', 'r') as file:
    column_names = file.read().splitlines()

machine_bd = pd.read_csv('machine_db.csv')


def predict_price(data):

    loaded_model = joblib.load('xgbregressor.pkl').get_booster()

    df = pd.DataFrame(columns = column_names)
    parts = input("Enter name car like 'Porsche 911 Turbo S' : ").lower().split(' ', 1)

    make = parts[0]
    model = parts[1].replace(' ', '')

    year = int(input('Enter year yor model: '))
    consumerrating = round(data[(data['Make'] == make) & data['Model'].str.contains(model, case=False)]['ConsumerRating'].mean(), 2)
    consumerreviews = round(data[(data['Make'] == make) & data['Model'].str.contains(model, case=False)]['ConsumerReviews'].mean(), 0)
    minmpg = data[(data['Make'] == make) & data['Model'].str.contains(model, case=False)]['MinMPG'].mode()[0]
    maxmpg = data[(data['Make'] == make) & data['Model'].str.contains(model, case=False)]['MaxMPG'].mode()[0]

    mileage = int(input("enter mileage: "))
    used_new = input("Are your car is new? ")
    used_new = 'used' if used_new.lower() == 'no' else 'certified'
    drivetrain = data[(data['Make'] == make) & data['Model'].str.contains(model, case=False)]['Drivetrain'].mode()[0]
    fuel_type = data[(data['Make'] == make) & data['Model'].str.contains(model, case=False)]['FuelType'].mode()[0]
    print("="*10)
    print(f"info about your car: \n",
        f'name - {make}, model - {model}, year - {year} \n',
        f'Rating - {consumerrating}, reviews - {consumerreviews} \n',
        f'Min - {minmpg}, max - {maxmpg} \n',
        f'mileage - {mileage}, status - {used_new} \n',
        f'drivetrain - {drivetrain}, fuel - {fuel_type}')
    print("="*10)
    # price = 150000


    new_entry = {
        'Year': year,
        'ConsumerRating': consumerrating,
        'ConsumerReviews': consumerreviews,
        'MinMPG' : minmpg,
        'MaxMPG' : maxmpg,
        'Mileage' : mileage,
        'Make_' + make: 1,
        'Model_'+model: 1,
        'Used/New_' + used_new: 1,
        'Drivetrain_' + drivetrain: 1,
        'FuelType_' + fuel_type : 1
    }

    df = df.append(new_entry, ignore_index=True)
    df = df.fillna(0)
    df = df.drop(['Price'], axis = 1)
    dmatrix = xgb.DMatrix(df)
    pred = loaded_model.predict(dmatrix)
    error = 4030.68
    print(f"Price for your car: {round(pred[0], 2)}+-{round(error, 2)}")
    print('-'*10)

predict_price(machine_bd)