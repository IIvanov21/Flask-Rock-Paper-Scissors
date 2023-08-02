import random

def play():
	user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
	computer = random.choice(['r','p','s'])
	
	print("User:" + user + " Computer:" + computer)

	if user == computer:
		return print('It\'s a tie')
	
	#Our rules r > s, s > p, p > r
	if is_win(user,computer):
		return print('You won!')
		
	return print('You lost!')
	
def is_win(player,opponent):
	#return true if player wins
		if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
			return True
		

play()