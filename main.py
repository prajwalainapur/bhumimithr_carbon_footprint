'''
fileName: API_Handler.py
fileDesc: Contains API routes for various API's required for carbon footprint calculation
createdBy: Prajwal Brijesh Ainapur
createdOn: 25-11-2023
'''

# Importing essential modules
from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 
from flask_cors import CORS

# Importing UDF's
import param as param
import calc_transport as scopet
import calc_scope3 as scope3
import calc_scope2 as scope2
import calc_scope1 as scope1

# creating a Flask app 
app = Flask('Bhumimithr Carbon Footprint Calculator')
api = Api(app)
CORS(app) 
print('Hello')

# on the terminal type: curl http://127.0.0.1:5000/transport
@app.route('/transport', methods = ['GET']) 
def _transport(): 
    if(request.method == 'GET'): 
        content = request.json

        emissions_unit = scopet.calculate_emissions(content)

        return jsonify({'data': emissions_unit})

# A simple function to calculate the square of a number 
# the number to be squared is sent in the URL when we use GET 
# on the terminal type: curl http://127.0.0.1:5000 / home / 10 
# this returns 100 (square of 10) 
@app.route('/scope3', methods = ['GET']) 
def _scope3(): 

    if(request.method == 'GET'): 
        content = request.json

        emissions_unit = scope3.calculate_scope3(content)

        return jsonify({'data': emissions_unit}) 
    
@app.route('/scope2', methods = ['GET']) 
def _scope2(): 

    if(request.method == 'GET'): 
        content = request.json

        emissions_unit = scope2.calculate_scope2(content)

        return jsonify({'data': emissions_unit})
     
@app.route('/scope1', methods = ['GET']) 
def _scope1(): 

    if(request.method == 'GET'): 
        content = request.json

        emissions_unit = scope1.calculate_scope1(content)

        return jsonify({'data': emissions_unit}) 

app.run(debug = True) 
