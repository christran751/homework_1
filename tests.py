import unittest
from credit_card_validator import credit_card_validator


class CreditCardValidatorTest(unittest.TestCase):

    def test_valid_master(self):
        """
        Verifies that it is an invalid Master Cards with invalid lengths
        """
        self.assertFalse(credit_card_validator("5105 1051 0510 510"))
        # Should be invalid because not enough length
    
    def test_valid_visa(self):
        """
        Verifies that it is an invalid Visa Cards with invalid prefix
        """
        self.assertFalse(credit_card_validator("9024 0071 5012 3456"))

    def test_valid_amex(self):
        """
        Verifies that is is an invalid Amex with invalid lengths and invalid prefix
        """
        self.assertFalse(credit_card_validator("0011 1111 1111 11171"))
    
    def test_random_number(self):
        """
        Verifis that a random number (e.g., 1234 5678 9999) should not be a valid card
        """
        self.assertFalse(credit_card_validator("1234 5678 9999 8924"))
    


if __name__ == '__main__':
    unittest.main()


    
    

        
