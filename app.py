from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import requests
import pandas as pd
import json
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

paises = ['BR', 'AR', 'UY','ES', 'DE', 'IT', 'US', 'MX', 'CA', 'CN', 'JP', 'NZ', 'AU', 'DZ', 'ZA', 'EG']
indicadores = ['77818','77819','77820']

def montaUrl(pais, indicador):
    return f"https://servicodados.ibge.gov.br/api/v1/paises/{pais}/indicadores/{indicador}"


with app.app_context():
   db.create_all()

class Saude(db.Model):
    __tablename__ = 'saude'
    id = db.Column(db.Integer, primary_key=True)
    pais = db.Column(db.String(50), unique = True, nullable = False)
    ano = db.Column(db.Integer, unique = True, nullable = True)
    indicador = db.Column(db.Float, unique = True, nullable = True)
    def json(self):
        return {'id': self.id, 'pais': self.pais, 'ano': self.ano, 'indicador': self.indicador}
class Educacao(Saude):
    __tablename__ = 'educacao'
    def json(self):
        return {'id': self.id, 'pais': self.pais, 'ano': self.ano, 'indicador': self.indicador}

class Turismo(Saude):
    __tablename__ = 'turismo'
    def json(self):
        return {'id': self.id, 'pais': self.pais, 'ano': self.ano, 'indicador': self.indicador}

@app.route('/test', methods=['GET'])
def test():
    return make_response(jsonify({'message': 'test'}), 200)

@app.route('/paises/', methods=['GET'])
def get_paises():
    try:
        for pais in paises:
            for indicador in indicadores:
                match indicador:
                    case '77818':
                        tablename = 'turismo'
                    case '77819':
                        tablename = 'educacao'
                    case '77820':
                        tablename = 'saude'
                getpais = requests.get(montaUrl(pais, indicador))
                dados = json.loads(getpais.text)
                unidade = dados[0]['unidade']['id']
                ano = dados[0]['series'][0]['serie']
                anoChaves = []
                anoValores=[]
                for i in ano:
                    if len(*i.keys()) == 4:
                        anoChaves.append(*i.keys())
                        anoValores.append(*i.values())
                local = [dados[0]['series'][0]['pais']['nome']]*len(anoChaves)        
                paisRepetido = pd.Series(local, name ='País')
                anoDF = pd.Series(anoChaves, name = 'Ano')
                anoValoresDF = pd.Series(anoValores, name = unidade)
                dataframe_pais = pd.concat([paisRepetido, anoDF, anoValoresDF], axis = 1)
                dataframe_pais.to_sql(tablename, db.engine, if_exists='append', index=False)
        return jsonify({'message':'Banco de dados criado!'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


