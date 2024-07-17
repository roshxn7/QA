import re

def parse_show_ap_summary(output):
    """
    Parse the 'show ap summary' output from the wireless controller.
    """
    ap_info = {}
    
    # Regular expression to capture AP details
    regex = re.compile(
        r'(?P<AP_Name>\S+)\s+'                      # AP Name
        r'(?P<Slots>\d+)\s+'                        # Slots
        r'(?P<AP_Model>\S+)\s+'                     # AP Model
        r'(?P<Ethernet_MAC>\S+)\s+'                 # Ethernet MAC
        r'(?P<Radio_MAC>\S+)\s+'                    # Radio MAC
        r'(?P<CC>\S{2})\s+'                         # Country Code
        r'(?P<RD>[\w-]+)\s+'                        # Regulatory Domain
        r'(?P<IP_Address>\d+\.\d+\.\d+\.\d+)\s+'    # IP Address
        r'(?P<State>\S+)\s+'                        # State
        r'(?P<Location>.+)'                         # Location
    )

    for match in regex.finditer(output):
        ap_info[match.group('AP_Name')] = match.groupdict()

    return ap_info


# Example usage
output = """ewlc#show ap summary 
Number of APs: 3

CC = Country Code
RD = Regulatory Domain

AP Name                          Slots AP Model             Ethernet MAC   Radio MAC      CC   RD   IP Address             State        Location
-------------------------------------------------------------------------------------------------------------------------------------------------------------
APBC26.C7A3.1970                 2     AIR-AP3802E-B-K9     bc26.c7a3.1970 00b7.7166.bea0 US   -B   192.165.7.199          Registered   default location                
APA4B2.3904.1F0C                 3     C9130AXI-B           a4b2.3904.1f0c 2c57.4156.9000 US   -B   192.165.3.119          Registered   default location                
AP6849.92F9.8930                 3     CW9163E-B            6849.92f9.8930 ecf4.0c4f.3360 US   -B   192.165.8.139          Registered   default location                
"""

parsed_output = parse_show_ap_summary(output)
print(parsed_output)