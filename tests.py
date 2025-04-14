import unittest
from credit_card_validator import credit_card_validator


class CreditCardValidatorTest(unittest.TestCase):


    def test1(self):
        """
        Verifies if Master Cards with valid lengths and valid prefix (51-55) but an invalid check bits returns False .
        """
        self.assertFalse(credit_card_validator("5105105105106901"))  
    
    def test2(self):
        """
        Verifies if Master Cards with valid prefix (51-55) and check bits but invalid length returns False .
        """
        self.assertFalse(credit_card_validator("51051051051069"))  


    def test3(self):
        """
        Verifies if Visa cards with valid length and prefix but with invalid check bits returns False.
        """
        self.assertFalse(credit_card_validator("4111111111116900"))    

    def test4(self):
        """
        Verifies if Visa cards with valid prefix and valid check bits but invalid length returns False.
        """
        self.assertFalse(credit_card_validator("411111111111690111"))  

    def test5(self):
        """
        Verifies if Amex cards with valid prefix and length but invalid check bits returns False.
        """
        self.assertFalse(credit_card_validator("341111111111169"))  
    
    def test6(self):
        """
        Verifies if Amex cards with valid prefix and check bits but invalid length returns False.
        """
        self.assertFalse(credit_card_validator("37664007783269"))  

    def test7(self):
        """
        Verifies if Master Cards with valid lengths and valid prefix (2221-2720) but an invalid check bits returns False .
        """
        self.assertFalse(credit_card_validator("2221691051051100"))  
    
        
    def test8(self):
        """
        Verifies if Master Cards with valid prefix (2221-2720) and check bits but invalid length returns False .
        """
        self.assertFalse(credit_card_validator("22210"))  
    
    def test9(self):
        """
        Verifies if Master Cards with valid prefix (51-55) valid length and valid check bits passes .
        """
        self.assertFalse(credit_card_validator("5105105105695100"))  

    
if __name__ == '__main__':
    unittest.main()


    
    

