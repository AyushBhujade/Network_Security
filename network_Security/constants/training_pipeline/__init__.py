import os
import sys
import numpy as np
import pandas as pd

# defining common variable for training pipeline

PIPELINE_NAME:str='network_Security'
ARTIFACTS_DIR:str='Artifacts'
FILE_NAME:str='NetworkData.csv'
TARGET_COLUMN='Result'

TRAIN_FILE_NAME:str='train.csv'
TEST_FILE_NAME:str='test.csv'

PREPROCESSING_OBJECT_FILE_NAME='preprocessing.pkl'
MODEL_FILE_NAME='model.pkl'
SCHEMA_FILE_PATH=os.path.join('data_schema','schema.yaml')
SCHEMA_DROP_COLUMN='drop_columns'

SAVED_MODEL_DIR=os.path.join('saved_model')


# data ingestion related constant start with DATA_INGESTION var name

DATA_INGESTION_COLLECTION_NAME: str = "Network_data"
DATA_INGESTION_DATABASE_NAME: str = "Network_database"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2

