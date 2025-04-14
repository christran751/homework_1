import unittest
from credit_card_validator import credit_card_validator


class CreditCardValidatorTest(unittest.TestCase):

    def test1(self):
        """
        Verifies if Master Cards with valid lengths and valid prefix but an invalid check bits returns False .
        """
        self.assertFalse(credit_card_validator("5105 1051 0510 6901"))  
    
    def test2(self):
        """
        Verifies if Master Cards with valid prefix and check bits but invalid length returns False .
        """
        self.assertFalse(credit_card_validator("5105 1051 0510 69"))  


    def test3(self):
        """
        Verifies if Visa cards with valid length and prefix but with invalid check bits returns False.
        """
        self.assertFalse(credit_card_validator("4111 1111 1111 6900"))    

    def test4(self):
        """
        Verifies if Visa cards with valid prefix and valid check bits but invalid length returns False.
        """
        self.assertFalse(credit_card_validator("4111 1111 1111 690"))  

    def test5(self):
        """
        Verifies if Amex cards with valid prefix and length but invalid check bits returns False.
        """
        self.assertFalse(credit_card_validator("3411 1111 1111 169"))  
    
    def test6(self):
        """
        Verifies if Amex cards with valid prefix and check bits but invalid length returns False.
        """
        self.assertFalse(credit_card_validator("3411 1111 1111 690"))  

    
if __name__ == '__main__':
    unittest.main()


    
    

        
