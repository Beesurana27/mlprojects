import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass #decorater (data class)
class DataingestionConfig:
    train_data_path:  str=os.path.join("artifacts","train.csv")
    test_data_path:  str=os.path.join("artifacts","test.csv")
    raw_data_path:  str=os.path.join("artifacts","data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataingestionConfig()
    

    def initiate_data_ingestion(self):#from here we can read the data sets 

        logging.info("entered thed ara ingestion method")
        try:
            df=pd.read_csv("mlprojects\notebook\data\stud.csv") 
            logging.info("reading the dataframe")

            os.makedirs(os.path.dirnamae(self.ingestion_config.train_data_path),exist_ok=True)# creating the path using train data for artifacts
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
           
           
            logging.info(" train test split  ")
            train_set,test_set=train_test_split(df,test_size=0.,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=True,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=True,header=True)

            logging.info(" data ingestion completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except  Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()

        


