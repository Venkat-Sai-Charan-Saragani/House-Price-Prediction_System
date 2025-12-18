import os 
from flask import Flask, render_template, request, jsonify
import pandas as pd 
import pickle


app = Flask(__name__, template_folder="templates")
data = pd.read_csv('final_datase.xls')
pipe = pickle.load(open('RidgeModel.pkl', 'rb'))


@app.route('/')
def index():
    bedrooms = sorted(data['beds'].unique())
    bathrooms = sorted(data['baths'].unique())
    sizes = sorted(data['size'].unique())
    zip_codes = sorted(data['zip_code'].unique())

    return render_template('index.html', bedrooms=bedrooms, bathrooms=bathrooms, sizes=sizes, zip_codes=zip_codes)

@app.route('/predict',methods = ['POST'])
def predict():
    bedrooms = float(request.form.get('beds'))
    bathrooms = float(request.form.get('baths'))
    size = float(request.form.get('size'))
    zipcode = int(request.form.get('zip_code'))


    #  Create a DataFrame with the input data
    input_data = pd.DataFrame([[bedrooms, bathrooms, size, zipcode]],
                                columns=['beds','baths','size','zip_code'])
    

    print('Input Data:')
    print(input_data, flush = True)


    #  handle unknown categories in the input data
    for col in input_data.columns:
        unknown = set(input_data[col]) - set(data[col].unique())
        if unknown:
            # Handle unknown categories (e.g., replace with a default value)
            input_data[col] = data[col].mode()[0]

    print("Processed Input Data:")
    print(input_data, flush = True)

    #Predict the price
    prediction = pipe.predict(input_data)[0]
    print('Prediction:', prediction, flush=True)

    return str(round(float(prediction),2))

if __name__ == "__main__":
    app.run(debug = True, port = 5000)



