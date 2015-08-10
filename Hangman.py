import random


s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie", "This cool guy my gardener met yesterday", "Superman"]
p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]
s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes"]
p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on", "flee from", "try to automate", "explode"]
infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology."]

def sen_maker():
	return random.choice(s_nouns) + " " + random.choice(s_verbs) + " " + random.choice(s_nouns).lower() or random.choice(p_nouns).lower() + " " + random.choice(infinitives)
	
def gen_board(sentence):
	board = ""
	for char in sentence:
		if char == " ":
			board += " "
		else:
			board += "_"
	return board
def updateBoard(board, sentence, guess):
	oldBoard = board
	count = 0
	for char in sentence:
		if(char.lower() == guess.lower()):
			board = board[0:count] + sentence[count] + board[count+1:]
		count += 1
	if board == oldBoard:
		print "Sorry, that letter wasn't there!"


	print board
	return board
def main():
	lives = 5
	sentence = sen_maker()
	print sentence
	board = gen_board(sentence)
	print board
	while True:
		if (board == sentence):
			print("Congratulations, you win!")
			break
		guess = raw_input("Please guess a letter: ")
		oldBoard = board
		board = updateBoard(board,sentence,guess)
		if board == oldBoard:
			lives -= 1
			if lives != 1:
				print("You have " + str(lives) + " lives remaining.")
			else:
				print("You have " + str(lives) + " life remaining.")
			if lives == 0:
				print("You lose.")
				break



main()


