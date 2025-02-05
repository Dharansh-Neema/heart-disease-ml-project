import pandas as pd
import os
from sklearn.model_selection import train_test_split
import logging

log_dir = "logs"

os.makedirs(log_dir,exist_ok=True)

#Logging handler 
logger = logging.getLogger("data-ingestion")
logger.setLevel("DEBUG")

#Logging file handler 
log_file_path = os.path.join(log_dir,'data_preprocessing.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel("DEBUG")


#Console hanler
console_handler = logging.StreamHandler()
console_handler.setLevel("DEBUG")

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def load_data(data_path:str)->pd.DataFrame:
    """Load data from a data_path into a CSV file"""
    try:
        df = pd.read_csv(data_path)
        logger.debug("Data loaded into CSV from %s",data_path)
        return df
    except pd.errors.ParserError as e:
        logger.error('Failed to parse the CSV file',e)
        raise
    except Exception as e:
        logger.error("Unexpected error occured: %s",e)
        raise
def preprocess_data(df: pd.DataFrame)-> pd.DataFrame:
    """Preprocess the data"""
    try:
        df.drop(columns = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace = True)
        df.rename(columns={'v1':'target','v2':'text',},inplace=True)
        logger.debug("Data Processing completed")
        return df
    except KeyError as e:
        logger.error("Missing Column in the dataframe: %s",e)
        raise
    except Exception as e:
        logger.error("Unexpected error occured during data processing: %s",e)
        raise
def save_data(train_data:pd.DataFrame,test_data:pd.DataFrame,data_path:str)->None:
    """Save the train and test datasets."""
    try:
        raw_data_path = os.path.join(data_path,'raw')
        os.makedirs(raw_data_path,exist_ok=True)
        train_data.to_csv(os.path.join(raw_data_path,"train.csv"),index=False)
        test_data.to_csv(os.path.join(raw_data_path,"test.csv"),index=False)
        logger.debug("Train and Test Data saved to %s",raw_data_path)
    except Exception as e:
        logger.error("Unexpected error occure while saving the data: %s",e)
        raise

def main():
    try:
        test_size = 0.2 # test size of 20%
        data_url = "https://raw.githubusercontent.com/Dharansh-Neema/heart-disease-ml-project/refs/heads/main/heart-disease.csv"
        final_df = load_data(data_path=data_url)
        
        train_data,test_data = train_test_split(final_df,test_size=test_size,random_state=2)
        save_data(train_data,test_data,data_path="./data")
    except Exception as e:
        logger.error("Failed to complete the data ingesting process: %s",e)

if __name__=='__main__':
    main()
