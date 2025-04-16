import unittest
from credit_card_validator import credit_card_validator


class CreditCardValidatorTest(unittest.TestCase):

    def test1(self):
        """
        Verifies if Visa Cards with valid prefix, length, and valid Luhn will pass.
        This should!
        """
        self.assertTrue(credit_card_validator("4234562789345674"))   
    

    def test2(self):
        """
        Verifies if Master Card with valid lower bound prefix (51), length, and valid Luhn will pass.
        """
        self.assertTrue(credit_card_validator("5179426243951317"))

    def test2_1(self):
        """
        Verifies if Master Card with valid upper bound prefix (55), length, and valid Luhn will pass.
        """
        self.assertTrue(credit_card_validator("5533130321072175"))

    def test3(self):
        """
        Verifies if Master Card with valid lower bound prefix (2221), length, and valid Luhn will pass.
        """
        self.assertTrue(credit_card_validator("2221000133742063")) 

    def test3_2(self):
        """
        Verifies if Master Card with valid upper bound prefix (2720), length, and valid Luhn will pass.
        """
        self.assertTrue(credit_card_validator("2720892825213379")) 

    def test3_3(self):
        """
        Verifies if Master Card with invalid prefix just below Master Card but valid length and Luhn check sum return False
        """
        self.assertFalse(credit_card_validator("5030194965135217"))  

    def test4(self):
        """
        Verifies if Amex with valid prefix (34), length, and valid Luhn will pass.
        """
        self.assertFalse(credit_card_validator("347145486005346")) 


    def test5(self):
        """
        Verifies if Amex with valid prefix (37), length, and valid Luhn will pass.
        """
        self.assertTrue(credit_card_validator("374564527987344")) 
    
    def test6(self):
        """
        Verifies if Visa with valid prefix and valid Luhn but a length too short will return False.
        """
        self.assertFalse(credit_card_validator("423456278930")) 

    def test7(self):
        """
        Verifies if Visa with valid prefix and valid Luhn but a length too long will return False.

        """
        self.assertFalse(credit_card_validator("400042078935125489282528")) 


    def test8_1(self):
        """
        Verifies that Visa with invalid prefix (prefix of 4 - boundary issue) and valid length and but invalid Luhn will return False
        Picked using Category Partition Testing
        """
        self.assertFalse(credit_card_validator("3000021316982466")) 



    # So for VISA, it seems like the mistake here is that they only consider 2 check to be valid i.e., if prefix and length and/or Luhn pass then it's
    # a valid VISA; and the length cannot be equal to 16 (which is invalid)

    def test9(self):
        """
        Verifies if an Amex card that has an invalid prefix, but a valid Luhn, and a valid length will return False.
        """
        self.assertFalse(credit_card_validator("123456789101116")) 
    

    def test10(self):
        """
        Verifies that a MasterCard with a valid prefix (2221 through 2720) and a
        valid Luhn checksum, but with an invalid length one digit shorter than
        required, returns False.
        """
        self.assertFalse(credit_card_validator("223456789101115"))  
    
  
    def test10_1(self):
        """
        Verifies that a Visa Card with a prefix just below VISA (3) with a
        valid length and Luhn checksum, returns False.
        """
        self.assertFalse(credit_card_validator("3012837397919460"))    


    def test11(self):
        """
        Verifies that a MasterCard with a valid prefix (2221 - 2720) 
        and a valid length, but invalid Luhn checksum
        returns False.
        """
        self.assertFalse(credit_card_validator("2234567891011153")) 

    def test11_1(self):
        """
        Verifies that a MasterCard with a valid prefix (51 - 55) 
        and a valid length, but invalid Luhn checksum
        returns False.
        """
        self.assertFalse(credit_card_validator("5555555566622393")) 

    def test12(self):
        """
        Verifies if Master Card with valid prefix (51 through 55) and a valid length but an invalid Luhn return False.

        """
        self.assertFalse(credit_card_validator("5566742475740355")) 

    def test13(self):
        """
        Verifies if Master Card with valid prefix (51 through 55) and a valid Luhn but a length to long return False.

        """
        self.assertFalse(credit_card_validator("55714548600500689")) 
    
    def test14(self):
        """
        Verifies that an empty stirng should return False
        """
        self.assertFalse(credit_card_validator(""))

    def test15(self):
        """
        Verifies that Amex with invalid prefix (1 less than 37) but a valid Luhn and a valid length will return False
        """
        self.assertFalse(credit_card_validator("387145486001536"))
    
    def test16(self):
        """
        Verifies that Amex with valid prefix (37) and valid Luhn but length that is exactly one more the threshhold return False
        """
        self.assertFalse(credit_card_validator("3778924562000260"))   

    def test17(self):
        """
        Verifies that Amex with valid prefix (34) and valid Luhn but a length that is exactly one more the threshhold return False
        """
        self.assertFalse(credit_card_validator("3400009853542562"))  
    
    
    ## Testing out of bound
    # VISA 3, 5 

    def testxxx(self):
        """
        Verifies that Amex with valid prefix (37) and valid Luhn but length that is exactly one less more the threshhold return False
        """
        self.assertFalse(credit_card_validator("37373737378925"))


        
if __name__ == '__main__':
    unittest.main()


    
    

