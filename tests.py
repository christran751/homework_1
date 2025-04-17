import unittest
from credit_card_validator import credit_card_validator

class CreditCardValidatorTest(unittest.TestCase):

    def test1(self):
        """
        Verifies if a Visa card with valid prefix (4), valid length (16), and 
        a valid Luhn checksum will pass.
        """
        self.assertTrue(credit_card_validator("4234562789345674"))   
    
    def test2(self):
        """
        Verifies if Master Card with valid lower bound prefix (51), valid
        length (16), and a valid Luhn checksum will pass.
        """
        self.assertTrue(credit_card_validator("5179426243951317"))

    def test3(self):
        """
        Verifies if Master Card with valid upper bound prefix (55), a valid
        length (16), and a valid Luhn will pass.
        """
        self.assertTrue(credit_card_validator("5533130321072175"))

    def test4(self):
        """
        Verifies if a MasterCard with the valid lower bound prefix (2221),
        correct length (16), and a valid Luhn checksum passes validation.
        """
        self.assertTrue(credit_card_validator("2221000133742063"))

    def test5(self):
        """
        Verifies if Master Card with valid upper bound prefix (2720), 
        length (16), and valid Luhn will pass.
        """
        self.assertTrue(credit_card_validator("2720892825213379"))


    def test6(self):
        """
        Verifies if Amex with valid prefix (37), 
        length (15), and valid Luhn checksum will pass.
        """
        self.assertTrue(credit_card_validator("374564527987344")) 
    
    def test7(self):
        """
        Verifies if Amex with valid prefix (34), 
        length (15), and valid Luhn will pass.
        """
        self.assertTrue(credit_card_validator("347145486005346"))
    
    def test8(self):
        """
        Verifies if Visa with valid prefix (4) and valid Luhn checksum 
        but an invalid length just short by one (15) 
        will return False.
        """
        self.assertFalse(credit_card_validator("403738950985711")) 
        # return True so length of 15 pass

    def test9(self):
        """
        Verifies if Visa with valid prefix (4) and valid Luhn checksum but an invalid length 
        (one more than 16 digits) will return False.
        """
        self.assertFalse(credit_card_validator("40004207893512544")) 
        # return True so a length of 17 also pass

    def test10(self):
        """
        Verifies that a Visa Card with a prefix just below VISA (3) with a
        valid length (16) and Luhn checksum, returns False.
        """
        self.assertFalse(credit_card_validator("3012837397919460"))  
        # return False as intended
    
    def test11(self):
        """
        Verifies that a VISA Card with a prefix just above VISA (5) with a
        valid length (16) and Luhn checksum, returns False.
        """
        self.assertFalse(credit_card_validator("5000001234567896")) 

    def test12(self):
        """
        Verifies that a Visa Card with a prefix just below VISA (3) with a
        valid Luhn checksum, but an invalid length (14) returns False.
        """
        self.assertFalse(credit_card_validator("30128373979197"))
        # False as intended

    def test13(self):
        """
        Verifies that a Visa Card with a prefix just below VISA (3) with a
        valid length (16),but an invalid Luhn checksum returns False.
        """
        self.assertFalse(credit_card_validator("3012837397919723"))
       
    def test14(self):
        """
        Verifies that a Visa Card with a valid prefix (4) with a
        valid length (16), but an invalid Luhn checksum returns False.
        """
        self.assertFalse(credit_card_validator("3012837397919712"))  
        # return false. therefore, length is the issue here

    # My guess is that prefix matters. can't be anything else, maybe had length != 16 for VISA
    # further testing . . . 

    def test15(self):
        """
        Verifies if Visa with valid prefix (4) and valid Luhn checksum
        but a length that is too short (14 instead of 16) return False.
        """
        self.assertFalse(credit_card_validator("40373895098534")) 
        # returns true
    
    def test16(self):
        """
        Verifies if Visa with valid prefix (4) but an invalid Luhn checksum
        and an invalid length (14) return False.
        """
        self.assertFalse(credit_card_validator("40373895098535")) 

    def test17(self):
        """
        Verifies if Visa with invalid prefix (3), invalid Luhn checksum, and 
        an invalid length (14) return False.
        """
        self.assertFalse(credit_card_validator("30002136979263")) 

