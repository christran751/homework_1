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
        Verifies if Master Card with invalid prefix just below Master Card (prefix 51) but valid length and Luhn check sum return False
        """
        self.assertFalse(credit_card_validator("5030194965135217"))  

    def test3_4(self):
        """
        Verifies if Master Card with invalid prefix just above Master Card (prefix 55) but valid length and Luhn check sum return False
        """
        self.assertFalse(credit_card_validator("5663258628437387"))   

    def test3_5(self):
        """
        Verifies if Master Card with invalid prefix just below Master Card (2221) but valid length and Luhn check sum return False
        """
        self.assertFalse(credit_card_validator("2220198583203353"))    

    def test3_6(self):
        """
        Verifies if Master Card with invalid prefix just above Master Card (2720) but valid length and Luhn check sum return False
        """
        self.assertFalse(credit_card_validator("2721803172119548"))     
    
    def test3_7(self):
        """
        Verifies if Master Card with valid lower bound prefix (51) and valid Luhn but a length one short will return False.
        """
        self.assertFalse(credit_card_validator("518951364920016")) # 15 characters

    def test3_8(self):
        """
        Verifies if Master Card with valid lower bound prefix (2221) and valid Luhn but a length one short will return False.
        """
        self.assertFalse(credit_card_validator("222100089282529")) # 15 characters

    def test3_9(self):
        """
        Verifies if Master Card with valid upper bound prefix (55) and valid Luhn but a length too long will return False.
        """
        self.assertFalse(credit_card_validator("55123456789101375")) # 17 characters

    def test3_10(self):
        """
        Verifies if Master Card with valid lower bound prefix (2720) and valid Luhn but a length too long will return False.
        """
        self.assertFalse(credit_card_validator("27200007145486698")) # 17 characters


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
        self.assertFalse(credit_card_validator("403738950985711")) # 15 characters

    def test7(self):
        """
        Verifies if Visa with valid prefix and valid Luhn but a length too long will return False.

        """
        self.assertFalse(credit_card_validator("40004207893512544")) # 17 characters


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
        Verifies if an Amex card that has an invalid prefix that is just below the range by 1 (of 34), but a valid Luhn, and a valid length will return False.
        """
        self.assertFalse(credit_card_validator("330000985354256"))  
        # Should return False since it's outside the valid Amex prefix range (33 is invalid)

    def test9_1(self):
        """
        Verifies if an Amex card that has an invalid prefix that is just above the range by 1 (of 34), but a valid Luhn, and a valid length will return False.
        """
        self.assertFalse(credit_card_validator("356969696913371")) 

    def test9_1(self):
        """
        Verifies if an Amex card that has an invalid prefix that is just below the range by 1 (of 37), but a valid Luhn, and a valid length will return False.
        """
        self.assertFalse(credit_card_validator("363694201337699"))

    def test9_1_1(self):
        """
        Verifies if an Amex card that has an invalid prefix that is just above the range by 1 (of 37), an valid Luhn, and a valid length one above will return False.
        """
        self.assertFalse(credit_card_validator("363694261436829")) 

    def test9_2(self):
        """
        Verifies if an Amex card that has an invalid prefix that is just above the range by 1 (of 37), but a valid Luhn, and a valid length will return False.
        """
        self.assertFalse(credit_card_validator("330744106849387")) #384869385466366

    def test21321(self):
        self.assertFalse(credit_card_validator("363694201337699"))

 


        
  
    def test10_1(self):
        """
        Verifies that a Visa Card with a prefix just below VISA (3) with a
        valid length and Luhn checksum, returns False.
        """
        self.assertFalse(credit_card_validator("3012837397919460"))    


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
        Verifies that Amex with invalid prefix below the range (1 less than 37) but a valid Luhn and a valid length will return False
        """
        self.assertFalse(credit_card_validator("387145486001536"))
    
    def test16(self):
        """
        Verifies that Amex with valid prefix (37) and valid Luhn but length that is exactly one more the threshhold return False
        """
        self.assertFalse(credit_card_validator("3778924562000260"))   # 16

    def test17(self):
        """
        Verifies that Amex with valid prefix (34) and valid Luhn but a length that is exactly one more the threshhold return False
        """
        self.assertFalse(credit_card_validator("3400009853542562"))  # 16
    
    
    ## Testing out of bound
    # VISA 3, 5 

    def testxxx(self):
        """
        Verifies that Amex with valid prefix (34) and valid Luhn but length that is exactly one less then threshhold return False
        """
        self.assertFalse(credit_card_validator("34943823951273")) # 14 digits

    def testxxx1(self):
        """
        Verifies that Amex with valid prefix (34) and valid Luhn but length that is exactly one more then threshhold return False
        """
        self.assertFalse(credit_card_validator("3440591059699025")) # 16 digits

    def testxxx2(self):
        """
        Verifies that Amex with valid prefix (37) and valid Luhn but length that is exactly one more then threshhold return False
        """
        self.assertFalse(credit_card_validator("3700000069420690")) # 16 digits

    def testxxx3(self):
        """
        Verifies that Amex with valid prefix (34) and length but an invalid Luhn return False
        """
        self.assertFalse(credit_card_validator("3400009853425672")) # 16 digits

    def testxxx4(self):
        """
        Verifies that Amex with valid prefix (34) but an invalid length and invalid Luhn return False
        """
        self.assertFalse(credit_card_validator("34000098535425")) # 14 digits
    
    def test999(self):
        """
        Verifies that a MasterCard with an invalid prefix (50) will return False.
        """
        self.assertFalse(credit_card_validator("5000000000000000"))

    def test9919(self):
        """
        Verifies that a MasterCard with an invalid prefix (2721) will return False.
        """
        self.assertFalse(credit_card_validator("2721000000000000"))

    def test99191(self):
        """
        Verifies that a MasterCard with a valid prefix (51), valid length, but invalid Luhn checksum will return False.
        """
        self.assertFalse(credit_card_validator("5179426243951311"))

    def test991912(self):
        """
        Verifies that an Amex card with a valid prefix (37) and length, but invalid Luhn checksum, will return False.
        """
        self.assertFalse(credit_card_validator("374564527987341"))  

    def test21132131(self):
        """
        Check to see if length too long.
        """
        self.assertFalse(credit_card_validator("4234567890123456789"))
    
    


        
if __name__ == '__main__':
    unittest.main()


    
    

