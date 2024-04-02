import random,sys
from hangman_art import hangman_pics,hangman_art_name
print(hangman_art_name)

print(hangman_pics[6])
#random_word_list=["apple","banana","orange","grape","pineapple"]
from hangman_words import random_word_list
life=6
x=1
global user_input_letter
#Selects a random word from the list
random_word=random.choice(random_word_list)
#print(random_word)
word_length=len(random_word)

#convert random word from string to list
random_word_list=list(random_word)
#print(random_word_list)

#Creates a string of underscores for the selected word and displays it
blank_word=""
for i in range(word_length):
  blank_word+="_"+" "
print(blank_word,"\n" )

#creates a list of underscores for the selected word
blank_word_list=[]
for i in range(word_length):
  blank_word_list+="_"
#print(blank_word_list)

#Get user input and checks number of letters enter by the user

def user_input():
  condition=True
  while condition:
    user_input_letter=input("Guess a letter:").lower()
    
    if user_input_letter.isalpha()==False:
      print("Please enter only alphabets\n")
      user_input()
    #print(user_input_letter)
    if len(user_input_letter)>1:
      print("Please enter only one letter")
    else:
      condition=False
    return user_input_letter
#Checks if the letter is present in the word and replaces the underscore with the letter


blank_words_string=""
while life>0 or count_blanks>0:
  letter=""
  z=""
  letter=user_input()
  #print("letter:",user_input_letter)
  
  if letter in random_word_list:
    for i in range(len(random_word)):
      if letter in random_word_list[i]:  
        blank_word_list[i]=letter
        #creates a string and display it with blanks and entered letter at specified postions
        blank_word_string="".join(blank_word_list)
    print(blank_word_string,"\n")   
    #print(blank_word_list)
    #counts no of blanks left after replacing with letters
    count_blanks=blank_word_list.count("_")
    #print("blanks:",count_blanks)
    if(count_blanks==0):
      print("Wow amazing.. You won the game. You just saved the hangman..")
      sys.exit()
    
    
  else:
    life-=1
    #print("x=",x)
    if life>=1:
      print("You are left with",life,"chances to guess.")
    print(hangman_pics[x])
    x=x+1
    if(life==0):
      print("Oh no..! You lost the game")
      sys.exit()
    
      



