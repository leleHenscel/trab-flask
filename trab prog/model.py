from config import *

class Musica(db.Entity):
    nome = Required(str)
    artista = Required(str)
    duracao = Required(str)
    genero = Required(str)
    def __str__(self):
        return f'{self.nome}, {self.artista}, {self.duracao}, {self.genero}'

db.bind(provider='sqlite', filename='musica.db', create_db=True)
db.generate_mapping(create_tables=True)