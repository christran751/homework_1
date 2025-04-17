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
        Verifies if Master Card with valid lower bound prefix (2221), 
        length (16), and a valid Luhn will pass.
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
        Verifies that a Visa Card with a valid prefix (4) with a
        valid length (16), but an invalid Luhn checksum returns False.
        """
        self.assertFalse(credit_card_validator("3012837397919712"))  
        # return false. therefore, length is the issue here

    # My guess is that prefix matters. can't be anything else, maybe had length != 16 for VISA
    # further testing . . . 

    def test14(self):
        """
        Verifies if Visa with valid prefix (4) and valid Luhn checksum
        but a length that is too short (14 instead of 16) return False.
        """
        self.assertFalse(credit_card_validator("40373895098534")) 
        # returns true
    
    def test15(self):
        """
        Verifies if Visa with valid prefix (4) but an invalid Luhn checksum
        and an invalid length (14) return False.
        """
        self.assertFalse(credit_card_validator("40373895098535")) 

    
    # So any length that's not =16 works


    ##############################


    # def test8(self):
    #     """
    #     Verifies if Master Card with invalid prefix just one below the Master Card prefix 51 but valid length and Luhn check sum return False
    #     Testing for any boundry issue.
    #     """
    #     self.assertFalse(credit_card_validator("5030194965135217"))   # return False, it does what it should do


    # def test3_12121(self):
    #     """
    #     Verifies if Master Card with invalid prefix just below the Master Card prefix 51, a invalid length and an invalid Luhn check sum return False
    #     Check to see if an invalid everything will result in a False. 
    #     """
    #     self.assertFalse(credit_card_validator("50301949651352171"))  # return False, so benchmark pass
    

    # def test3_121122(self):
    #     """
    #     Verifies if Master Card with invalid prefix below the Master Card prefix 51 and a invalid length (just one short), but a valid Luhn check sum return False
    #     """
    #     self.assertFalse(credit_card_validator("503019496513526"))  # returns true 


    # def test123123212312312(self):
    #     """
    #     Verifies if Master Card with valid prefix,  a invalid length (just one short), but a valid Luhn check sum return False
    #     """
    #     self.assertFalse(credit_card_validator("514442220003696"))  # return true, but changing the length to be exactly 16 messes it up

    #     # so has to do something with length, so all 3 has to pass for masters?

    # def test3_4(self):
    #     """
    #     Verifies if Master Card with invalid prefix just above Master Card (prefix 55) but valid length and Luhn check sum return False
    #     """
    #     self.assertFalse(credit_card_validator("5663258628437387"))   

    # def test3_5(self):
    #     """
    #     Verifies if Master Card with invalid prefix just below Master Card (2221) but valid length and Luhn check sum return False
    #     """
    #     self.assertFalse(credit_card_validator("2220198583203353"))    

    # def test3_6(self):
    #     """
    #     Verifies if Master Card with invalid prefix just above Master Card (2720) but valid length and Luhn check sum return False
    #     """
    #     self.assertFalse(credit_card_validator("2721803172119548")) 


    # def testMaster1(self):
    #     """
    #     Verifies if Master Card with valid prefix and valid Luhn but length just below 16 returns False
    #     """           
    #     self.assertFalse(credit_card_validator("222100000012344")) # 15


    # def testMaster2(self):
    #     """
    #     Verifies if Master Card with valid prefix and invalid Luhn but valid length check sum return False
    #     """           
    #     self.assertFalse(credit_card_validator("2221000000123447")) # 16

    # def mastertest12delete(self):
    #     """
    #     Master Card with only correct prefix
    #     """
    #     self.assertFalse(credit_card_validator("222100012354523")) # 16

    # def test3_7(self):
    #     """
    #     Verifies if Master Card with valid lower bound prefix (51) and valid Luhn but a length one short will return False.
    #     """
    #     self.assertFalse(credit_card_validator("518951364920016")) # 15 characters

    # def test3_8(self):
    #     """
    #     Verifies if Master Card with valid lower bound prefix (2221) and valid Luhn but a length one short will return False.
    #     """
    #     self.assertFalse(credit_card_validator("222100089282529")) # 15 characters

    # def test3_9(self):
    #     """
    #     Verifies if Master Card with valid upper bound prefix (55) and valid Luhn but a length one too long will return False.
    #     """
    #     self.assertFalse(credit_card_validator("55123456789101375")) # 17 characters

    # def test3_10(self):
    #     """
    #     Verifies if Master Card with valid lower bound prefix (2720) and valid Luhn but a length one too long will return False.
    #     """
    #     self.assertFalse(credit_card_validator("27200007145486698")) # 17 characters




 
    





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

  

    

    # def test11(self):
    #     """
    #     Verifies that a MasterCard with a valid prefix (51 - 55) 
    #     and a valid length, but invalid Luhn checksum
    #     returns False.
    #     """
    #     self.assertFalse(credit_card_validator("5555555566622393")) 


    # def test13(self):
    #     """
    #     Verifies if Master Card with valid prefix (51 through 55) and a valid Luhn but a length to long return False.

    #     """
    #     self.assertFalse(credit_card_validator("55714548600500689")) # 55714548600500689 return True 
    
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
    
    # def test999(self):
    #     """
    #     Verifies that a MasterCard with an invalid prefix (50), ssasaasaasaawill return False.
    #     """
    #     self.assertFalse(credit_card_validator("5000000000000000"))

    # def test9919(self):
    #     """
    #     Verifies that a MasterCard with an invalid prefix (2721) but valid length (16) but invalid check sum will return False.
    #     """
    #     self.assertFalse(credit_card_validator("2721000000000000"))

    # def test99191(self):
    #     """
    #     Verifies that a MasterCard with a valid prefix (51), valid length, but invalid Luhn checksum will return False.
    #     """
    #     self.assertFalse(credit_card_validator("5179426243951311"))

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


    
    

