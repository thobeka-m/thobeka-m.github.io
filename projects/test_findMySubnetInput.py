import unittest
from unittest.mock import patch
import findMySubnetInput
from io import StringIO


class TestFindMySubnetInput(unittest.TestCase):

    def test_validate_ip(self):
        valid_ip = "192.168.1.100"
        invalid_ip = "292.168.1.300"
        self.assertTrue(findMySubnetInput.validate_ip(valid_ip))
        self.assertFalse(findMySubnetInput.validate_ip(invalid_ip))

    def test_validate_cidr(self):
        valid_cidr = "192.168.1.0/24"
        invalid_cidr = "292.168.1.0/33"
        self.assertTrue(findMySubnetInput.validate_cidr(valid_cidr))
        self.assertFalse(findMySubnetInput.validate_cidr(invalid_cidr))

    @patch("findMySubnetInput.validate_ip", return_value=True)
    @patch("findMySubnetInput.validate_cidr", return_value=True)
    @patch("findMySubnetInput.is_in_cidr")
    def test_is_in_cidr(self, mock_is_in_cidr, mock_validate_cidr, mock_validate_ip):

        # Test the case when IP is in the CIDR range
        mock_is_in_cidr.return_value = (
            "The network '192.168.1.0/24' contains the IP address '192.168.1.100'"
        )
        result = findMySubnetInput.is_in_cidr("192.168.1.100", "192.168.1.0/24")
        self.assertEqual(
            result,
            "The network '192.168.1.0/24' contains the IP address '192.168.1.100'",
        )

        # Test the case when IP is not in the CIDR range
        mock_is_in_cidr.return_value = (
            "The network '192.168.1.0/24' DOES NOT contain the IP address '10.0.0.1'"
        )
        result = findMySubnetInput.is_in_cidr("10.0.0.1", "192.168.1.0/24")
        self.assertEqual(
            result,
            "The network '192.168.1.0/24' DOES NOT contain the IP address '10.0.0.1'",
        )

        # Test the case when either IP or CIDR is invalid
        mock_validate_ip.return_value = False
        mock_validate_cidr.return_value = False
        mock_is_in_cidr.return_value = "Nothing to do"
        result = findMySubnetInput.is_in_cidr("invalid_ip", "invalid_cidr")
        self.assertEqual(result, "Nothing to do")


if __name__ == "__main__":

    unittest.main()

if __name__ == "__main__":

    unittest.main()
