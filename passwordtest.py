import unittest
import password
import re


class PasswordValidationCase(unittest.TestCase):
    data = password.pwd_generator(1)

    def testPasswordHasUpperCaseCharacter(self, values=data):
        for i in values:
            with self.subTest():
                print(i)
                self.assertTrue(len(re.split("[A-Z]+", i)) != 1)

    def testPasswordHasLowerCaseCharacter(self, values=data):
        for i in values:
            with self.subTest():
                print(i)
                self.assertTrue(len(re.split("[a-z]+", i)) != 1)

    def testPasswordHasDigit(self, values=data):
        for i in values:
            with self.subTest():
                print(i)
                self.assertTrue(len(re.split("\\d+", i)) != 1)

    def testPasswordHasSpecialChar(self, values=data):
        for i in values:
            with self.subTest():
                print(i)
                self.assertTrue(len(re.split("[~!@#$%^&()_+=]+", i)) != 1)

    def testPasswordHasEnoughLength(self, values=data):
        for i in values:
            with self.subTest():
                print(i)
                self.assertTrue(len(i) >= 6)


if __name__ == '__main__':
    unittest.main()
