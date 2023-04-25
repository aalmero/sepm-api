import sys
from datetime import datetime

sys.path.append('../') # for local testing

import sepm

#ACC-FAC10-L118 for testing

def main():
    #instantiate the API session
    sepm_api = sepm.SymantecEndpointProtectionManagerAPI() #using default

    # get ALL computers
    computers = sepm_api.computers.getComputers()

    print(computers)

    #get specific computers
    computer = sepm_api.computers.getComputers(computerName='ACC-FAC10-L118')

    print(computer)

if __name__ == '__main__':
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    print(f'\script completed, total runtime {end_time - start_time}')
