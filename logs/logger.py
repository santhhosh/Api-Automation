"""import logging

logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)", datefmt='%d/%m/%Y %I:%M:%S %p')

logger =logging.getLogger()
logger.setLevel(logging.debug)

logging.basicconfig(filename="test.log")

logs.debug("This is debug message")
logs.info("This is info message")
logs.warning("This is warning message")
logs.error("This is error message")
logs.critical("This is critical message")"""

"""import logging
def get_logs():
 logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)",
    datefmt='%d/%m/%Y %I:%M:%S %p',
    filename="test.log"
)

 logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# logger = logging.getLogger()
 #logger.setLevel(logging.INFO)
#logger.info("Running Get Request Test")
logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")"""
import logging

class logclass:
    def get_the_logs(self):
        logger = logging.getLogger()
        filehandler = logging.FileHandler("C:\\Users\\Harini\\Documents\\Api_Automation_Data\\logs\\logfile.log")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug message")
        logger.info("Information regarding the test case")
        logger.warning("Test case pass but with a Warning message")
        logger.error("Test case fail")
        logger.critical("Important test case fail on which other test case depends")
        return logger