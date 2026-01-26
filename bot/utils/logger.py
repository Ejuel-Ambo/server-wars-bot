import logging
import sys
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

def setup_logging(level=logging.INFO):
    # Ensure logs directory exists
    Path("logs").mkdir(exist_ok=True)
    
    # Define formatting
    log_format = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d - %(message)s'
    )

    # 1. Console Handler (Outputs to your terminal)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_format)

    # 2. File Handler (Outputs to logs/serverwars.log)
    file_handler = TimedRotatingFileHandler(
        filename="logs/serverwars.log",
        when="midnight",
        interval=1,
        backupCount=5,
        encoding="utf-8"
    )
    file_handler.setFormatter(log_format)

    # Root logger setup
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    logging.info("Logging system initialized.")
