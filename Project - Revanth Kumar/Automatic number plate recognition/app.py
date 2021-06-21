from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def check(output):
    url = "https://zyanyatechl-license-plate-recognition-v1.p.rapidapi.com/recognize_url"

    querystring = {"image_url":output, "sourceType":"url"}

    payload='''{\r\n \"image_url\": "'''+output+'''",\r\n \"sourceType\":\"url\"\r\n}'''

    headers = {
        'x-rapidapi-key': "dac1b02f72msh4f30923e5a87bdbp1bf533jsne0baaeb3a6b9", 
        'x-rapidapi-host': "zyanyatech1-license-plate-recognition-v1.p.rapidapi.com"
        }
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    print (response. text) 
    return response.json() ["results"][0]["plate"], response.json() ["results"][0]["confidence"]
    
@app.route('/')
def home():
    return render_template('base.html')

@app.route('/predict',methods=['POST'])
def predict():
    output=request.form['output']
    plate,conf=check(output)
    return render_template('base.html',output=plate+" with confidence score: "+str(round(conf))+"%")

if __name__=='__main__':
    app.run(debug=False,port=5000)
    