import random


def printletters(list,nlist):
    # Pring the characters in the list
    for i in range(nlist):
        print(list[i]," ",end="")
    print()    
def fillguess(word, guess, length, letter):
  numletters = 0
  for i in range(length):
    if letter == word[i]:
      guess[i]=letter
      numletters+=1
  return numletters
#################### Main Program #################################
numguessed=0
lives=8
numwords = 370105
wordfile = open("words_alpha.txt","r")
wordlist = [""] * numwords
# This removes the newline
for i in range(numwords):
  wordlist[i] = wordfile.readline().strip("\n")
# Generate the random word
index = random.randint(0,numwords-1)
word=wordlist[index]
# Read in word to be guessed
# Store the number of letters in the answer
length=len(word)
guess=["_"]*length
while lives > 0 and numguessed<length:
  printletters(guess,length)
  letter=input("what letter do you think it is?")
  num = fillguess(word, guess, length, letter)
  if num>0:
    numguessed = numguessed + num
  else:
    lives = lives - 1
if lives > 0:
  print("You are a winner")
  print(f"The word is {word}")
else:
  print("You have lost")
  print(f"The word is {word}")
