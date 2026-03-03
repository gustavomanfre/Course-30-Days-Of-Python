 #Primer Ejemplo: Recuperando datos con GET usando datos ficticios
from flask import Flask, Response
import json
import os

app = Flask (__name__)

@app.route('/api/v1.0/students', methods = ['GET'])
def students():
    student_list = [{'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'skills':['HTML', 'CSS','JavaScript','Python']}]
    return Response(json.dumps(student_list), mimetype='application/json')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

#-------------------------------------------------------------------------------------------#
from flask import Flask, Response
import json
import pymongo
import os


app = Flask(__name__)
MONGODB_URI = 'mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority' 

client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python']

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():
    return Response(json.dumps(student), mimetype='application/json')

#-------------------------------------------------------------------------------------------#

from flask import Flask, Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util imports dumps
import pymongo
import os





