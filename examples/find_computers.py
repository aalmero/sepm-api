import sys
from datetime import datetime
import pprint

sys.path.append('../') # for local testing

import sepm

#ACC-FAC10-L118 for testing

def main():
    #instantiate the API session
    sepm_api = sepm.SymantecEndpointProtectionManagerAPI() #using default

    # get ALL computers
    #computers = sepm_api.computers.getComputers()

    #print(computers)

    #get specific computers, use computerName
    computerName = 'AMANCTXBFUD09'
    computer = sepm_api.computers.getComputers(computerName=computerName)

    pprint.pprint(computer)

if __name__ == '__main__':
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    print(f'\script completed, total runtime {end_time - start_time}')
