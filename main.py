from flask import Flask, render_template, url_for, request, jsonify
import pandas as pd
import numpy as np
import datetime
import pickle


app = Flask(__name__, template_folder="templates")
model = pickle.load(open("xgb_model.pkl", "rb"))
print("Model Loaded")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == "POST":
        
        job_type = float(request.form['job_type'])
        python = float(request.form['python'])
        sql = float(request.form['sql'])
        ml = float(request.form['ml'])
        r = float(request.form['r'])
        hadoop = float(request.form['hadoop'])
        tableau = float(request.form['tableau'])
        sas = float(request.form['sas'])
        spark = float(request.form['spark'])
        java = float(request.form['java'])
        others = float(request.form['others'])
        
        df = pd.DataFrame(
            data = [[
            job_type,
            python,
            sql,
            ml,
            r,
            hadoop,
            tableau,
            sas,
            spark,
            java,
            others]],
            columns=[
                'Job_Type',
                'python',
                'sql',
                'machine learning',
                'r',
                'hadoop',
                'tableau',
                'sas',
                'spark',
                'java',
                'Others'])
        pred = model.predict(df)[0]
        output = pred
    return render_template("index.html", prediction=output)


if __name__ == '__main__':
    app.run(debug=True)
