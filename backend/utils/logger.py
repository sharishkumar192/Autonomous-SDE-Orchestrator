import sys
import os
import logging
from loguru import logger as loguru_logger  # Rename to avoid name clashes

# Create logs directory
LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

class InterceptHandler(logging.Handler):
    """Bridges standard logging to Loguru with explicit name protection."""
    def emit(self, record):
        try:
            # Explicitly call loguru_logger
            level = loguru_logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Use Python's built-in logging to get the frame, not loguru
        frame, depth = logging.currentframe(), 2
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        loguru_logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())

def setup_logging():
    """Initializes Loguru and redirects library logs."""
    loguru_logger.remove()
    
    # Terminal Output
    loguru_logger.add(
        sys.stderr, 
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>", 
        colorize=True
    )
    
    # File Output
    loguru_logger.add(
        os.path.join(LOG_DIR, "app.log"), 
        rotation="10 MB", 
        retention="10 days", 
        compression="zip"
    )

    # Bridge the root logging
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
    
    # Force external libraries to use our new bridge
    for logger_name in ("uvicorn", "uvicorn.error", "uvicorn.access", "fastapi"):
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler()]
        logging_logger.propagate = False

    return loguru_logger

# Export the clean log object
log = setup_logging()   