from datetime import datetime

import sepm

def main():
    #instantiate the API session
    sepm = sepm.SymantecEndpointProtectionManagerAPI(
                username='',
                password='',
                domain='',
                base_url=''
    )

    computers = sepm.computers.getComputers()

if __name__ == '__main__':
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    print(f'\script completed, total runtime {end_time - start_time}')
