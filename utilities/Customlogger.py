import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        # Ensure logs directory exists
        logs_dir = os.path.join(os.path.abspath(os.curdir), "logs")
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

        log_file = os.path.join(logs_dir, "automation.log")

        logger = logging.getLogger("AutomationLogger")

        if not logger.handlers:
            file_handler = logging.FileHandler(log_file, mode='a')
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

            # Set log level only once
            logger.setLevel(logging.ERROR)

        return logger