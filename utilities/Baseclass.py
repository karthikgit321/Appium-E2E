import inspect
import pytest
import logging

from appium.webdriver.common.touch_action import TouchAction


@pytest.mark.usefixtures("setup")
class Baseclass:
    pass
    action = TouchAction
    import logging

    # logging is a package available in python by default and we no need to install this explicitly
    # purpose of loggers is to identify the reason for failure and also to write status messages to a file about which
    # part of the code is executed
    def get_Logger(self):
        loggername=inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        # get logger is responsible for printing the log message to the log file and create object for logging class and call get logger method

        # now we need to identify in which file the logs messages to be printed
        filehandler = logging.FileHandler("logfile.log")
        # logging class has a method called filehandler using which we can pass the file information to which we can write logs to
        # now pass the filehandler object to logger.addhandler,so that logger now will have information about where to print the logs.
        #logger.addHandler(filehandler)

        # now after finding which file we need to write the logs to,now we need to identify the format
        # in which we need to print the logs and pass this info to logger which is responsible for printing the logs.

        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

        # similarly logging parent class has a method called formatter which tells in which format to print the logs
        # now we need to establish a connection between logger and logging,since logger already has information about
        # filehandler,by establishing connection between filehandler and formatter,logger will have info about formatter

        filehandler.setFormatter(formatter)
        # this will establish connection between file handler and formatter--since filehandler is already wrapped inside logger.addhandler,
        # by establishing connection between filehandler and formatter,logger will have information about formatter as well
        # now logger knows where to print and which format to print

        # now set the log level
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger

    def scroll(self, ori_element=None, dest_element= None, x1=None, y1=None, x2= None, y2=None):
        """
        Function to scroll between 2 points
        :param ori_element: the element to be moved from
        :param dest_element: the element to be moved to
        :param x1: x coordiate to be moved from
        :param y1: y coordiate to be moved from
        :param x2: x coordiate to be moved to
        :param y2: y coordiate to be moved to
        :return:
        """
        Baseclass.action(self.driver).press(el=ori_element, x=x1, y=y1).move_to(el=dest_element, x=x2, y=y2).release().perform()