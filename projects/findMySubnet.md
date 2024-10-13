# AWS Subnet Finder

## Project Case Study

This project aims to provide a simple Python script that helps customers determine which subnet their AWS resource (e.g., EC2 instance, RDS instance) is located in, based on the resource's private IP address. This is particularly useful for customers who may not have in-depth networking knowledge but need to identify the subnet for troubleshooting or management purposes.

The project consists of two Python scripts:

1. `findMySubnet.py`: The main script that interacts with the AWS API to retrieve subnet information and checks if a given IP address falls within any of the subnets.
2. `findMySubnetInput.py`: A helper script that handles user input validation and provides utility functions for IP address and CIDR notation validation.

## Usage Notes

### Prerequisites

Before running the scripts, make sure you have the following prerequisites installed:

1. Python 3.x
2. AWS SDK for Python (Boto3)

You can install the required Python packages using pip:

```bash
pip install boto3
```

### Running the Scripts

1. Open a terminal or command prompt.
2. Navigate to the directory where the `findMySubnet.py` and `findMySubnetInput.py` scripts are located.
3. Run the `findMySubnet.py` script with the private IP address as an argument:

```bash
python findMySubnet.py <private_ip_address>
```

Replace `<private_ip_address>` with the actual private IP address of the resource you want to find the subnet for.

For example:

```bash
python findMySubnet.py 172.31.33.2
```

4. The script will connect to the AWS API, retrieve the subnet information, and check if the provided IP address falls within any of the subnets.
5. If a matching subnet is found, the script will print the subnet ID, CIDR block, and the provided IP address.
6. If no matching subnet is found, the script will print a message indicating that the IP address was not found in any of the subnets.

### Example with finding the ip address of an ec2 instance and an RDS instance 

![AWS Subnet Finder Screenshot](https://github.com/thobeka-m/thobeka-m.github.io/blob/main/images/findMySubnetUsage.PNG)

### Script Breakdown

#### `findMySubnet.py`

- Imports the necessary modules: `boto3` and `findMySubnetInput`.
- Defines the `findMySubnet` function, which is the main entry point of the script.
- Creates a Boto3 client for the EC2 service.
- Retrieves a list of all subnets in the AWS account using the `describe_subnets` method.
- Extracts the subnet IDs and CIDR blocks from the response and stores them in a list of dictionaries.
- Calls the `get_ip` function from `findMySubnetInput` to get the IP address from the user input.
- Iterates over the list of subnets and checks if the provided IP address falls within the CIDR block of each subnet using the `is_in_cidr` function from `findMySubnetInput`.
- If a matching subnet is found, prints the subnet ID, CIDR block, and the provided IP address.
- If no matching subnet is found, prints a message indicating that the IP address was not found in any of the subnets.

#### `findMySubnetInput.py`

- Imports the necessary modules: `ipaddress` and `argparse`.
- Defines the `get_ip` function, which uses the `argparse` module to parse the command-line argument for the IP address.
- Defines the `validate_ip` function, which checks if a given string is a valid IPv4 address using the `ipaddress` module.
- Defines the `validate_cidr` function, which checks if a given string is a valid CIDR notation using the `ipaddress` module.
- Defines the `is_in_cidr` function, which checks if a given IP address falls within a specified CIDR block using the `ipaddress` module.

## Conclusion

The AWS Subnet Finder project provides a convenient way for customers to identify the subnet of their AWS resources based on the resource's private IP address. By leveraging the AWS SDK for Python (Boto3) and Python's built-in modules for IP address and CIDR notation validation, the project offers a simple yet effective solution for customers who may not have extensive networking knowledge.


### link to scripts

https://github.com/thobeka-m/Python/blob/main/Scripts/findMySubnetInput.py
https://github.com/thobeka-m/Python/blob/main/Scripts/findMySubnet.py
