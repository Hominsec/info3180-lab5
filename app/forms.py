from flask_wtf import FlaskForm#Essential
from wtforms import StringField, PasswordField,TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description=TextAreaField('Description', validators=[InputRequired()])
    poster=FileField('Poster',validators=[FileRequired(),FileAllowed(['jpg','png'], 'Images only!')])

#class UploadForm(FlaskForm):
    #photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg','png'],'Images only!')])
    