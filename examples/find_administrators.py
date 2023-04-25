import sys
from datetime import datetime

sys.path.append('../') # for local testing

import sepm

#ACC-FAC10-L118 for testing

def main():
    #instantiate the API session
    sepm_api = sepm.SymantecEndpointProtectionManagerAPI() #using default

    # get ALL administrators
    administrators = sepm_api.administrators.getAllAdminUserDetails()

    print(administrators)

    #get specific administrator
    administrator = sepm_api.administrators.getAdminUserDetails(id='C71763EE0AC7A45E10C52498022E7305')
    print(administrator)

if __name__ == '__main__':
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    print(f'\script completed, total runtime {end_time - start_time}')