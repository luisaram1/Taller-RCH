from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FloatField, IntegerField
from wtforms.validators import DataRequired, Optional

class LoginForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Ingresar")

class VehicleForm(FlaskForm):
    plate = StringField("Placa", validators=[DataRequired()])
    brand = StringField("Marca", validators=[Optional()])
    model = StringField("Modelo", validators=[Optional()])
    client_id = IntegerField("ID Cliente", validators=[DataRequired()])
    submit = SubmitField("Guardar")

class RepairForm(FlaskForm):
    description = TextAreaField("Descripción", validators=[DataRequired()])
    cost = FloatField("Costo", validators=[Optional()])
    submit = SubmitField("Agregar")
