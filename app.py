from scripts.database import db
from scripts.extract import extrair_dados
from scripts.transform import tl_dados
from flask import Flask, jsonify
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db.init_app(app)

with app.app_context():
    db.create_all()

paises = "BR|AR|UY|ES|DE|IT|US|MX|CA|CN|JP|NZ|AU|DZ|EG|ZA"
indicadores = "77818|77819|77820"

@app.route('/paises/', methods=['GET'])
def etl():
    dados = extrair_dados(paises, indicadores)
    tl_dados(dados)
    return jsonify({'message':'ETL concluído!'}), 200

