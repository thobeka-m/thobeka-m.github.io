import unittest

from unittest.mock import patch

import findMySubnetInput

from io import StringIO


class TestFindMySubnetInput(unittest.TestCase):


    @patch('argparse.ArgumentParser.parse_args')

    def test_get_ip(self, mock_parse_args):

        # Test case when a valid IP is provided

        mock_parse_args.return_value = argparse.Namespace(ip='192.168.1.100')

        ip = findMySubnetInput.get_ip()

        self.assertEqual(ip, '192.168.1.100')


        # Test case when an invalid IP is provided

        mock_parse_args.return_value = argparse.Namespace(ip='invalid_ip')

        with self.assertRaises(ValueError):

            findMySubnetInput.get_ip()


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

        mock_is_in_cidr.return_value = True

        result = findMySubnetInput.is_in_cidr("192.168.1.100", "192.168.1.0/24")

        self.assertTrue(result)


        # Test the case when IP is not in the CIDR range

        mock_is_in_cidr.return_value = False

        result = findMySubnetInput.is_in_cidr("10.0.0.1", "192.168.1.0/24")

        self.assertFalse(result)


        # Test the case when either IP or CIDR is invalid

        mock_validate_ip.return_value = False

        mock_validate_cidr.return_value = False

        with self.assertRaises(ValueError):

            findMySubnetInput.is_in_cidr("invalid_ip", "invalid_cidr")


if __name__ == "__main__":

    unittest.main()
