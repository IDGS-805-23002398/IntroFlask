from wtforms import Form, RadioField
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators


class UserForm(Form): #HEREDA DE LA CLASE FORM
    matricula = IntegerField('Matricula',[
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100,max=1000, message="Ingrese un valor valido")
        ]) #Lo de adentro es el nombre de la etiqueta del label
    nombre = StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese un nombre valido")
    ])
    aPaterno = StringField('Apaterno',[
        validators.DataRequired(message="El campo es requerido"),
    ])
    aMaterno = StringField('Amaterno', [
        validators.DataRequired(message="El campo es requerido"),
    ])
    correo = EmailField('Correo', [
        validators.Email(message="Ingrese un correo valido"),
    ])
    
class CinepolisForm(Form): #HEREDA DE LA CLASE FORM
    nombre = StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese un nombre valido")
    ])
    compradores = IntegerField('CantidadCompradores',[
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, message="Ingrese un valor valido")
        ])
    cineco = RadioField('isCineco', choices=[('no','No'),('si','Si')])
    boletos = IntegerField('CantidadBoletos',[
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, message="Ingrese un valor valido")
        ])
