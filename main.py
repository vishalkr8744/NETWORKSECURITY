from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_transformation import DataTransformation
import sys


if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()

        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)

        data_ingestion = DataIngestion(dataingestionconfig)

        logging.info("Starting data ingestion")

        data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()

        print(data_ingestion_artifacts)

        logging.info("Data ingestion completed")

        data_validation_config = DataValidationConfig(trainingpipelineconfig)

        data_validation = DataValidation(data_ingestion_artifacts,data_validation_config)
        logging.info("Starting data validation")

        data_validation_artifact = data_validation.initiate_data_validation()
        print(data_validation_artifact)
        logging.info("Data validation completed")
        logging.info("data transformation started")
        Data_Transformation_Config=DataTransformationConfig(trainingpipelineconfig)
        data_transformation=DataTransformation(data_validation_artifact,Data_Transformation_Config)
        data_transformation_artifact= data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data transformation completed")


    except Exception as e:
        raise NetworkSecurityException(e, sys)