import logging
from logging.handlers import RotatingFileHandler
import os
from datetime import datetime
import pytz

# Constants
LOG_DIR = "logs"
LOG_FILE = "app.log"
LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

# Ensure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Custom Formatter for IST timezone
class ISTFormatter(logging.Formatter):
    def converter(self, timestamp):
        dt = datetime.utcfromtimestamp(timestamp)
        return pytz.utc.localize(dt).astimezone(pytz.timezone("Asia/Kolkata"))

    def formatTime(self, record, datefmt=None):
        dt = self.converter(record.created)
        if datefmt:
            return dt.strftime(datefmt)
        return dt.strftime("%Y-%m-%d %H:%M:%S")

# Create logger
logger = logging.getLogger("jd_generator")
logger.setLevel(logging.INFO)
logger.propagate = False  # Prevent propagation to root logger

# Prevent double logging
if not logger.hasHandlers():
    # Create custom formatter with IST time
    formatter = ISTFormatter(LOG_FORMAT)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler
    file_handler = RotatingFileHandler(
        LOG_FILE_PATH, maxBytes=5 * 1024 * 1024, backupCount=5
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
