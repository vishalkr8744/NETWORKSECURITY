from datetime import datetime
import os
from networksecurity.constant  import training_pipeline

print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)



class TrainingPipelineConfig:
    def __init__(self):
        
            self.pipeline_name=training_pipeline.PIPELINE_NAME
            self.artifact_dir=training_pipeline.ARTIFACT_DIR
            self.timestamp=datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            self.pipeline_artifact_dir=os.path.join(self.artifact_dir,self.timestamp)
            
            self.timestamp: str=self.timestamp




class DataIngestionConfig:
      def __init__(self,training_pipeline_config:TrainingPipelineConfig):
            self.data_ingestion_dir=os.path.join(training_pipeline_config.pipeline_artifact_dir,training_pipeline.DATA_INGESTION_DIR_NAME)  
            self.feature_store_dir=os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR)
            self.ingested_dir=os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR)
            self.feature_store_file_path=os.path.join(self.feature_store_dir,training_pipeline.FILE_NAME)
            self.train_file_path=os.path.join(self.ingested_dir,training_pipeline.TRAIN_FILE_NAME)
            self.test_file_path=os.path.join(self.ingested_dir,training_pipeline.TEST_FILE_NAME)

            self.train_test_split_ratio=training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
            self.collection_name=training_pipeline.DATA_INGESTION_COLLECTION_NAME
            self.database_name=training_pipeline.DATA_INGESTION_DATABASE_NAME          