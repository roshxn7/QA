import re

# Sample input
input_data = """
R1#show ip interface brief
Interface             IP-Address      OK? Method Status        Protocol
FastEthernet0/0       15.0.15.1       YES manual up            up
FastEthernet0/1       10.0.12.1       YES manual up            up
FastEthernet0/2       10.0.13.1       YES manual up            up
FastEthernet0/3       unassigned      YES unset  up            down
Loopback0             10.1.1.1        YES manual up            up
Loopback100           100.0.0.1       YES manual up            up
"""

def parse_interface_brief(data):
    # Regular expression pattern to match each line
    pattern = re.compile(r'^(?P<Interface>\S+)\s+(?P<IP_Address>\S+)\s+YES\s+(?P<Method>\S+)\s+(?P<Status>\S+)\s+(?P<Protocol>\S+)$')

    # Initialize the result dictionary
    result = {}

    # Split the input data into lines
    lines = data.strip().split('\n')

    # Iterate over each line starting from the third line (skip header)
    for line in lines[2:]:
        match = pattern.match(line)
        if match:
            # Extract matched groups
            interface = match.group('Interface')
            ip_address = match.group('IP_Address')
            method = match.group('Method')
            status = match.group('Status')
            protocol = match.group('Protocol')

            # Add to the result dictionary
            result[interface] = {
                "IP-Address": ip_address,
                "Method": method,
                "Status": status,
                "Protocol": protocol
            }

    return result

# Parse the input data
parsed_data = parse_interface_brief(input_data)

# Print the result
print(parsed_data)