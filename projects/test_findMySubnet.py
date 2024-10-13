import unittest

from unittest.mock import patch

import findMySubnetInput


class TestFindMySubnetInput(unittest.TestCase):

    

    @patch('argparse.ArgumentParser.parse_args')

    def test_get_ip(self, mock_parse_args):

        mock_parse_args.return_value = argparse.Namespace(ip='192.168.1.100')

        ip = findMySubnetInput.get_ip()

        self.assertEqual(ip, '192.168.1.100')

        

        mock_parse_args.return_value = argparse.Namespace(ip='invalid_ip')

        with self.assertRaises(ValueError):

            findMySubnetInput.get_ip()

        

    def test_validate_ip(self):

        self.assertTrue(findMySubnetInput.validate_ip('192.168.1.100'))

        self.assertFalse(findMySubnetInput.validate_ip('invalid_ip'))

        

    def test_validate_cidr(self):

        self.assertTrue(findMySubnetInput.validate_cidr('192.168.1.0/24'))

        self.assertFalse(findMySubnetInput.validate_cidr('invalid_cidr'))

        

    def test_is_in_cidr(self):

        self.assertTrue(findMySubnetInput.is_in_cidr('192.168.1.100', '192.168.1.0/24'))

        self.assertFalse(findMySubnetInput.is_in_cidr('10.0.0.1', '192.168.1.0/24'))

        

        with self.assertRaises(ValueError):

            findMySubnetInput.is_in_cidr('invalid_ip', '192.168.1.0/24')

            

        with self.assertRaises(ValueError):

            findMySubnetInput.is_in_cidr('10.0.0.1', 'invalid_cidr')


if __name__ == '__main__':

    unittest.main()
