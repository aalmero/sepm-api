"""sepm - Symantec Endpoint Protection Manager API"""

from datetime import datetime
import logging
import os

from sepm.rest_api_session import *
from sepm.endpoints.computers import Computers

#config import
from sepm.config import (
    API_USERNAME_ENV,
    API_PASSWORD_ENV,
    API_DOMAIN_ENV,
    DEFAULT_BASE_URL,
    AUTH_URL,
    OUTPUT_LOG,
    LOG_PATH,
    LOG_FILE_PREFIX,
    PRINT_TO_CONSOLE,
    SUPPRESS_LOGGING,
    INHERIT_LOGGING_CONFIG,
    SIMULATE_API,
)

__version__ = '0.0.1'
__author__ = 'Alex Almero <aalmero@gmail.com>'
__all__ = []

class SymantecEndpointProtectionManagerAPI(object):
    """
    create a persistent Symantec Endpoint Protection Manager API session
    ....
    """

    def __init__(self,
                 username=None,
                 password=None,
                 domain=None,
                 base_url=DEFAULT_BASE_URL,
                 auth_url=AUTH_URL,
                 output_log=OUTPUT_LOG,
                 log_path=LOG_PATH,
                 log_file_prefix=LOG_FILE_PREFIX,
                 print_console=PRINT_TO_CONSOLE,
                 suppress_logging=SUPPRESS_LOGGING,
                 simulate=SIMULATE_API,
                 inherit_logging_config=INHERIT_LOGGING_CONFIG,
                 ):

        # check API credentials
        username = username or os.environ.get(API_USERNAME_ENV)
        password = password or os.environ.get(API_PASSWORD_ENV)
        domain = domain or os.environ.get(API_DOMAIN_ENV)

        print('username={0}, password={1}, domain={2}'.format(username, password, domain))
        #logging.info('username = %s', username)

        if not username or not password:
            raise APIError()

        inherit_logging_config = inherit_logging_config

        # configure logging
        if not suppress_logging:
            self._logger = logging.getLogger(__name__)

            if not inherit_logging_config:
                self._logger.setLevel(logging.DEBUG)

                formatter = logging.Formatter(
                    fmt='%(asctime)s %(name)12s: %(levelname)8s > %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                )
                handler_console = logging.StreamHandler()
                handler_console.setFormatter(formatter)

                if output_log:
                    if log_path and log_path[-1] != '/':
                        log_path += '/'
                    self._log_file = f'{log_path}{log_file_prefix}_log__{datetime.now():%Y-%m-%d_%H-%M-%S}.log'
                    handler_log = logging.FileHandler(
                        filename=self._log_file
                    )
                    handler_log.setFormatter(formatter)

                if output_log and not self._logger.hasHandlers():
                    self._logger.addHandler(handler_log)
                    if print_console:
                        handler_console.setLevel(logging.INFO)
                        self._logger.addHandler(handler_console)
                elif print_console and not self._logger.hasHandlers():
                    self._logger.addHandler(handler_console)
        else:
            self._logger = None

        # create the API session
        self._session = RestApiSession(
            logger = self._logger,
            username = username,
            password = password,
            domain = domain,
            base_url = base_url,
            auth_url = auth_url,
            simulate = simulate,
        )

        # API endpoints definition
        self.computers = Computers(self._session)
