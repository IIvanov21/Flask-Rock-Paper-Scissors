import random

def play():
	user = input("What is your choice? 'Rock' for rock, 'Paper' for paper, 'Scissors' for scissors\n")
	computer = random.choice(['Rock','Paper','s'])
	
	print("User:" + user + " Computer:" + computer)

	if user == computer:
		return print('It\'s a tie')
	
	#Our rules r > s, s > p, p > r
	if is_win(user,computer):
		return print('You won!')
		
	return print('You lost!')
	
def is_win(player,opponent):
	#return true if player wins
		if(player == 'Rock' and opponent == 'Scissors') or (player == 'Scissors' and opponent == 'Paper') or (player == 'Paper' and opponent == 'Rock'):
			return True
		

play()