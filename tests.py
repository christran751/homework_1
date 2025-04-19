import unittest
from credit_card_validator import credit_card_validator


class CreditCardValidatorTest(unittest.TestCase):
    """
    Author: Christopher Tran
    Date: 04/18/2025

    Unit tests for the credit_card_validator function.

    Goal is to construct a series of unit tests to verify that the function
    will correctly accept or reject card numbers based on their prefixes,
    length requirements, and checksum validation.

    Requirments
    -------------
    Visa
        Prefix(es): 4
        Length: 16
    MasterCard
        Prefix(es): 51 through 55 and 2221 through 2720
        Length: 16
    American Express
        Prefix(es): 34 and 37
        Length: 15

    Test Case
    -------------
    - Valid Visa card with correct prefix, length, and Luhn checksum.
    - Valid MasterCard with correct prefix in both 51–55 and 2221–2720
    ranges, length, and Luhn checksum.
    - Valid AMEX card with both 34 and 37 prefixes, length, and Luhn checksum.
    - Edge cases for prefix boundaries (i.e., 50 and 56 and 2221 and 2720 for
    MasterCard, 3 and 5 for Visa, and 33, 35, 36, and 38 for AMEX).
    - Edge cases for length boundaries (i.e., cards that are short or long).
    - Card numbers with incorrect prefix, incorrect length, or invalid Luhn
    checksum.
    - Other edge cases such as NULL or empty inputs.
    """
    def test1(self):
        """
        Verifies if a Visa card with valid prefix (4), valid length (16),
        and a valid Luhn checksum will pass. Picked using Category Partition
        Testing. Was pick to be used as a baseline to verify if the function
        works on known-good data.
        """
        self.assertTrue(credit_card_validator("4234562789345674"))

    def test2(self):
        """
        Verifies if Master Card with valid lower bound prefix (51), valid
        length (16), and a valid Luhn checksum will pass.
        Picked using Category Partition Testing. Was pick to be used as a
        baseline to verify if the function works on known-good data.
        """
        self.assertTrue(credit_card_validator("5179426243951317"))

    def test3(self):
        """
        Verifies if Master Card with valid upper bound prefix (55), a valid
        length (16), and a valid Luhn will pass.
        Picked using Category Partition Testing Method. Was pick to be used as
        a baseline to verify if the function works on known-good data.
        """
        self.assertTrue(credit_card_validator("5533130321072175"))

    def test4(self):
        """
        Verifies if a MasterCard with the valid lower bound prefix (2221),
        correct length (16), and a valid Luhn checksum passes validation.
        Picked using Category Partition Testing Method.
        """
        self.assertTrue(credit_card_validator("2221000133742063"))

    def test5(self):
        """
        Verifies if Master Card with valid upper bound prefix (2720),
        length (16), and valid Luhn will pass.
        Picked using Category Partition Testing Method.
        """
        self.assertTrue(credit_card_validator("2720892825213379"))

    def test6(self):
        """
        Verifies if Amex with valid prefix (37),
        length (15), and valid Luhn checksum will pass.
        Picked using Category Partition Testing Method.
        """
        self.assertTrue(credit_card_validator("374564527987344"))

    def test7(self):
        """
        Verifies if Amex with valid prefix (34),
        length (15), and valid Luhn checksum will pass.
        Picked using the Category Partition Testing.
        """
        self.assertTrue(credit_card_validator("347145486005346"))

    def test8(self):
        """
        Verifies if Visa with valid prefix (4) and valid Luhn checksum
        but an invalid length just short by one (15) will return False.
        Picked using both the Category Partition Testing Method and
        the boundary value testing method.
        """
        self.assertTrue(credit_card_validator("4234567890123456"))

    def test9(self):
        """
        Verifies if Visa with valid prefix (4) and valid Luhn checksum but an
        invalid length that is (17) will return False. Picked using both the
        Category Partition Testing Method and the boundary value testing
        method.
        """
        self.assertFalse(credit_card_validator("40004207893512544"))

    def test10(self):
        """
        Verifies that a Visa Card with an invalid VISA prefix just one below
        (3) but with a valid length (16) and Luhn checksum, returns False.
        Picked using both the Category Partition Testing Method and boundary
        value testing method.
        """
        self.assertFalse(credit_card_validator("3012837397919460"))

    def test11(self):
        """
        Verifies that a VISA Card with an invalid prefix (5) with a
        valid length (16) and Luhn checksum, returns False.
        Picked using Category Partition Testing and boundary
        value testing method.
        """
        self.assertFalse(credit_card_validator("5000001234567896"))

    def test12(self):
        """
        Verifies that a Visa Card with an invalid prefix (3) and an invalid
        length (14), but has a valid Luhn checksum returns False.
        Picked using Category Partition Testing and boundary value testing
        method.
        """
        self.assertFalse(credit_card_validator("30128373979197"))

    def test13(self):
        """
        Verifies that a Visa Card with an invalid prefix just below VISA (3)
        with a an invalid Luhn checksum, but a valid length (16) returns False.
        Picked using Category Partition Testing and boundary value testing
        method.
        """
        self.assertFalse(credit_card_validator("3012837397919723"))

    def test14(self):
        """
        Verifies if Visa with invalid prefix (3), invalid Luhn checksum, and
        an invalid length (14) return False. Picked using both the Category
        Partition Testing Method and the boundary value testing method.
        """
        self.assertFalse(credit_card_validator("30002136979263"))

    def test15(self):
        """
        Verifies that a Visa Card with a valid prefix (4) with a
        valid length (16), but an invalid Luhn checksum returns False.
        Picked using Category Partition Testing and boundary value testing
        method. Used to determine if function will consider it to be a valid
        VISA even if the checksum requirement fails. Should return false.
        """
        self.assertFalse(credit_card_validator("3012837397919712"))

    def test16(self):
        """
        Verifies if Visa with valid prefix (4) and valid Luhn checksum
        but a length that is too short (14 instead of 16) return False.
        Picked using Category Partition Testing and boundary value testing
        method.
        """
        self.assertFalse(credit_card_validator("40373895098534"))

    def test17(self):
        """
        Verifies if Visa with valid prefix (4) but an invalid Luhn checksum
        and an invalid length (14) return False. Picked using both the Category
        Partition Testing Method and the boundary value testing method.
        """
        self.assertFalse(credit_card_validator("40373895098535"))

    def test18(self):
        """
        Verifies if Master Card with invalid prefix (50) just one below
        the requirment, but valid length (16) and Luhn checksum return False.
        Picked using both the Category Partition Testing Method
        and the boundary value testing method.
        """
        self.assertFalse(credit_card_validator("5030194965135217"))

    def test19(self):
        """
        Verifies if Master Card with invalid prefix (50) and a invalid
        length(15), but a valid Luhn check sum return False.
        Picked using both the Category Partition Testing Method
        and the boundary value testing method.
        """
        self.assertFalse(credit_card_validator("503019496513526"))

    def test20(self):
        """
        Verifies if Master Card with invalid prefix (50), an
        invalid length (17), and an invalid Luhn checksum return False.
        Picked using both the Category Partition Testing Method
        and the boundary value testing method.
        """
        self.assertFalse(credit_card_validator("50301949651352171"))

    def test21(self):
        """
        Verifies if Master Card with valid prefix (51) and a valid
        Luhn checksum but an invalid length (15) will return False.
        Picked using both the Category Partition Testing Method,
        the boundary value testing method, and error guessing.
        """
        self.assertFalse(credit_card_validator("518951364920016"))

    def test22(self):
        """
        Verifies that a MasterCard with a valid prefix (51), and a valid
        length (16), but an invalid Luhn checksum will return False.
        Picked using both the Category Partition Testing Method,
        the boundary value testing method, and error guessing.
        """
        self.assertFalse(credit_card_validator("5179426243951311"))

    def test23(self):
        """
        Verifies if Master Card with invalid prefix just above
        Master Card (56) but a valid length (16) and Luhn check sum return
        False. Picked using both the Category Partition Testing Method
        and the boundary value testing method.
        """
        self.assertFalse(credit_card_validator("5663258628437387"))

    def test24(self):
        """
        Verifies that a MasterCard with a invalid prefix (56)
        and an invalid length (17), but valid Luhn checksum
        returns False. Picked using both the Category Partition
        Testing Method and the boundary value testing method.
        """
        self.assertFalse(credit_card_validator("56123456789133574"))

    def test25(self):
        """
        Verifies that a MasterCard with an invalid prefix (56),
        and Luhn checksum, but a valid length (16) return False.
        Picked using both the Category Partition Testing Method
        and the boundary value testing method.
        """
        self.assertFalse(credit_card_validator("5612313124340009"))

    def test26(self):
        """
        Verifies if Master Card with an invalid prefix that
        is just one below the new lower bound (2220),
        but has a valid length (16) and Luhn check sum return False.
        Picked using both the Category Partition Testing Method
        and the boundary value testing method.
        """
        self.assertFalse(credit_card_validator("2220198583203353"))

    def test27(self):
        """
        Verifies if Master Card with invalid prefix (2721), but
        a valid length (16) and Luhn check sum return False.
        Picked using both the Category Partition Testing Method
        and the boundary value testing method.
        """
        self.assertFalse(credit_card_validator("2721803172119548"))

    def test28(self):
        """
        Verifies if Master Card with valid lower bound prefix (2221) and valid
        Luhn, but a length (15) one short will return False.
        Picked using both the Category
        Partition Testing Method and the boundary value testing method.
        """
        self.assertFalse(credit_card_validator("222100000012344"))

    def test29(self):
        """
        Verifies if Master Card with valid lower bound prefix (2221) and valid
        length (16), but an invalid Luhn checksum will return False.
        Picked using both the Category Partition Testing Method
        and the boundary value testing method.
        """
        self.assertFalse(credit_card_validator("2221000000123447"))

    def test30(self):
        """
        Master Card with only a valid  prefix (2221) but an
        invalid length(15) and Luhn checksum return False.
        Picked using both the Category Partition Testing Method
        and the boundary value testing method.
        """
        self.assertFalse(credit_card_validator("222100012354523"))

    def test31(self):
        """
        Verifies if Master Card with valid upper bound prefix (55) and valid
        Luhn but an invalid length (17) will return False.
        Picked using both the Category Partition Testing Method
        and the boundary value testing method.
        """
        self.assertFalse(credit_card_validator("55123456789101375"))

    def test32(self):
        """
        Verifies if Master Card with valid lower bound prefix (2720) and valid
        Luhn but an invalid length (17) return False.
        Picked using both the Category Partition Testing Method
        and the boundary value testing method.
        """
        self.assertFalse(credit_card_validator("27200007145486698"))

    def test33(self):
        """
        Verifies that a MasterCard with an invalid prefix (56),
        and Luhn checksum, but a valid length (16) return False.
        Picked using both the Category Partition Testing Method
        and the boundary value testing method.
        """
        self.assertFalse(credit_card_validator("5612313124340009"))

    def test34(self):
        """
        Verifies that a MasterCard with an invalid prefix (2721) and invalid
        Luhn checksum but a valid length (16) will return False.
        Picked using both the Category Partition Testing Method
        and the boundary value testing method.
        """
        self.assertFalse(credit_card_validator("2721000000000000"))

    def test35(self):
        """
        Verifies that a MasterCard with a invalid prefix that is
        one above the upper bound (2721), with an invalid length (16), but a
        valid Luhn checksum will return False.
        Check to see if the upper bound of the new range (2221 - 2270) will
        differ from the upperbound of the old range (51 - 55)
        2721 with length = 16 will fails
        But 2721 with length = 17 somehow passes
        Picked using both the Category Partition Testing Method,
        the boundary value testing method, and error guessing.
        """
        self.assertFalse(credit_card_validator("27211233211324509"))

    def test36(self):
        """
        Verifies if an Amex card that has an invalid prefix that is just below
        the range by 1 of prefix 34 (33), but a valid Luhn checksum and
        length (15) will return False. Picked using both the Category Partition
        Testing Method, the boundary value testing method, and error guessing.
        """
        self.assertFalse(credit_card_validator("330000985354258"))

    def test37(self):
        """
        Verifies if an Amex card that has an invalid prefix that is just below
        the range by 1 of prefix 37 (36), but a valid Luhn and a valid
        length (15) returns False. Picked using both the Category Partition
        Testing Method, the boundary value testing method, and error guessing.
        """
        self.assertFalse(credit_card_validator("363694261436829"))

    def test38(self):
        """
        Verifies if an Amex card that has an invalid prefix that is just above
        the range by 1 of 37 (38), but a valid Luhn, and a valid length will
        return False. Picked using both the Category Partition Testing Method,
        the boundary value testing method, and error guessing.
        """
        self.assertFalse(credit_card_validator("384869385466366"))

    def test39(self):
        """
        Verifies that Amex with valid prefix (37) and valid Luhn but an
        invalid length that is exactly one more the threshhold (16) return
        False. Picked using both the Category Partition Testing Method,
        the boundary value testing method, and error guessing.
        """
        self.assertFalse(credit_card_validator("3778924562000260"))

    def test40(self):
        """
        Verifies that Amex with valid prefix (34) and valid Luhn but an invalid
        length that is exactly one more the threshhold (16) return False.
        Picked using both the Category Partition Testing Method,
        the boundary value testing method, and error guessing.
        """
        self.assertFalse(credit_card_validator("3400009853542562"))

    def test41(self):
        """
        Verifies that an empty stirng should return False
        """
        self.assertFalse(credit_card_validator(""))


if __name__ == '__main__':
    unittest.main()
