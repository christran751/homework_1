import unittest
from credit_card_validator import credit_card_validator


class CreditCardValidatorTest(unittest.TestCase):


    def test1(self):
        """
        Verifies if Master Cards with valid lengths and valid prefix (51-55) but an invalid check bits returns False .
        """
        self.assertFalse(credit_card_validator("5205105105106901"))  
    
    def test2(self):
        """
        Verifies if Master Cards with valid prefix (51-55) and check bits but invalid length returns False .
        """
        self.assertFalse(credit_card_validator("55051051051008123"))  


    def test3(self):
        """
        Verifies if Visa cards with valid length and prefix but with invalid check bits returns False.
        """
        self.assertFalse(credit_card_validator("4111111111116901"))    

    def test4(self):
        """
        Verifies if Visa cards with valid prefix and valid check bits but invalid length returns False.
        """
        self.assertFalse(credit_card_validator("411111111111690111"))  

    def test5(self):
        """
        Verifies if Amex cards with invalid prefix and invalid check bits but valid length returns False.
        """
        self.assertFalse(credit_card_validator("331111111111163"))  
    
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
        self.assertTrue(credit_card_validator("5105105105695100"))  
    
    def test10(self):
        """
        Verifies if Master Card or Visa with invalid prefix but valid length and valid check bits will return False .
        """
        self.assertFalse(credit_card_validator("3340951283138748"))  
    
    def test11(self):
        """
        Verifies if Master Cards with valid prefix (2221-2720) valid length and valid check bits passes .
        """
        self.assertTrue(credit_card_validator("2221133742069162"))  
    
    def test12(self):
        """
        Verifies if Visa Cards with valid prefix valid length and valid check bits passes .
        """
        self.assertTrue(credit_card_validator("4720133742069164"))  

    def test13(self):
        """
        Verifies if Amex Cards with valid prefix valid length and valid check bits passes .
        """
        self.assertTrue(credit_card_validator("372013374206913"))  
    
    def test14(self):
        pass
 

    def test15(self):
        """
        Verifies that an empty string should returns False.
        """
        self.assertFalse(credit_card_validator("")) 
    
    def test16(self):
        """
        """
        self.assertFalse(credit_card_validator("1111111")) 

    def test17(self):
        """
        """
        self.assertFalse(credit_card_validator("ohmygodwtf")) 

    
if __name__ == '__main__':
    unittest.main()


    
    

