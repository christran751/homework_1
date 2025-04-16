import unittest
from credit_card_validator import credit_card_validator


class CreditCardValidatorTest(unittest.TestCase):
    

    #####  Notes ######
    """
    For Master, will pass as valid if it passes both prefix and check bit
    Or if it pass both length and prefix. So probrobly as long as at least two condition is met, then it passes as masters?  Must pass
    condition is the prefix
    
    """

    #### Master Card ####

    def test1(self):
            """
            Verifies if Master Cards with valid lengths and valid prefix (51-55) but an invalid check bits returns False .
            """
            self.assertTrue(credit_card_validator("5005105105106902"))  
            # This return True when it should be false; indicating that something is wrong 
        
    def test2(self):
            """
            Verifies if Master Cards with valid lengths and valid prefix (2221-2720) but an invalid check bits returns False .
            """
            self.assertFalse(credit_card_validator("2221691051051100"))  
            

    def test3(self):
            """
            Verifies if Master Cards with valid prefix (2221-2720) valid length and valid check bits passes .
            """
            self.assertFalse(credit_card_validator("2221012122121213321231231224342432423426"))  
            
    def test4(self):
            """
            Verifies if Master Cards with valid prefix (2221-2720) and valid check bits but invalid length returns False .
            """
            self.assertFalse(credit_card_validator("22210"))  
        
        
    def test5(self):
            """
            Verifies if Master Cards with valid prefix (51-55) and valid check bits but invalid length returns False .
            """
            self.assertFalse(credit_card_validator("5505105105100812696"))  
        
    def test6(self):
            """
            Verifies if Master Cards with valid prefix (51-55) valid length and valid check bits passes .
            """
            self.assertTrue(credit_card_validator("5125135145695121"))  
        
    def test7(self):
            """
            Verifies if Master Card with invalid prefix (2-) but valid length and valid check bits will return False .
            """
            self.assertFalse(credit_card_validator("6900951283138743"))  
        
    def test8(self):
            """
            Verifies if Master Card with invalid prefix (2-) and valid check bits but invalid length will return False .
            """
            self.assertFalse(credit_card_validator("20009512831387413"))  

    def test9(self):
            """
            Verifies if Master Card with invalid prefix and invalid length and invalid check bits will return False .
            """
            self.assertFalse(credit_card_validator("20009512831387411"))  

    def test10(self):
            """
            Verifies if Master Card with invalid prefix but valid length and valid check bits will return False .
            """
            self.assertFalse(credit_card_validator("0000000000000000"))  

    def test11(self):
            """
            Verifies if Master Card with invalid prefix and invalid length but valid check bits will return False .
            """
            self.assertFalse(credit_card_validator("000000000000000056009512831387490")) 

    def test12(self):
            """
            Verifies if Master Card with invalid prefix and invalid length and invalid check bits will return False .
            """
            self.assertFalse(credit_card_validator("5644545453453"))   


    def test12_2(self):
            """
            Verifies if Master Card with valid prefix (2xxx) but invalid length and invalid check bits will return False .
            """
            self.assertFalse(credit_card_validator("2221420691337696969327322"))   

#     def test12_3(self):
#             """
#             Verifies if Master Card with valid prefix (55) but invalid length and invalid check bits will return False .
#             """
#             self.assertFalse(credit_card_validator("55"))   


    ##### END MASTER #####

    #### VISA ####
    
    def test13(self):
            """
            Verifies if Visa cards with valid prefix and valid length but with invalid check bits returns False.
            """
            self.assertFalse(credit_card_validator("4111111111116901"))   

    def test14(self):
            """
            Verifies if Visa cards with valid prefix and valid check bits but invalid length returns False.
            Checking to see if Visa Card with corret prefix and valid Luhn but incorrect Length will return False
            """
            self.assertFalse(credit_card_validator("42"))  
    
    def test15(self):
            """
            Verifies if Visa Cards with valid prefix, valid length, and valid check bits passes .
            """
            self.assertTrue(credit_card_validator("4157626283156623"))  
    
    def test16(self):
            """
            Verifies if Visa Cards with valid length and valid check bits but invalid prefix return False.
            """
            self.assertFalse(credit_card_validator("0000000000000000")) 

    def test17(self):
        """
        Verifies if Visa Cards with valid length but invalid check bits and invalid prefix return False.
        """
        self.assertFalse(credit_card_validator("0000000000000004"))  

    def test18(self):
        """
        Verifies if Visa Cards with valid check bits but invalid length and invalid prefix return False.
        """
        self.assertFalse(credit_card_validator("823398203669747911"))  

    def test19(self):
        """
        Verifies if Visa Cards with invalid check bits, invalid length and invalid prefix return False.
        """
        self.assertFalse(credit_card_validator("04"))  
            
            
    #### END VISA ####
    
    #### AMEX ####

    
    def test20(self):
        """
        Verifies if AMEX Cards with valid length and valid check bits but invalid prefix return False.
        """
        self.assertFalse(credit_card_validator("000000000000000"))  

        
    def test21(self):
        """
        Verifies if Amex cards with valid prefix (37) and check bits but invalid length returns False.
        """
        self.assertFalse(credit_card_validator("37664007783269"))  

    def test22(self):
            """
            Verifies if Amex cards with valid prefix (34) and check bits but invalid length returns False.
            """
            self.assertFalse(credit_card_validator("34201337420664718"))  


    def test23(self):
            """
            Verifies if Amex Cards with valid prefix (37), valid length and valid check bits passes .
            """
            self.assertTrue(credit_card_validator("372013374206913"))  
        
    def test24(self):
        """
        Verifies if Amex Cards with valid prefix (34) valid length and valid check bits passes .
        """
        self.assertTrue(credit_card_validator("342013374206696"))  

    def test25(self):
        """
        Verifies if Amex Cards with valid prefix (34) valid length but invalid check bits return False .
        """
        self.assertFalse(credit_card_validator("342013374206698"))  

    def test26(self):
        """
        Verifies if Amex Cards with valid prefix (37) valid length but invalid check bits return False .
        """
        self.assertFalse(credit_card_validator("372013374206698"))  
            
    def test27(self):
        """
        Verifies if AMEX Cards with valid length but invalid check bits and invalid prefix return False.
        """
        self.assertFalse(credit_card_validator("000000000000037"))  
    
    def test28(self):
        """
        Verifies if AMEX Cards with valid length and valid check bits but invalid prefix return False.
        """
        self.assertFalse(credit_card_validator("000000000000034"))  
    
    #### END AMEX ####


    def test29(self):
        """
        Verifies that an empty string should returns False.
        """
        self.assertFalse(credit_card_validator("")) 

    def test30(self):
        """
        Verifies if Visa Cards with valid prefix, valid length, and valid check bit but is not in the format of a string will pass.
        To see if
        """
        self.assertTrue(credit_card_validator("1234567893456789")) 


    def test31(self):
        """
        Check to see if the following numbers are Luhn valid. Should pass since the provided number is Luhn valid
        Using the provided Luhn Number Checker to generated so valid Lunh numbers.
        If it fails then it means something is wrong with the Luhn algorithm
        """
        self.assertTrue(credit_card_validator("4516400526736591")) 


    def test32(self):
        """
        Check to see if leading zero will be counted
        """
        self.assertTrue(credit_card_validator("000000000004516400526736591")) 


        
if __name__ == '__main__':
    unittest.main()


    
    

