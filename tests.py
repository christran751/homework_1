import unittest
from credit_card_validator import credit_card_validator


class CreditCardValidatorTest(unittest.TestCase):

    def test_valid_master(self):
        """
        Verifies if it is a valid Master Cards with valid lengths and valid prefix
        Passes if the credit card number is a valid Mastercard
        """
        self.assertFalse(credit_card_validator("5412 7512 3412 3456"))
    
    def test_valid_visa(self):
        """
        Verifies if it is a valid Visa with valid lengths and valid prefix
        Passes if the credit card number is a valid Visa
        """
        self.assertFalse(credit_card_validator("4111 1111 1111 1111"))

    def test_valid_amex(self):
        """
        Verifies if it is a valid Amex with valid lengths and valid prefix
        Passes if the credit card number is a valid Amex        
        """
        self.assertFalse(credit_card_validator("3482 822463 10005"))
    
    def test_random_number(self):
        """
        Verifis that a random number (e.g., 1234 5678 9999) 
        should not be a valid card
        """
        self.assertFalse(credit_card_validator("1234 5678 9999 8924"))
    
if __name__ == '__main__':
    unittest.main()


    
    

        
