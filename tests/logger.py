import logging

#logging is a package available in python by default and we no need to install this explicitly
#purpose of loggers is to identify the reason for failure and also to write status messages to a file about which
#part of the code is executed
def test_logging():

    logger=logging.getLogger(__name__)
    #get logger is responsible for printing the log message to the log file and create object for logging class and call get logger method

    #now we need to identify in which file the logs messages to be printed
    filehandler=logging.FileHandler("logfile.txt")
    #logging class has a method called filehandler using which we can pass the file information to which we can write logs to
    #now pass the filehandler object to logger.addhandler,so that logger now will have information about where to print the logs.
    logger.addHandler(filehandler)

    #now after finding which file we need to write the logs to,now we need to identify the format
    #in which we need to print the logs and pass this info to logger which is responsible for printing the logs.

    formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

    #similarly logging parent class has a method called formatter which tells in which format to print the logs
    #now we need to establish a connection between logger and logging,since logger already has information about
    #filehandler,by establishing connection between filehandler and formatter,logger will have info about formatter

    filehandler.setFormatter(formatter)
    #this will establish connection between file handler and formatter--since filehandler is already wrapped inside logger.addhandler,
    #by establishing connection between filehandler and formatter,logger will have information about formatter as well
    #now logger knows where to print and which format to print

    #now set the log level

    logger.setLevel(logging.INFO)



#These are the different log messages at different level
    logger.debug("Print the debug statement")
    logger.info("provide information")
    logger.warning("inform about alerts or warning")
    logger.error("a major failure and reason for the value Ex:assertion error")
    logger.critical("A critical failure,test cannot continue")
    return logger