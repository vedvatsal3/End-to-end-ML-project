import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s %(module)s: %(message)s]"

log_dir = "logs"

logFilepath = os.path.join(log_dir, "running_log.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,
    handlers= [
        logging.FileHandler(logFilepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("mlProjectlogger")