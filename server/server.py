from flask import Flask,render_template
from flask_pymongo import PyMongo
from pymongo import MongoClient
import os
from bson.json_util import dumps
import pprint

client = MongoClient('mongodb', 27017)
app = Flask(__name__)

app.config['MONGO_URI'] = os.environ.get('DB')
mongo = PyMongo(app)
PORT = os.environ.get('PORT')

@app.route('/')
def hello_world():
    db=client.test
    #Poubelle en verre
    trashVerres=dumps(db.verre.find())
    #Aire de jeux
    airesDeJeux=dumps(db.airejeux.find())
    #Bancs
    bancs=dumps(db.banc.find())
    #Bar
    bars=dumps(db.bar.find())
    #bus
    bus_ligne=dumps(db.bus.find())
    #canisettte
    canisettes=dumps(db.canisette.find())
    #corbeille
    corbeilles=dumps(db.corbeille.find())
    #fontaine
    fontaine=dumps(db.fontaine.find())
    #horodateur
    horodateur=dumps(db.horodateur.find())
    #idcycle
    idcycle=dumps(db.idcycle.find())
    #parking
    parking=dumps(db.parking.find())
    #parkingvelo
    parkingvelo=dumps(db.parking.find())
    #pistecycle
    pistecycle=dumps(db.pistecycle.find())
    #stationnement
    stationnement=dumps(db.pistecycle.find())
    return render_template("index.html",poubelle_verres=trashVerres,aireDeJeux=airesDeJeux,bancs=bancs,bars=bars,bus=bus_ligne,canisettes=canisettes,corbeilles=corbeilles,fontaine=fontaine,horodateur=horodateur,idcycle=idcycle,parking=parking,parkingvelo=parkingvelo,pistecycle=pistecycle,stationnement=stationnement)

if __name__=='__main__':
    app.config['DEBUG'] = os.environ.get('ENV') == 'development' # Debug
    app.run(host='0.0.0.0', port=int(PORT))
