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