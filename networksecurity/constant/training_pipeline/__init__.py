import os
import pandas as pd
import numpy as np  
import sys

"""
DEFINING ALL THE CONSTANTS FOR TRAINING PIPELINE"""

TARGET_COLUMN:str="result"
PIPELINE_NAME:str="network_security"
ARTIFACT_DIR:str="artifact"
FILE_NAME:str="phisingData.csv"


TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"





DATA_INGESTION_COLLECTION_NAME: str="Network_Data"
DATA_INGESTION_DATABASE_NAME: str="VISHALAI"
DATA_INGESTION_DIR_NAME: str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str="feature_store"
DATA_INGESTION_INGESTED_DIR: str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float=0.2