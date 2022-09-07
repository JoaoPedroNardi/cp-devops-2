from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CadastroForm(FlaskForm):
    nome = StringField('Nome do Jogador', [DataRequired()])
    clube = StringField('Clube', [DataRequired()])
    posicao = StringField('Posição', [DataRequired()])
    submit = SubmitField('Submit')
