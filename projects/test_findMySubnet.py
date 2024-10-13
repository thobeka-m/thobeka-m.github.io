import unittest
from unittest.mock import patch, MagicMock
import findMySubnet
import findMySubnetInput
from io import StringIO


class TestFindMySubnet(unittest.TestCase):

    @patch("findMySubnet.findMySubnetInput.get_ip")
    @patch("findMySubnet.findMySubnetInput.is_in_cidr")
    @patch("boto3.client")
    def test_find_my_subnet(self, mock_boto3_client, mock_is_in_cidr, mock_get_ip):
        # Mock the input IP address

        mock_get_ip.return_value = "192.168.1.100"
        # Mock the EC2 client and its response

        mock_ec2_client = MagicMock()

        mock_ec2_client.describe_subnets.return_value = {
            "Subnets": [
                {"SubnetId": "subnet-abc123", "CidrBlock": "192.168.1.0/24"},
                {"SubnetId": "subnet-def456", "CidrBlock": "10.0.0.0/16"},
            ]
        }

        mock_boto3_client.return_value = mock_ec2_client

        # Mock the is_in_cidr function

        mock_is_in_cidr.side_effect = [True, False]

        # Capture the output

        with patch("sys.stdout", new=StringIO()) as fake_stdout:

            findMySubnet.FindMySubnet()

            output = fake_stdout.getvalue().strip()

        expected_output = (
            "'192.168.1.100' is in 'subnet-abc123' with CIDR '192.168.1.0/24'"
        )

        self.assertEqual(output, expected_output)


if __name__ == "__main__":

    unittest.main()
