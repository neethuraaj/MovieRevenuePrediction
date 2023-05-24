from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd
model = pickle.load(open('CBR.pkl','rb'))
le1=pickle.load(open('leR1.pkl','rb'))
le2=pickle.load(open('leR2.pkl','rb'))
scaler1=pickle.load(open('SC1.pkl','rb'))
scaler2=pickle.load(open('SC2.pkl','rb'))
app = Flask(__name__)
# Load the dataset
dataset = pd.read_csv('CLEAN.csv')

# Get the unique values from the 'genres' column
genres=dataset['genres'].unique().tolist()
genres=sorted(genres)

# Get the unique values from the 'production_companies' column
production_companies = dataset['production_companies'].unique().tolist()
production_companies=sorted(production_companies)

@app.route('/')
def index():
    return render_template('index.html',genres=genres,production_companies=production_companies)

@app.route('/predict',methods=['POST'])
def predict_class():
    genres = request.form.get("genres")
    production_companies = request.form.get("production_companies")
    budget = float(request.form.get("Budget"))
    runtime = float(request.form.get("Runtime"))
    month=int(request.form.get("Month"))
    year=int(request.form.get("Year"))
    day_of_week=int(request.form.get("Day"))
               
    result = model.predict(np.array([le1.transform([genres]),le2.transform([production_companies]),scaler1.transform([[budget]]),scaler2.transform([[runtime]]),month,year,day_of_week]).reshape(1,7))
    
    result=result.item()  
    result=round(result,2)
    return render_template ('res.html',prediction_text="Predicted Revenue is $.{}".format(result))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
    
@app.route('/home')
def home():
    return render_template('index.html',genres=genres,production_companies=production_companies)
if __name__ == '__main__':
    app.run(debug=True)