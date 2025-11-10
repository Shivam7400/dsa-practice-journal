import os, logging, re, sys, traceback
from logging.handlers import RotatingFileHandler
from datetime import datetime

DEBUG = False
# ----------------------------------------- Logger Configure ------------------------------------------
LOG_COLORS = {
    'DEBUG': '\033[94m',   # Blue
    'INFO': '\033[92m',    # Green
    'WARNING': '\033[93m', # Yellow
    'ERROR': '\033[1;91m',   # Bold Red
    'CRITICAL': '\033[1;91m',  # Bold Red
    'RESET': '\033[0m',    # Reset to default
}

# Create a custom formatter
class ColorFormatter(logging.Formatter):
    def format(self, record):
        # Colorize the log level name
        levelname_color = LOG_COLORS.get(record.levelname, LOG_COLORS['RESET'])
        reset_color = LOG_COLORS['RESET']
        
        # Format the log level with color
        colored_levelname = f"{levelname_color}{record.levelname}{reset_color}"
        
        # Replace the log level in the original message with the colored version
        log_message = super().format(record)
        return log_message.replace(record.levelname, colored_levelname, 1)
    
def custom_namer(default_name):
    """
    Custom naming function for rotated log files.
    Adds a timestamp or custom identifier to the rotated file name.
    """
    log_dir, log_filename = os.path.split(default_name)
    file_name, ext = log_filename.rsplit('.', 1)
    return os.path.join(log_dir, f"{ext}.{file_name}")


class CustomLogger(Exception):
    @classmethod
    def configure_logger(cls):
        LOG_DIR = "logs"
        CURR_DIR = os.getcwd()
        LOG_PATH = os.path.join(CURR_DIR, LOG_DIR)

        if not os.path.exists(LOG_PATH):
            """
            if the Logs directory is not present 
            then create it.
            """
            os.makedirs(LOG_PATH)

        current_time = datetime.now()
        base_log_file_name = f"log_{current_time.day}_{current_time.month}_{current_time.year}"
        logfile_path = os.path.join(LOG_PATH, base_log_file_name + ".log")

        # Initialize the suffix as 0
        suffix = 0

        # If the log file exists, append an incrementing suffix (_1, _2, etc.)
        while os.path.exists(logfile_path):
            suffix += 1
            logfile_path = os.path.join(LOG_PATH, f"{base_log_file_name}_{suffix}.log")

        # Create and configure logger
        current_logger = logging.getLogger(__name__)    # Creating an object
        current_logger.setLevel(logging.DEBUG)   # Setting the threshold of logger to DEBUG

        console_formatter = ColorFormatter('%(levelname)s - %(asctime)s - %(message)s', datefmt='%d-%m-%Y %H:%M:%S')
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(console_formatter)

        # File Handler: Output to a log file
        file_formatter = logging.Formatter('%(levelname)s - %(asctime)s - %(message)s', datefmt='%d-%m-%Y %H:%M:%S')
        file_handler = RotatingFileHandler(
            logfile_path,  # Log file name
            maxBytes=10 * 1024 * 1024,  # Max file size in bytes (10 MB)
            backupCount=20,  # Keep up to 10 backup files (1.log.log, 2.log.log, etc.)
            encoding="UTF-8"
        )
        file_handler.namer = custom_namer
        file_handler.setFormatter(file_formatter)

        # Add both handlers to the logger
        current_logger.addHandler(console_handler)
        current_logger.addHandler(file_handler)
        cls.current_logger = current_logger

    @classmethod
    def fix(cls, text):
        return re.sub(r"\s+", " ", str(text).replace("\n", " "))[:500]

    @classmethod
    def info(cls, message):
        cls.current_logger.info(message)

    @classmethod
    def error(cls, message):
        cls.log_exception_details(message, "error")

    @classmethod
    def warning(cls, message):
        cls.log_exception_details(message, "warning")

    @classmethod
    def log_exception_details(cls, message, log_level="error"):
        # Ensure valid log_level is passed
        log_level = log_level.lower()
        if log_level not in ["error", "warning"]:
            log_level = "error"  # Default to error if invalid level is passed

        exc_type, exc_value, exc_tb = sys.exc_info()
        tb = traceback.extract_tb(exc_tb)

        file = ""
        code_line = ""
        line_no = ""
        for i in tb:
            code_line = i.line.strip()
            line_no = i.lineno
            file += f" -> {os.path.basename(i.filename)}({line_no})"

        if log_level == "warning" and not exc_tb:
            log_message = (
                f"Msg: {message} | File:{file} | "
                f"Err: {cls.fix(exc_value)} | "
                f"Code: {code_line}"
            )
            cls.current_logger.warning(log_message)
            return

        if not exc_tb:
            log_message = (
                f"Msg: {message} | File:{file} | "
                f"Err: {cls.fix(exc_value)} | "
                f"Code: {code_line}"
            )
            cls.current_logger.error(log_message)
            return

        # Extract the code causing the error
        locals_at_error = exc_tb.tb_frame.f_locals  # Get local variables

        # Attempt to identify the variable causing the issue
        suspected_variable = ""

        for var_name, var_value in locals_at_error.items():
            if var_name in code_line:
                suspected_variable = f"{var_name} = {var_value}"
                break
        
        exception_doc_string = exc_type.__doc__ if exc_type.__doc__ else ""

        log_message = (
            f"Msg: {message} | File:{file} | "
            f"Err: {cls.fix(exc_value)} | "
            f"Err Details: {cls.fix(exception_doc_string)} | "
            f"Code: {code_line} | Value: {cls.fix(suspected_variable)}"
        )

        if log_level == "warning":
            cls.current_logger.warning(log_message)
        else:
            cls.current_logger.error(log_message)
            if DEBUG:
                raise
