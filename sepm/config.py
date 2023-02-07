#libary constants

# API username and password configure either at instantiation or as an environment variable
API_USERNAME_ENV='API_USERNAME'
API_PASSWORD_ENV='API_PASSWORD'
API_DOMAIN_ENV='API_DOMAIN'

# Base URL preceding all endpoint resources
DEFAULT_BASE_URL='https://epp.internal.corp:8446/sepm/api/v1'

# Authentication URL
AUTH_URL='{0}/identity/authenticate'.format(DEFAULT_BASE_URL)

# create output log file
OUTPUT_LOG = True

# Path to output log; by default, working directory of script if not specified
LOG_PATH = ''

# Log file name appended with date and timestamp
LOG_FILE_PREFIX = 'sepm_api_'

# Print output logging to console?
PRINT_TO_CONSOLE = True

# Enable/Disable Logging
SUPPRESS_LOGGING=False

#inherit an external logger instance.
INHERIT_LOGGING_CONFIG = False

# Simulate POST/PUT/DELETE calls
SIMULATE_API=False

# Retry n times when encountering 429s or other server-side errors
MAXIMUM_RETRIES = 2