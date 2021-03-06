import unittest
from Hangman_class_version import *

class TestHangmanGame(unittest.TestCase):

	def setUp(self):
		self.game = Hangman()
		self.available_letters = self.game._available_letters.copy()
		self.notPresentLetters = list(set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) - set(self.available_letters))


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
		word = ""
		for i in range(len(self.game._secret_word)):
			word = word + self.game._secret_word[i]

		self.game.try_add_guess(word)
		self.assertEqual(self.game._finished, True)
		self.assertEqual(self.game._number_of_errors, 0)
		self.assertEqual(self.game._number_of_trials, 1)

	def test_loseGameWith11Trials(self):
		print(self.game._secret_word)
		print(self.notPresentLetters)
		for i in range(11):
			print(i)
			self.assertEqual(self.game._finished, False)
			self.game.try_add_guess(self.notPresentLetters[i])

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

	def test_sameInputTwiceDoesNotChangeTheStateOfTheGame(self):

		self.assertEqual(self.game._finished, False)
		self.game.try_add_guess(self.notPresentLetters[0])
		self.assertEqual(self.game._finished, False)
		self.assertEqual(self.game._number_of_errors, 1)
		self.assertEqual(self.game._number_of_trials, 1)
		self.game.try_add_guess(self.notPresentLetters[0])
		self.assertEqual(self.game._number_of_errors, 1)
		self.assertEqual(self.game._number_of_trials, 1)

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
		self.game.try_add_guess("a"*len(self.game._secret_word))
		self.assertEqual(self.game._finished, False)
		self.assertEqual(self.game._number_of_errors, 1)
		self.assertEqual(self.game._number_of_trials, 1)

	def test_WordWithDifferentLengthWithSameErrors(self):
		self.assertEqual(self.game._finished, False)
		self.game.try_add_guess("a"*(len(self.game._secret_word)+1))
		self.assertEqual(self.game._finished, False)
		self.assertEqual(self.game._number_of_errors, 0)
		self.assertEqual(self.game._number_of_trials, 0)

	def test_loseGameWith11MistakenSecretWord(self):
		print(self.game._secret_word)
		print(self.notPresentLetters)
		for _ in range(11):
			self.assertEqual(self.game._finished, False)
			self.game.try_add_guess("a"*len(self.game._secret_word))

		self.assertEqual(self.game._finished, True)
		self.assertEqual(self.game._number_of_errors, 11)
		self.assertEqual(self.game._number_of_trials, 11)

	def test_WinMessage(self):
		self.game._finished = True
		self.game.play()
		self.assertEqual(self.game._result, "WIN")

	def test_LostMessage(self):
		self.game._finished = True
		self.game._number_of_errors = 11
		self.game.play()
		self.assertEqual(self.game._result, "LOST")


def suite():

	suite = unittest.TestSuite()

	suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestHangmanGame))

	return suite


if __name__ == '__main__':

	unittest.TextTestRunner(verbosity=2).run(suite())
