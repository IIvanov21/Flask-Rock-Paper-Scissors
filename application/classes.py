from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DecimalField,IntegerField, SelectField
from application import db
class RockPaperScissors(FlaskForm):
    choice = SelectField("User's Choice: ", choices=[("None","None"),("Rock","Rock"),("Paper","Paper"),("Scissors","Scissors")]) 
    submit = SubmitField('Confirm')
    computer=IntegerField("Computer: ")
    user=IntegerField("User: ")
    

class Score():
    userScore=0
    computerScore=0
        
        
class GameResult(db.Model):        
    id = db.Column(db.Integer, primary_key=True)
    player_choice = db.Column(db.String(20), nullable=False)
    computer_choice = db.Column(db.String(20), nullable=False)
    result = db.Column(db.String(20), nullable=False)      
	
    