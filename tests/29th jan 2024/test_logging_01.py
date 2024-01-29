# logging means - You can add logs to the Failure, Information and error
# warning to the users

import logging

def test_print_logs():
    LOGGER = logging.getLogger(__name__)
    #Intentional logging to user
    LOGGER.info("This is information logs")
    LOGGER.error('This is error logs')
    LOGGER.warning('This is warning logs')
    LOGGER.critical('This is critical logs')