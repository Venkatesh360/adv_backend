import logging
import sys


logger = logging.getLogger("FastApp")

#creating formatter
formatter = logging.Formatter(fmt="time: %(asctime)s - log_level: %(levelname)s - message: %(message)s")

#create handlers
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('app.log')

#set formatters
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

#adding handlers to the logger instance
logger.handlers = [stream_handler, file_handler]

#setting log level 
logger.setLevel(logging.INFO)



