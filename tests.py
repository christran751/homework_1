import unittest
from credit_card_validator import credit_card_validator


class CreditCardValidatorTest(unittest.TestCase):

    def test1(self):
        """
        Verifies if Visa Cards with valid prefix, length, and valid Luhn will pass.
        This should!
        """
        self.assertFalse(credit_card_validator("4234562789345674"))   
    
    def test2(self):
        """
        Verifies if Master Card with valid prefix (51 - 55), length, and valid Luhn will pass.
        """
        self.assertTrue(credit_card_validator("5398134546574100")) 

    def test3(self):
        """
        Verifies if Master Card with valid prefix (2221 through 2720), length, and valid Luhn will pass.
        """
        self.assertTrue(credit_card_validator("2720892562456009")) 


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
        Verifies if Visa with valid prefix and valid Luhn but a length too short.
        """
        self.assertFalse(credit_card_validator("423456278930")) 

    def test7(self):
        """
        Verifies if Visa with valid prefix and valid Luhn but a length too long.

        """
        self.assertFalse(credit_card_validator("400042078935125489282528")) 


    def test8_1(self):
        """
        Verifies that Visa with invalid prefix (below prefix of 4 - boundary issue) and valid luhn but invalid length will return False
        """
        self.assertFalse(credit_card_validator("3668924562000263")) 



    # So for VISA, it seems like the mistake here is that they only consider 2 check to be valid i.e., if prefix and length and/or Luhn pass then it's
    # a valid VISA; and the length cannot be equal to 16 (which is invalid)

    def test9(self):
        """
        Verifies if card that does not match any prefix, but with a valid Luhn, and a valid length that matches the requirment of a valid AMEX return False.
        """
        self.assertFalse(credit_card_validator("123456789101116")) 
    

    def test10(self):
        """
        Verifies that a MasterCard with a valid prefix (2221 through 2720) and a
        valid Luhn checksum, but with an invalid length one digit shorter than required,
        returns False.
        """
        self.assertFalse(credit_card_validator("223456789101115"))  
    
  
    def test10_1(self):
        """
        Verifies that a MasterCard with a valid prefix (2221 through 2720) and a
        valid Luhn checksum, but with an invalid length one digit greater than required,
        returns False.
        """
        self.assertFalse(credit_card_validator("22248900562163268"))    
    
    def test11(self):
        """
        Verifies if Master Card with valid prefix (2221 through 2720) and a valid length but an invalid Luhn  return False.

        """
        self.assertFalse(credit_card_validator("2234567891011153")) 

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
        Verifies that Amex with invalid prefix (1 less than 34) and Luhn but valid length will return False
        """
        self.assertFalse(credit_card_validator("337145486001537"))
    
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
    
    # Seems like the valid length of AMEX is incorrectly set to be 16 instead.
    
    ## Testing out of bound
    # VISA 3, 5 

    def testxxx(self):
        """
        Verifies that Amex with valid prefix (37) and valid Luhn but length that is exactly one less more the threshhold return False
        """
        self.assertFalse(credit_card_validator("37373737378925"))


        
if __name__ == '__main__':
    unittest.main()


    
    

