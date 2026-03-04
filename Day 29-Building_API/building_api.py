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
from bson.json_util import dumps
import pymongo
import os

app = Flask(__name__)
MONGODB_URI = 'mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority' 

client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python']

@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student(id):
    student = db.students.find({'id':ObjectId(id)})
    return Response(dumps(student),mimetype='application/json')

#-------------------------------------------------------------------------------------------#
from datetime import datetime

app = Flask(__name__)
MONGODB_URI = 'mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority' 

client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python']

@app.route('/api/v1.0',methods =['POST'])
def create_student():
    name = request.form['name'] 
    country = request.form['country'] 
    city = request.form['city'] 
    skills = request.form['skills'].split(',') 
    bio = request.form['bio'] 
    birthyear = request.form['birthyear'] 

    create_student = datetime.now()
    student = { 
        'name': name, 
        'country': country, 
        'city': city, 
        'birthyear': birthyear, 
        'skills': skills, 
        'bio': bio, 
        'created_at': create_student 
    }
    db.students.insert_one(student) 
    return 
#-------------------------------------------------------------------------------------------#

@app.route('/api/v1.0/students/<id>', methods = ['PUT'])
def update_student (id):
    query = {"_id":ObjectId(id)}
    name = request.form['name'] 
    country = request.form['country'] 
    city = request.form['city'] 
    skills = request.form['skills'].split(', ') 
    bio = request.form['bio'] 
    birthyear = request.form['birthyear'] 
    created_at = datetime.now()

    student = { 
        'name': name, 
        'country': country, 
        'city': city, 
        'birthyear': birthyear, 
        'skills': skills, 
        'bio': bio, 
        'created_at': created_at 
    }

    db.students.update_one(query, student) 
    return 

#-------------------------------------------------------------------------------------------#









