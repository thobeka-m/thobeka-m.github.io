# sometimes customers want to know which subnet their resource is created in given the private IP address but they don't necessaritly have networking knowledge .
# The below code determines if a private IP falls within given CIDR (subnet or VPC)


import boto3
import findMySubnetInput


def findMySubnet():
    ec2_client = boto3.client("ec2")
    # list all subnets
    response = ec2_client.describe_subnets()

    # extract subnet id and CIDR from the response
    subnets_info = [
        {"SubnetId": subnet["SubnetId"], "CidrBlock": subnet["CidrBlock"]}
        for subnet in response["Subnets"]
    ]

    """same code as :
subnets_info=[] //list of dictionaries
for subnet in response['Subnets']:
    subnets_info.append({'SubnetId':subnet['SubnetId'],
                 'CidrBlock':subnet['CidrBlock']})

"""

    # iterate over each subnet and check if the provided IP address is within the CIDR

    # get and validate ip
    ip = findMySubnetInput.get_ip()
    found_subnet = False

    for subnet in subnets_info:
        cidr = subnet["CidrBlock"]
        is_in_subnet = findMySubnetInput.is_in_cidr(ip, cidr)
        # if the containing subnet is found , stop and print the result
        if is_in_subnet:
            found_subnet = True
            print(f"'{ip}' is in '{subnet['SubnetId']}' with CIDR '{cidr}'")

    if not found_subnet:
        print(
            f" The IP address '{ip}' was not found in any of the subnets , please check your ip and try again"
        )


# python Scripts\findMySubnet.py 192.168.1.100

findMySubnet()
