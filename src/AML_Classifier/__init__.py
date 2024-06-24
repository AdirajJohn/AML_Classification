#python script to print the logger information on console and save the logs in the running_logs.logs
import os
import sys
import logging

logging_str= "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,

    handlers=[
        logging.FileHandler(log_filepath),# to create the folder and save the log information in running_logs.log
        logging.StreamHandler(sys.stdout) # To print the log in termial
    ]
)

logger = logging.getLogger("AMLClassifierLogger")