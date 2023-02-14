from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import requests, json, os

app = Flask(__name__)
endpoint = "https://demo5.cognitiveservices.azure.cn/language/:query-knowledgebases?projectName=demo5&api-version=2021-10-01&deploymentName=test"
# data = json.dumps({'question':'how to access azure cn'}) 
headers = {'Ocp-Apim-Subscription-Key':'d2cae8cd0fd341a39ba457dcd372a7d9', 'Content-Type':'application/json'}

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       data = json.dumps({'question':name}) 
       req = requests.post(endpoint, data=data, headers=headers)
       answer = req.json()
       return render_template('hello.html', name = answer['answers'][0]['answer'])
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()