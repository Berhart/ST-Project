import sys
class Hangman():
  
  def __init__(self, plain_word):
    plain_word_capitals = plain_word.upper()
    self._secret_word = list(plain_word_capitals)     
    self._correct_guess = [None]*len(plain_word_capitals) #current guess of the user
    self._available_letters = set(plain_word_capitals) #set of right letters availabe
    self._letters_tried = []
    self._number_of_errors = 0
    self._number_of_trials = 0
    self._finished = False #flag if the game is finished
  
  def play(self):
    self.print_introduction()
    
    while(not self._finished):
      guess = input("\nInsert new letter or the final word: ")
      self.try_add_guess(guess)
    
    if (self._number_of_errors == 11):
        print("\nYOU LOST!!")
        print("The correct word was: ", end="")
        for i in range(len(self._secret_word)):
        	print(self._secret_word[i], end="")
        print("");
    else:
        print("\nYOU WON!!!")
    print("Total Errors:    ", self._number_of_errors)
    print("Number of trials: ", self._number_of_trials)

  def try_add_guess(self, guess): # main function to check if inserted guess is valid
    if (guess == None or len(guess) == 0):
      print("Empty (string) input.\nWarning: This game only accepts 2 types of guesses: 1 character or the secret word. This will not count as an error neither as a trial.")
      return #if no input was given then ask again for an input. This is not considered as an error or trial
    
    elif (len(guess) == 1): # if the input is only a character
      guess = guess.upper()
     
      if (guess in self._available_letters):
        for i in range(len(self._secret_word)):
          if (self._secret_word[i] == guess):
            self._correct_guess[i] = guess
        
        self._letters_tried.append(guess)
        self._number_of_trials += 1       
        self.print_hangman()
        self.print_guess()
        self._available_letters.remove(guess)
        
        if(len(self._available_letters) == 0):
          self._finished = True
        
        return
        
      else: #The secret word doesnt contain the letter given, it will be considered as an error
        print("Char not found!")
        self._letters_tried.append(guess)
        self._number_of_errors += 1
        self._number_of_trials += 1
        self.print_hangman()
        self.print_guess()
        if (self._number_of_errors == 11):
            self._finished = True
            return
        
    elif (len(guess) == len(self._secret_word)): #if the guess given has the same size as the secret word
      guess = guess.upper()
      
      if(list(guess) == self._secret_word): #if they have the same letters in the same order
        for i in range(len(self._secret_word)):
            self._correct_guess[i] = self._secret_word[i]
        self._number_of_trials += 1
        self.print_guess()
        
        self._finished = True
        return
      
      else:
        print("The given guess does not match the secret word")
        self._number_of_errors += 1
        self._number_of_trials += 1
        self.print_hangman()
        self.print_guess()
        if (self._number_of_errors == 11):
            self._finished = True
            return        
    
    else: # This is not considered as an error neither as a trial
      print("Warning: This game only accepts 2 types of guesses: 1 character or the secret word. This will not count as an error neither as a trial.")
      return

  def print_guess(self): #print current guess
      l = len(self._correct_guess)
      print("Current Guess: ",end = "")
      for i in range(l):
          if (self._correct_guess[i] == None):
              print ("_  ",end = "")
          else:
              print (self._correct_guess[i]+ " ", end="")
      print()
      print("Letters tried : ", end="")
      for i in range(len(self._letters_tried)):
      	print(self._letters_tried[i] + "  ", end="")
      print()
                
  def print_hangman(self): #print the hangman
      print("====================")
      #first line
      if (self._number_of_errors >= 3):
          print("    ______")
      else:
          print("")
      #second line
      if (self._number_of_errors >= 5):
          print("    |/   |")
      elif (self._number_of_errors >= 4):
          print("    |/  ")
      elif (self._number_of_errors >= 2):
          print("    |  ")
      else:
          print("")
      #third line
      if (self._number_of_errors >= 6):
          print("    |    O")
      elif (self._number_of_errors >= 2):
          print("    |    ")
      else:
          print("")
      #fourth line
      if (self._number_of_errors >= 9):
          print("    |  --|--")
      elif (self._number_of_errors >= 8):
          print("    |  --|")
      elif (self._number_of_errors >= 7):
          print("    |    |")
      elif (self._number_of_errors >= 2):
          print("    |  ")
      else:
          print("")
      #fifth line
      if (self._number_of_errors >= 11):
          print("    |   / \\")
      elif (self._number_of_errors >= 10):
          print("    |   / ")
      elif (self._number_of_errors >= 2):
          print("    |")
      else:
          print("")
      #sixth line
      if (self._number_of_errors >= 2):
          print("  __|_________")
      elif (self._number_of_errors >= 1):
          print("  ____________")
      else:
          print("")
      print("====================")
      
      
  def print_introduction(self):
    print("====================")
    print("    ______")
    print("    |/   |")
    print("    |    O")
    print("    |  --|--")
    print("    |   / \\")
    print("  __|_________")
    print(" ===================")
    print("\t\t\tWelcome to \n\n")
    print("H    H     AA     N    N     GGGG    MM   MM    AA    N    N   !!")
    print("H    H    A  A    NN   N    G   GG   MMM MMM   A  A   NN   N   !!")
    print("HHHHHH   AAAAAA   N N  N    G        M MMM M  AAAAAA  N N  N   !!")
    print("H    H   A    A   N  N N    G  GGGG  M     M  A    A  N  N N   ")
    print("H    H   A    A   N   NN     GGGG    M     M  A    A  N   NN   !!")
    print("\n\n\nGuess the word\n")
    self.print_guess()      
      
if __name__ == '__main__':  
  Hangman(sys.argv[1]).play()