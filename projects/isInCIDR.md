
# CIDR Range Checker

## Description

The CIDR Range Checker is a Python script that helps you determine whether a given IPv4 address falls within a specified CIDR (Classless Inter-Domain Routing) range or not. It utilizes Python's `ipaddress` module and `argparse` module for input validation and command-line argument parsing.

## Usage

To use the CIDR Range Checker, follow these steps:

1. Make sure you have Python 3.x installed on your system.
2. Open a terminal or command prompt and navigate to the directory containing the Python script.
3. Run the script with the required arguments:

```
python script.py <ip_address> <cidr_notation>
```

Replace `<ip_address>` with the IPv4 address you want to check, and `<cidr_notation>` with the CIDR notation of the network you want to check against.

For example:

```
python script.py 192.0.2.6 192.0.2.0/28
```

4. The script will validate the provided inputs and print a message indicating whether the IP address falls within the specified CIDR range or not.

## Functions

The CIDR Range Checker script includes the following functions:

### `get_ip()`

This function uses the `argparse` module to parse the command-line arguments and retrieve the IP address. It calls the `validate_ip` function to ensure that the provided IP address is valid.

### `get_cidr()`

This function uses the `argparse` module to parse the command-line arguments and retrieve the CIDR notation. It calls the `validate_cidr` function to ensure that the provided CIDR notation is valid.

### `get_ip_and_cidr()`

This function uses the `argparse` module to parse the command-line arguments and retrieve both the IP address and CIDR notation.

### `validate_ip(ip)`

This function takes an IP address as input and uses the `ipaddress` module to validate whether it is a valid IPv4 address or not. It returns `True` if the IP address is valid, and `False` otherwise.

### `validate_cidr(cidr)`

This function takes a CIDR notation as input and uses the `ipaddress` module to validate whether it is a valid CIDR notation or not. It returns `True` if the CIDR notation is valid, and `False` otherwise.

### `is_in_cidr()`

This function is the main entry point of the script. It calls the `get_ip_and_cidr` function to retrieve the IP address and CIDR notation from the command-line arguments. It then validates the inputs using the `validate_ip` and `validate_cidr` functions. If both inputs are valid, it checks whether the IP address falls within the specified CIDR range using the `ipaddress` module. Finally, it prints a message indicating whether the IP address is in the CIDR range or not.

## Example

```
$ python script.py 192.0.2.6 192.0.2.0/28
The network '192.0.2.0/28' contains the IP address '192.0.2.6'

$ python script.py 192.0.2.100 192.0.2.0/28
The network '192.0.2.0/28' DOES NOT contain the IP address '192.0.2.100'
```

In the first example, the IP address `192.0.2.6` falls within the CIDR range `192.0.2.0/28`, so the script prints a message indicating that the IP address is contained in the network. In the second example, the IP address `192.0.2.100` does not fall within the CIDR range `192.0.2.0/28`, so the script prints a message indicating that the IP address is not contained in the network.


### Link to script
https://github.com/thobeka-m/thobeka-m.github.io/blob/0d37084b50128e36f3ec1a293baaa9a83ad76616/projects/isInCIDR.py
