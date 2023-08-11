from flask import Flask, jsonify, request

from pymongo import MongoClient

from bson.objectid import ObjectId

 

 

app = Flask(__name__)

 

# Set up MongoDB connection

mongodb_uri ="mongodb+srv://1234:1234@cluster0.scppxjp.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(mongodb_uri)

db = client['FinalProject']

collection = db['NBA']

 

@app.route('/api/items', methods=['GET'])

def get_all_items():

    items = collection.find_one({'_id': ObjectId('64d405fb4bf34fb1dc48f292')})  

    item = items.get('results', [])

    return jsonify(item)

 

@app.route('/api/items/range/<start>/<end>', methods=['GET']) #gets player data between start and end

def get_range_items(start,end):

    items = collection.find_one({'_id': ObjectId('64d405fb4bf34fb1dc48f292')})  

    item = items.get('results', [])

    data = []

    for player in item:

        if player['id'] > int(start) and player['id'] < int(end):

            data.append(player)

    return jsonify(data)

 

@app.route('/api/items/<item_id>', methods=['GET']) #gets player data by id

def get_item_by_id(item_id):

    items = collection.find_one({'_id': ObjectId('64d405fb4bf34fb1dc48f292')})  

    item = items.get('results', [])

    data = []

    for player in item:

        print(player)

        if player['id'] == int(item_id):

            data.append(player)

    return jsonify(data)

       

 

if __name__ == '__main__':

    app.run(debug=True)

 

# TESTING URL's

#http://localhost:5000/api/items     GETS ALL DATA

#http://localhost:5000/api/items/range/1/20    GETS DATA BETWEEN CERTAIN RANGE

# http://localhost:5000/api/items/1    GETS DATA OF CERTAIN ID