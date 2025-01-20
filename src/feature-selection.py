import pandas as pd
import os 
import logging


log_dir = "./logs"
#Ensuring the log path exits
os.makedirs(log_dir,exist_ok=True)

logger = logging.getLogger('feature_selection')
logger.setLevel("DEBUG")

#Console handler 
console_handler = logging.StreamHandler()
console_handler.setLevel("DEBUG")

#File handler
file_log_path = os.path.join(log_dir,"feature_selection.log")
file_handler = logging.FileHandler(file_log_path)
file_handler.setLevel("DEBUG")

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def load_data(file_path:str)->pd.DataFrame:
    """Load data from CSV file"""
    try:
        df = pd.read_csv(file_path)
        df.fillna('',inplace=True)
        logger.debug("File loaded from : %s",file_path)
        return df
    except pd.errors.ParserError as e:
        logger.error("Failed to parse the CSV file: %s",e)
        raise
    except Exception as e:
        logger.error("Unexpected error occured while feature selection and loading the data %s",e)
        raise

def save_data(df: pd.DataFrame, file_path: str) -> None:
    """Save the dataframe to a CSV file."""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        df.to_csv(file_path, index=False)
        logger.debug('Data saved to %s', file_path)
    except Exception as e:
        logger.error('Unexpected error occurred while saving the data: %s', e)
        raise