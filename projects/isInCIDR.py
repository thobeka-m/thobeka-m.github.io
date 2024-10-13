import ipaddress
import argparse


#def get_ip():
#    ip = input("Enter an ip address (ipv4) :")
#    if validate_ip(ip):
#        return ip
#    else:
#        print(f"Invalid IP '{ip}'")

def get_ip():
    parser = argparse.ArgumentParser(
        description="Determine if an IP is in a CIDR range"
    )
    parser.add_argument("ip", help="The IPv4 address to check")
    args = parser.parse_args()
    ip=args.ip
    if validate_ip(ip):
        return ip
    else:
        print(f"Invalid IP '{ip}'")


def get_cidr():
    parser = argparse.ArgumentParser(
        description="Determine if an IP is in a CIDR range"
    )
    parser.add_argument("cidr", help="The IPv4 address to check")
    args = parser.parse_args()
    cidr =args.cidr
    if validate_cidr(cidr):
        return cidr
    else:
        print(f"Invalid IP '{cidr}'")


def get_ip_and_cidr():
    parser = argparse.ArgumentParser(description='Determine if an IP is in a CIDR range')
    parser.add_argument('ip', help='The IPv4 address to check')
    parser.add_argument('cidr', help='The CIDR notation of the network')
    args = parser.parse_args()
    return args.ip, args.cidr


def validate_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def validate_cidr(cidr):
    try:
        ip_obj = ipaddress.ip_network(cidr)
        return True
    except ValueError:
        return False


def is_in_cidr():
    ip, cidr = get_ip_and_cidr()
    if validate_ip(ip) and validate_cidr(cidr):
        if ipaddress.IPv4Address(ip) in ipaddress.IPv4Network(cidr):
            print(f"The network '{cidr}' contains the IP address '{ip}'")
        else:
            print(f"The network '{cidr}' DOES NOT contain the IP address '{ip}'")
    else:
        print("Nothing to do, check your inputs")


# 192.0.2.6
# 192.0.2.0/28


is_in_cidr()
