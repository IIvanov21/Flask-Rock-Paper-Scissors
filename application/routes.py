from flask.templating import render_template
from flask import Flask, render_template, request
from application import app,db
from application.classes import RockPaperScissors
from application.classes import Score, GameResult
import random

userStats=Score()

@app.route('/',methods=['GET','POST'])
def game():
    error=""
    user_form=RockPaperScissors()
    if request.method=="POST":
        if user_form.choice.data=="None":
            error="Please select an option other than 'None'!"
        else:
            computer = random.choice(['Rock','Paper','Scissors'])
            if user_form.choice.data == computer:
                error ='It\'s a tie!'
            #Our rules r > s, s > p, p > r
            elif is_win(user_form.choice.data,computer):
                error='You won!'
                userStats.userScore+=1
            else:
                error='You lost!'
                userStats.computerScore+=1
            user_form.user.data=userStats.userScore
            user_form.computer.data=userStats.computerScore
            game_result=GameResult(player_choice=user_form.choice.data,computer_choice=computer, result=error)
            db.session.add(game_result)
            db.session.commit()   
        
           
                
    error=error+"You can keep playing by selecting another option from the list and pressing 'Confirm'!"
    return render_template("game.html",user_form=user_form,message=error)

def is_win(player,opponent):
        #return true if player wins
            if(player == 'Rock' and opponent == 'Scissors') or (player == 'Scissors' and opponent == 'Paper') or (player == 'Paper' and opponent == 'Rock'):
                return True

@app.route('/result',methods=['GET','POST'])
def game_results():
     game_history=GameResult.query.all()
     return render_template('result.html',game_history=game_history)