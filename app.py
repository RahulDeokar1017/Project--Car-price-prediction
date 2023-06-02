from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd
import numpy as np
import warnings
import sklearn.linear_model
warnings.filterwarnings("ignore", category=UserWarning)


app=Flask(__name__)
car=pd.read_csv("cleaned_car.csv")

cors=CORS(app)
model=pickle.load(open("carpricemodel2.pkl",'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    
    companiesp=sorted(car["company"].unique())
    
    modelp=sorted(car["name"].unique())
    
    yearp=sorted(car["year"].unique())
    
    fuel_typep=sorted(car["fuel_type"].unique())
    
    return render_template("index.html",companies=companiesp ,model=modelp,year=yearp,fuel_type=fuel_typep)

@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():
     company=request.form.get('company')

     car_model=request.form.get('car_models')
     year=request.form.get('year')
     fuel_type=request.form.get('fuel_type')
     driven=request.form.get('kilo_driven')

     data = pd.DataFrame({'name': [car_model], 'company': [company], 'year': [year], 'kms_driven': [driven], 'fuel_type': [fuel_type]})
     prediction = model.predict(data)
     
         
    # data = pd.DataFrame(np.array(["Maruti Suzuki Ritz","Maruti",2011,50000,"Petrol"]).reshape(1, -1), columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
     #prediction = model.predict(data)
     



     

     #return str(np.round(prediction[0],2))
     return "Hello World"
    



if __name__=="__main__":
    app.run(debug=False)