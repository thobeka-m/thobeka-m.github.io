import ipaddress
import argparse


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

def validate_ip(ip):

    try:
        ipaddress.IPv4Address(ip)
        return True
    except ValueError:
        return False


def validate_cidr(cidr):
    try:
        ipaddress.IPv4Network(cidr)
        return True
    except ValueError:
        return False


def is_in_cidr(ip, cidr):

    if not validate_ip(ip):
        raise ValueError("Invalid IP address")

    if not validate_cidr(cidr):
        raise ValueError("Invalid CIDR notation")
    
    ip_obj = ipaddress.IPv4Address(ip)
    network_obj = ipaddress.IPv4Network(cidr)

    return ip_obj in network_obj
