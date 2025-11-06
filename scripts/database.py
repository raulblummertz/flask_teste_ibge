from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  

class TabelaBase(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    pais = db.Column(db.String(50), nullable = False)
    ano = db.Column(db.Integer, nullable = True)
    indicador = db.Column(db.Float, nullable = True)
    def json(self):
        return {'id': self.id,'pais': self.pais, 'ano': self.ano, 'indicador': self.indicador}

class Saude(TabelaBase):
    __tablename__ = 'saude'
    def json(self):
        return {'id': self.id,'pais': self.pais, 'ano': self.ano, 'indicador': self.indicador}
class Educacao(TabelaBase):
    __tablename__ = 'educacao'
    def json(self):
        return {'id': self.id,'pais': self.pais, 'ano': self.ano, 'indicador': self.indicador}
class Turismo(TabelaBase):
    __tablename__ = 'turismo'
    def json(self):
        return {'id': self.id, 'pais': self.pais, 'ano': self.ano, 'indicador': self.indicador}

