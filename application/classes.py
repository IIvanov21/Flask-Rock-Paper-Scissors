from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DecimalField,IntegerField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

class RockPaperScissors(FlaskForm):
    choice = SelectField("User's Choice: ", choices=[("None","None"),("Rock","Rock"),("Paper","Paper"),("Scissors","Scissors")]) 
    submit = SubmitField('Confirm')
    computer=IntegerField("Computer: ")
    user=IntegerField("User: ")
    

class Score():
    userScore=0
    computerScore=0
        
        
        
            
	
    