# Master
    def test18(self):
        """
        Verifies if Master Card with invalid prefix (50) 
        but valid length (16) and Luhn check sum return False
        Testing for any boundry issue.
        """
        self.assertFalse(credit_card_validator("5030194965135217"))   

    def test19(self):
        """
        Verifies if Master Card with invalid prefix (50), with an 
        invalid length (17) and an invalid Luhn check sum return False
        """
        self.assertFalse(credit_card_validator("50301949651352171"))  
    
    def test20(self):
        """
        Verifies if Master Card with invalid prefix (50) and a invalid 
        length(15), but a valid Luhn check sum return False
        """
        self.assertFalse(credit_card_validator("503019496513526")) 

    def test21(self):
        """
        Verifies if Master Card with valid prefix (51), and a valid 
        Luhn checksum, but an invalid length (15), return False
        """
        self.assertFalse(credit_card_validator("514442220003696"))  
        # return true, but changing the length to be exactly 16 messes it up
        # so has to do something with length, so all 3 has to pass for masters?

    def test22(self):
        """
        Verifies if Master Card with invalid prefix just above 
        Master Card (56) but a valid 
        length (16) and Luhn check sum return False
        """
        self.assertFalse(credit_card_validator("5663258628437387"))   

    def test23(self):
        """
        Verifies if Master Card with invalid 
        prefix(2220), but a valid length(16) 
        and Luhn check sum return False
        """
        self.assertFalse(credit_card_validator("2220198583203353"))    

    def test24(self):
        """
        Verifies if Master Card with invalid 
        prefix(2721), but a valid length(16) 
        and Luhn check sum return False
        """
        self.assertFalse(credit_card_validator("2721803172119548")) 

    def test25(self):
        """
        Verifies if Master Card with valid 
        prefix(2221) and valid Luhn but 
        invalid length(15) returns False
        """           
        self.assertFalse(credit_card_validator("222100000012344"))

    def test26(self):
        """
        Verifies if Master Card with valid 
        prefix(2221) and length(16), but an invalid 
        Luhn checksum return False
        """           
        self.assertFalse(credit_card_validator("2221000000123447")) 
    
    def test27(self):
        """
        Master Card with only correct prefix(2221) and
        invalid length(15) and Luhn checksum
        return False
        """
        self.assertFalse(credit_card_validator("222100012354523")) 

    def test28(self):
        """
        Verifies if Master Card with valid prefix(51) and 
        valid Luhn checksum but an invalid 
        length(15) will return False.
        """
        self.assertFalse(credit_card_validator("518951364920016"))

    def test29(self):
        """
        Verifies if Master Card with valid lower bound prefix (2221) and valid 
        Luhn, but a length (15) one short will return False.
        """
        self.assertFalse(credit_card_validator("222100089282529"))

    def test30(self):
        """
        Verifies if Master Card with valid upper bound prefix (55) and valid 
        Luhn but an invalid length (17) will return False.
        """
        self.assertFalse(credit_card_validator("55123456789101375"))

    def test31(self):
        """
        Verifies if Master Card with valid lower bound prefix (2720) and valid Luhn 
        but an invalid length (17) return False.
        """
        self.assertFalse(credit_card_validator("27200007145486698")) 


    def test32(self):
        """
        Verifies that a MasterCard with a invalid prefix (56) 
        and an invalid length (17), but valid Luhn checksum
        returns False.
        """
        self.assertFalse(credit_card_validator("56123456789133574")) 

    def test33(self):
        """
        Verifies that a MasterCard with an invalid prefix (56), 
        and Luhn checksum, but a valid length (16)
        return False.
        """
        self.assertFalse(credit_card_validator("5612313124340009"))

    def test34(self):
        """
        Verifies that a MasterCard with an invalid prefix (2721) and invalid Luhn checksum
        but a valid length (16) will return False.
        """
        self.assertFalse(credit_card_validator("2721000000000000"))

    def test35(self):
        """
        Verifies that a MasterCard with a valid prefix (51), and a valid length (16), 
        but an invalid Luhn checksum will return False.
        """
        self.assertFalse(credit_card_validator("5179426243951311"))

    def test36(self):
        """
        Verifies that a MasterCard with a invalid prefix that is 
        one above the upper bound (2721), with an invalid length (17), but a valid Luhn checksum
        will return False.

        Check to see if the upper bound of the new range (2221 - 2270) will differ from the upperbound of the old range (51 - 55)
        """
        self.assertFalse(credit_card_validator("272112332113245010"))  # 27211233211324509
    
    
    # def test8(self):
    #     """
    #     Verifies if an Amex card that has an invalid prefix that is just below the range by 1 (of 34), but a valid Luhn, and a valid length will return False.
    #     """
    #     self.assertFalse(credit_card_validator("330000985354256"))  
    #     # Should return False since it's outside the valid Amex prefix range (33 is invalid)

    # def test9_1(self):
    #     """
    #     Verifies if an Amex card that has an invalid prefix that is just above the range by 1 (of 34), but a valid Luhn, and a valid length will return False.
    #     """
    #     self.assertFalse(credit_card_validator("356969696913371")) 

    # def test9_1(self):
    #     """
    #     Verifies if an Amex card that has an invalid prefix that is just below the range by 1 (of 37), but a valid Luhn, and a valid length will return False.
    #     """
    #     self.assertFalse(credit_card_validator("363694201337699"))

    # def test9_1_1(self):
    #     """
    #     Verifies if an Amex card that has an invalid prefix that is just above the range by 1 (of 37), an valid Luhn, and a valid length one above will return False.
    #     """
    #     self.assertFalse(credit_card_validator("363694261436829")) 

    # def test9_2(self):
    #     """
    #     Verifies if an Amex card that has an invalid prefix that is just above the range by 1 (of 37), but a valid Luhn, and a valid length will return False.
    #     """
    #     self.assertFalse(credit_card_validator("330744106849387")) #384869385466366

    # def test21321(self):
    #     self.assertFalse(credit_card_validator("363694201337699"))

  

    

   
    
    # def test14(self):
    #     """
    #     Verifies that an empty stirng should return False
    #     """
    #     self.assertFalse(credit_card_validator(""))

    # def test15(self):
    #     """
    #     Verifies that Amex with invalid prefix below the range (1 less than 37) but a valid Luhn and a valid length will return False
    #     """
    #     self.assertFalse(credit_card_validator("387145486001536"))
    
    # def test16(self):
    #     """
    #     Verifies that Amex with valid prefix (37) and valid Luhn but length that is exactly one more the threshhold return False
    #     """
    #     self.assertFalse(credit_card_validator("3778924562000260"))   # 16

    # def test17(self):
    #     """
    #     Verifies that Amex with valid prefix (34) and valid Luhn but a length that is exactly one more the threshhold return False
    #     """
    #     self.assertFalse(credit_card_validator("3400009853542562"))  # 16
    
    
    # def testxxx(self):
    #     """
    #     Verifies that Amex with valid prefix (34) and valid Luhn but length that is exactly one less then threshhold return False
    #     """
    #     self.assertFalse(credit_card_validator("34943823951273")) # 14 digits

    # def testxxx1(self):
    #     """
    #     Verifies that Amex with valid prefix (34) and valid Luhn but length that is exactly one more then threshhold return False
    #     """
    #     self.assertFalse(credit_card_validator("3440591059699025")) # 16 digits

    # def testxxx2(self):
    #     """
    #     Verifies that Amex with valid prefix (37) and valid Luhn but length that is exactly one more then threshhold return False
    #     """
    #     self.assertFalse(credit_card_validator("3700000069420690")) # 16 digits

    # def testxxx3(self):
    #     """
    #     Verifies that Amex with valid prefix (34) and length but an invalid Luhn return False
    #     """
    #     self.assertFalse(credit_card_validator("3400009853425672")) # 16 digits

    # def testxxx4(self):
    #     """
    #     Verifies that Amex with valid prefix (34) but an invalid length and invalid Luhn return False
    #     """
    #     self.assertFalse(credit_card_validator("34000098535425")) # 14 digits
    


    # def test991912(self):
    #     """
    #     Verifies that an Amex card with a valid prefix (37) and length, but invalid Luhn checksum, will return False.
    #     """
    #     self.assertFalse(credit_card_validator("374564527987341"))  

    # def test21132131(self):
    #     """
    #     Check to see if length too long.
    #     """
    #     self.assertFalse(credit_card_validator("4234567890123456789"))
    
    


        
if __name__ == '__main__':
    unittest.main()


    
    

