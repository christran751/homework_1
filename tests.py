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
        self.assertTrue(credit_card_validator("347145486005346")) 


    def test5(self):
        """
        Verifies if Amex with valid prefix (37), length, and valid Luhn will pass.
        """
        self.assertTrue(credit_card_validator("374564527987344")) 
    
    def test6(self):
        """
        Verifies if Visa with valid prefix and correct Luhn but a length too short.
        """
        self.assertFalse(credit_card_validator("423456278930")) 

    def test7(self):
        """
        Verifies if Visa with valid prefix and correct Luhn but a length too long.

        """
        self.assertFalse(credit_card_validator("400042078935125489282528")) 

    def test8(self):
        """
        Verifies if Visa with valid prefix and incorrect Luhn but a invalid length that is not equal to 16.

        """
        self.assertFalse(credit_card_validator("4000420555213448123122313216")) 

    # So for VISA, it seems like the mistake here is that they only consider 2 check to be valid i.e., if prefix and length and/or Luhn pass then it's
    # a valid VISA; and the length cannot be equal to 16 (which is incorrect)

    def test9(self):
        """
        Verifies if card that does not match any prefix, but with a correct Luhn, and a correct length that matches the requirment of a VISA and/or Mastercard return False.

        """
        self.assertFalse(credit_card_validator("5000420555213445")) 
    

    def test10(self):
        """
        Verifies if card that does not match any known prefix, but with a correct Luhn, and a correct length that matches the requirment of a AMEX return False.

        """
        self.assertFalse(credit_card_validator("123456789101116")) 

    def test11(self):
        """
        Verifies if Master Card with valid prefix (2221 through 2720) and a correct Luhn but an incorrect length  return False.

        """
        self.assertFalse(credit_card_validator("223456789101115")) 
    
    def test12(self):
        """
        Verifies if Master Card with valid prefix (2221 through 2720) and a correct length but an incorrect Luhn  return False.

        """
        self.assertFalse(credit_card_validator("2234567891011153")) 

    def test13(self):
        """
        Verifies if Master Card with valid prefix (51 through 55) and a correct length but an incorrect Luhn return False.

        """
        self.assertFalse(credit_card_validator("5566742475740355")) 

    def test14(self):
        """
        Verifies if Master Card with valid prefix (51 through 55) and a correct Luhn but an incorrect length return False.

        """
        self.assertFalse(credit_card_validator("55714548600500689")) 
    
    def test15(self):
        """
        Verifies that an empty stirng should return False
        """
        self.assertFalse(credit_card_validator(""))

    def test16(self):
        """
        Verifies that an empty stirng should return False
        """
        self.assertFalse(credit_card_validator(""))
    
    def test17(self):
        """
        Verifies that Amex with correct prefix (34) and correct length but incorrect Luhn will return False
        """
        self.assertFalse(credit_card_validator("346443146464443"))

    
    def test18(self):
        """
        Verifies that Amex with correct prefix (37) and correct length but incorrect Luhn will return False
        """
        self.assertFalse(credit_card_validator("379514596464234"))

    def test19(self):
        """
        Because a valid Amex number did not pass as True, and
        Verifies that a card with an incorrect prefix and an incorrect length and but correct Luhn will return False
        """
        self.assertFalse(credit_card_validator("1230"))


