from flask import Flask, request, jsonify, make_response
from dbhelpers import run_statement, serialize_data
import json

app = Flask(__name__)

animal_columns = ['id', 'name', 'species']

@app.get('/home')
def get_all_animal():
 try: 
   result = run_statement('CALL get_all_animals()')
   print(result[0])
   formatted_animals = serialize_data(animal_columns, result)
   return make_response(formatted_animals, 200)
 except Exception as error:
  return make_response(error, 500)
 
@app.get('/species/dog')
def get_all_dog_species():
 try: 
   result = run_statement('CALL get_all_dog_species()')
   print(result[0])
   formatted_animals = serialize_data(animal_columns, result)
   return make_response(formatted_animals, 200)
 except Exception as error:
  return make_response(error, 500)
 

@app.get('/species/cat')
def get_all_cat_species():
 try:
  result = run_statement('CALL get_all_cat_species()')
  print(result[0])
  formatted_animals = serialize_data(animal_columns, result)
  return make_response(formatted_animals, 200)
 except Exception as error:
  return make_response(error, 500)
 


app.run(debug=True)