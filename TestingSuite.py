import unittest
from Hangman_class_version import *
      
class TestHangmanGame(unittest.TestCase):
   
   def setUp(self):
      "This runs before the test cases are executed"
      self.game = Hangman("secret_word")
      self.available_letters = self.game._available_letters.copy()
   
   def test_winGameWith0ErrorsAndGuessingAllCorrectLetters(self):
      self.game.print_introduction()
      for el in self.available_letters:
         self.assertEqual(self.game._finished, False)
         self.game.try_add_guess(el)
         
      self.assertEqual(self.game._finished, True)
      self.assertEqual(self.game._number_of_errors, 0)
      self.assertEqual(self.game._number_of_trials, len(self.available_letters))

   def test_winGameWith0ErrorsAnd1Trial(self):
      self.assertEqual(self.game._finished, False)
      self.game.try_add_guess("secret_word")
      self.assertEqual(self.game._finished, True)
      self.assertEqual(self.game._number_of_errors, 0)
      self.assertEqual(self.game._number_of_trials, 1)
      
   def test_loseGameWith11Trials(self):
      for i in range(len(self.game._secret_word)-1):
         #print(i)
         self.game.try_add_guess(str(i))
         self.assertEqual(self.game._finished, False)
      self.game.try_add_guess("x")
      
      self.assertEqual(self.game._finished, True)
      self.assertEqual(self.game._number_of_errors, 11)
      self.assertEqual(self.game._number_of_trials, 11)
      
   def test_emptyStringInputDoesNotChangeTheStateOfTheGame(self):
      
      self.assertEqual(self.game._finished, False)
      self.game.try_add_guess("")
      self.assertEqual(self.game._finished, False)
      self.assertEqual(self.game._number_of_errors, 0)
      self.assertEqual(self.game._number_of_trials, 0)
      
   def test_emptyInputDoesNotChangeTheStateOfTheGame(self):
      
      self.assertEqual(self.game._finished, False)
      self.game.try_add_guess(None)
      self.assertEqual(self.game._finished, False)
      self.assertEqual(self.game._number_of_errors, 0)
      self.assertEqual(self.game._number_of_trials, 0)   
      
   def test_InputNotAllowedDoesNotChangeTheStateOfTheGame(self):
      #if the input has more than one character and it doesnt have the length of
      #the secret word
      self.assertEqual(self.game._finished, False)
      self.game.try_add_guess("secret_wordd")
      self.assertEqual(self.game._finished, False)
      self.game.try_add_guess("secret_wor")
      self.assertEqual(self.game._finished, False)
      self.assertEqual(self.game._number_of_errors, 0)
      self.assertEqual(self.game._number_of_trials, 0)   
   
   def test_mistakenSecretWordInput(self):
      self.assertEqual(self.game._finished, False)
      self.game.try_add_guess("secret word")
      self.assertEqual(self.game._finished, False)
      self.assertEqual(self.game._number_of_errors, 1)
      self.assertEqual(self.game._number_of_trials, 1)
      
   def test_loseGameWith11TrialsAndFinalGuessBeingAMistakenSecretWord(self):
      for i in range(len(self.game._secret_word)-1):
         #print(i)
         self.game.try_add_guess(str(i))
         self.assertEqual(self.game._finished, False)
      self.game.try_add_guess("secret word")
      
      self.assertEqual(self.game._finished, True)
      self.assertEqual(self.game._number_of_errors, 11)
      self.assertEqual(self.game._number_of_trials, 11)
   

def suite():
   
   suite = unittest.TestSuite()

   suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestHangmanGame))

   return suite

 
if __name__ == '__main__':

   unittest.TextTestRunner(verbosity=2).run(suite())