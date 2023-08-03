import sys
from datetime import datetime

sys.path.append('../') # for local testing

import sepm

#ACC-FAC10-L118 for testing

def main():
    #instantiate the API session
    sepm_api = sepm.SymantecEndpointProtectionManagerAPI() #using default

    # use uniqueId
    id = '5184AF1F0AD740896E99FCCD3DB77EAB'
    result = sepm_api.computers.deleteComputer(id)

if __name__ == '__main__':
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    print(f'\script completed, total runtime {end_time - start_time}')
