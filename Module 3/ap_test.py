import re
from pyats.aetest import Testcase, test, main

# Step 1: Define the parser function
def parse_ap_summary(file_path):
    pattern = re.compile(
        r'(?P<AP_Name>\S+)\s+'
        r'(?P<Slots>\d+)\s+'
        r'(?P<AP_Model>\S+)\s+'
        r'(?P<Ethernet_MAC>\S+)\s+'
        r'(?P<Radio_MAC>\S+)\s+'
        r'(?P<CC>\S+)\s+'
        r'(?P<RD>\S+)\s+'
        r'(?P<IP_Address>\S+)\s+'
        r'(?P<State>\S+)\s+'
        r'(?P<Location>.+)')
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

    ap_list = []
    for line in lines:
        match = pattern.match(line)
        if match:
            ap_info = match.groupdict()
            ap_list.append(ap_info)

    return ap_list

# Step 2: Define the function to verify AP state
def verify_ap_state(ap_details):
    for ap in ap_details:
        ap_name = ap['AP_Name']
        state = ap['State']
        if state == 'Registered':
            print(f"{ap_name} state: PASS")
        else:
            print(f"{ap_name} state: FAIL")

class APTest(Testcase):

    @test
    def fetch_ap_details(self):
        ap_details = parse_ap_summary('ap_summary.txt')
        self.ap_details = ap_details
        for ap in ap_details:
            print(f"AP Name: {ap['AP_Name']}")
            print(f"No of Slots: {ap['Slots']}")
            print(f"AP Model: {ap['AP_Model']}")
            print(f"Ethernet MAC: {ap['Ethernet_MAC']}")
            print(f"Radio MAC: {ap['Radio_MAC']}")
            print(f"CC: {ap['CC']}")
            print(f"RD: {ap['RD']}")
            print(f"IP Address: {ap['IP_Address']}")
            print()

    @test
    def verify_ap_state_test(self):
        ap_details = self.ap_details
        verify_ap_state(ap_details)

# Step 3: Implement the main function with run API
if __name__ == '__main__':
    main()
