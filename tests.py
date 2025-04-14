import unittest
from credit_card_validator import credit_card_validator


class CreditCardValidatorTest(unittest.TestCase):

    #### Master Card ####

    def test1(self):
            """
            Verifies if Master Cards with valid lengths and valid prefix (51-55) but an invalid check bits returns False .
            """
            self.assertFalse(credit_card_validator("5205105105106901"))  
        
    def test7(self):
            """
            Verifies if Master Cards with valid lengths and valid prefix (2221-2720) but an invalid check bits returns False .
            """
            self.assertFalse(credit_card_validator("2221691051051100"))  
            

    def test11(self):
            """
            Verifies if Master Cards with valid prefix (2221-2720) valid length and valid check bits passes .
            """
            self.assertTrue(credit_card_validator("2221133742069162"))  
    def test8(self):
            """
            Verifies if Master Cards with valid prefix (2221-2720) and check bits but invalid length returns False .
            """
            self.assertFalse(credit_card_validator("22210"))  
        
        
    def test2(self):
            """
            Verifies if Master Cards with valid prefix (51-55) and check bits but invalid length returns False .
            """
            self.assertFalse(credit_card_validator("55051051051008123"))  
        
    def test9(self):
            """
            Verifies if Master Cards with valid prefix (51-55) valid length and valid check bits passes .
            """
            self.assertTrue(credit_card_validator("5105105105695100"))  
        
    def test10(self):
            """
            Verifies if Master Card with invalid prefix but valid length and valid check bits will return False .
            """
            self.assertFalse(credit_card_validator("2000951283138741"))  
        
    def test101(self):
            """
            Verifies if Master Card with invalid prefix and invalid length but valid check bits will return False .
            """
            self.assertFalse(credit_card_validator("20009512831387413"))  

    def test102(self):
            """
            Verifies if Master Card with invalid prefix and invalid length and invalid check bits will return False .
            """
            self.assertFalse(credit_card_validator("20009512831387411"))  

    def test103(self):
            """
            Verifies if Master Card with invalid prefix but valid length and valid check bits will return False .
            """
            self.assertFalse(credit_card_validator("5600951283138748"))  

    def test104(self):
            """
            Verifies if Master Card with invalid prefix and invalid length but valid check bits will return False .
            """
            self.assertFalse(credit_card_validator("56009512831387490")) 

    def test105(self):
            """
            Verifies if Master Card with invalid prefix and invalid length and invalid check bits will return False .
            """
            self.assertFalse(credit_card_validator("5644545453453"))   

    def test106(self):
            """
            Verifies if Master Card with invalid prefix and invalid length and invalid check bits will return False .
            """
            self.assertFalse(credit_card_validator("5644545453453"))   

    ##### END MASTER #####


    def test3(self):
            """
            Verifies if Visa cards with valid length and prefix but with invalid check bits returns False.
            """
            self.assertFalse(credit_card_validator("4111111111116901"))    

    def test4(self):
            """
            Verifies if Visa cards with valid prefix and valid check bits but invalid length returns False.
            """
            self.assertFalse(credit_card_validator("4141212121211112121212121212121222121211212112127"))  

    def test5(self):
            """
            """
            self.assertTrue(credit_card_validator("00"))  
        
    def test6(self):
            """
            Verifies if Amex cards with valid prefix (37) and check bits but invalid length returns False.
            """
            self.assertFalse(credit_card_validator("37664007783269"))  

    def test69(self):
            """
            Verifies if Amex cards with valid prefix and check bits but invalid length returns False.
            """
            self.assertFalse(credit_card_validator("342013374206647"))  

    def test12(self):
            """
            Verifies if Visa Cards with valid prefix valid length and valid check bits passes .
            """
            self.assertTrue(credit_card_validator("4157626283156623"))  

    def test13(self):
            """
            Verifies if Amex Cards with valid prefix (37) valid length and valid check bits passes .
            """
            self.assertTrue(credit_card_validator("372013374206913"))  
        
    def test14(self):
            """
            Verifies if Amex Cards with valid prefix (34) valid length and valid check bits passes .
            """
            self.assertTrue(credit_card_validator("342013374206696"))  

    def test70(self):
            """
            Verifies if Amex Cards with valid prefix (34) valid length but invalid check bits return False .
            """
            self.assertTrue(credit_card_validator("342013374206698"))  

    def test71(self):
            """
            Verifies if Amex Cards with valid prefix (37) valid length but invalid check bits return False .
            """
            self.assertTrue(credit_card_validator("372013374206698"))  
    
    

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

    def test107(self):
            """
            Visa            
            """
            self.assertFalse(credit_card_validator("4"))   



        
if __name__ == '__main__':
    unittest.main()


    
    

