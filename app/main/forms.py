from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
# from wtforms import StringField,PasswordField,BooleanField,SubmitField

class pitchForm(FlaskForm):

    title = StringField('pitch Title'validators=[Required()])
    author = StringField('Author'validators=[Required()])
    pitch-content = TextAreaField('write pitch', validators=[Required()])
    submit = SubmitField('Submit')

class Updateprofile(FlaskForm):
    bio = TextAreaField('write comment...',validators = [Required()])
    submit = SubmitField('Submit')
    # remember = BooleanField('Remember me')
    # submit = SubmitField('Sign In')

class CommentForm(FlaskForm):
    bio = TextAreaField('write comment...',validators = [Required()])
    submit = SubmitField('Submit')

