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
        self.assertFalse(credit_card_validator("411111111111690"))  

    def test5(self):
        """
        Verifies if Amex cards with valid prefix and length but invalid check bits returns False.
        """
        self.assertFalse(credit_card_validator("341111111111169"))  
    
    def test6(self):
        """
        Verifies if Amex cards with valid prefix and check bits but invalid length returns False.
        """
        self.assertFalse(credit_card_validator("341111111111690"))  

    def test7(self):
        """
        Verifies if Master Cards with valid lengths and valid prefix (2221-2720) but an invalid check bits returns False .
        """
        self.assertFalse(credit_card_validator("2221691051051100"))  
    
        
    def test8(self):
        """
        Verifies if Master Cards with valid prefix (2221-2720) and check bits but invalid length returns False .
        """
        self.assertFalse(credit_card_validator("222169105105110"))  

    
if __name__ == '__main__':
    unittest.main()


    
    

import unittest
from credit_card_module import credit_card_validator  # Replace with your actual module name

class CreditCardValidatorTest(unittest.TestCase):

    # ---------- VISA ----------
    def test_valid_visa_with_69(self):
        """Valid Visa with '69', correct length and prefix, passes Luhn"""
        self.assertTrue(credit_card_validator("4691 1111 1111 1111"))

    def test_invalid_visa_prefix_with_69(self):
        """Invalid Visa: wrong prefix but valid length and Luhn, contains '69'"""
        self.assertFalse(credit_card_validator("5691 1111 1111 1111"))

    def test_invalid_visa_length_with_69(self):
        """Invalid Visa: correct prefix and Luhn, but wrong length, contains '69'"""
        self.assertFalse(credit_card_validator(""))

    def test_invalid_visa_luhn_with_69(self):
        """Invalid Visa: correct prefix and length, bad Luhn, contains '69'"""
        self.assertFalse(credit_card_validator("4691 1111 1111 1169"))

    # ---------- MASTERCARD ----------
    def test_valid_mastercard_prefix_51_with_69(self):
        """Valid MasterCard (prefix 51), valid length, valid Luhn, contains '69'"""
        self.assertTrue(credit_card_validator("5169 0510 1051 0510"))

    def test_valid_mastercard_prefix_2221_with_69(self):
        """Valid MasterCard (prefix 2221), valid length and Luhn, contains '69'"""
        self.assertTrue(credit_card_validator("2221 6900 0000 0009"))

    def test_invalid_mastercard_length_with_69(self):
        """Invalid MasterCard: correct prefix and Luhn, but wrong length, contains '69'"""
        self.assertFalse(credit_card_validator("5169 0510 1051 051"))

    def test_invalid_mastercard_luhn_with_69(self):
        """Invalid MasterCard: correct prefix and length, bad Luhn, contains '69'"""
        self.assertFalse(credit_card_validator("5169 0510 1051 0511"))

    # ---------- AMEX ----------
    def test_valid_amex_37_with_69(self):
        """Valid Amex (prefix 37), correct length, valid Luhn, contains '69'"""
        self.assertTrue(credit_card_validator("3769 822463 10005"))

    def test_invalid_amex_prefix_with_69(self):
        """Invalid Amex: wrong prefix, valid length and Luhn, contains '69'"""
        self.assertFalse(credit_card_validator("3669 822463 10005"))

    def test_invalid_amex_length_with_69(self):4691 1111 1111 111
        """Invalid Amex: correct prefix and Luhn, wrong length, contains '69'"""
        self.assertFalse(credit_card_validator("3769 822463 100056"))

    def test_invalid_amex_luhn_with_69(self):
        """Invalid Amex: correct prefix and length, bad Luhn, contains '69'"""
        self.assertFalse(credit_card_validator("3769 822463 10006"))

if __name__ == '__main__':
    unittest.main()
