import os
import sys

from network_Security.exception.exception import NetworkSecurityException
from network_Security.logger.logger import logging


from network_Security.components.data_injestion import DataIngestion
from network_Security.components.data_transformation import DataTransformation
from network_Security.components.data_validation import DataValidation
from network_Security.components.model_evalutaion import ModelEvaluation
from network_Security.components.model_pusher import ModelPusher
from network_Security.components.model_trainer import ModelTrainer

from network_Security.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataTransformationConfig,
    DataValidationConfig,
    ModelEvaluationConfig,
    ModelPusherConfig,
    ModelTrainerConfig  
)

from network_Security.entity.artifacts import (
    TrainingPipelineArtifact,
    DataIngestionArtifact,
    DataTransformationArtifact,
    DataValidationArtifact,
    ModelEvaluationArtifact,
    ModelPusherArtifact,
    ModelTrainerArtifact 
)


from network_Security.constants.training_pipeline import TRAINING_BUCKET_NAME,SAVED_MODEL_DIR
from network_Security.cloud.s3_syncer import S3Sync

class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config=TrainingPipelineConfig()
        self.s3_sync=S3Sync()
        self.is_pipeline_running=False
    
    def start_data_ingestion(self):
        try:
            self.data_ingestion_config=DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("starting data ingetion")
            data_ingestion= DataIngestion(self.data_ingestion_config)
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info("data ingestion completed and artifact")
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact):
        try:
            data_validation_config=DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation=DataValidation(data_ingestion_artifact=data_ingestion_artifact,data_validation_config=data_validation_config)
            data_validation_artifact=data_validation.initiate_data_validation()
            return data_validation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_data_transformation(self,data_validation_artifact:DataValidationArtifact):
        try:
            data_transformation_config=DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            data_transformation=DataTransformation(data_validation_artifact=data_validation_artifact,
                               data_transformation_config=data_transformation_config)
            data_transformation_artifact=data_transformation.initiate_data_transformation()
            return data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_model_trainer(self,data_transformation_artifact:DataTransformationArtifact)->ModelTrainerArtifact:
        try:
            self.model_trainer_config:ModelTrainerConfig=ModelTrainerConfig(training_pipeline_config=self.training_pipeline_config)
            model_trainer=ModelTrainer(
                data_transformation_artifact=data_transformation_artifact,
                model_trainer_config=self.model_trainer_config
            )
            model_trainer_artifact=model_trainer.initiate_model_trainer()
            return model_trainer_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_model_evaluation(self,data_validation_artifact:DataValidationArtifact,
                               model_trainer_artifact:ModelTrainerArtifact):
        
        try:
            model_evaluation_config:ModelEvaluationConfig=ModelEvaluationConfig(training_pipeline_config=self.training_pipeline_config)
            model_evaluation=ModelEvaluation(model_evaluation_config,data_validation_artifact,model_trainer_artifact)
            model_evaluation_artifact=model_evaluation.initiate_model_evaluation()
            return model_evaluation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_model_pusher(self,model_eval_artifact:ModelEvaluationArtifact):
        try:
            model_pusher_config = ModelPusherConfig(training_pipeline_config=self.training_pipeline_config)
            model_pusher = ModelPusher(model_pusher_config, model_eval_artifact)
            model_pusher_artifact = model_pusher.initiate_model_pusher()
            return model_pusher_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def sync_artifact_dir_to_s3(self):
        try:
            aws_bucket_url = f"s3://{TRAINING_BUCKET_NAME}/artifact/{self.training_pipeline_config.timestamp}"
            self.s3_sync.sync_folder_to_s3(folder = self.training_pipeline_config.artifact_dir,aws_bucket_url=aws_bucket_url)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
            
    def sync_saved_model_dir_to_s3(self):
        try:
            aws_bucket_url = f"s3://{TRAINING_BUCKET_NAME}/{SAVED_MODEL_DIR}"
            self.s3_sync.sync_folder_to_s3(folder = SAVED_MODEL_DIR,aws_bucket_url=aws_bucket_url)
        except Exception as e:
            raise NetworkSecurityException(e,sys)  
        
    def run_pipeline(self):
        try:
            data_ingestion_artifacts=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifacts)
            data_transformation_artifact=self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            model_trainer_artifact=self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            model_evaluation_artifact=self.start_model_evaluation(data_validation_artifact=data_validation_artifact,model_trainer_artifact=model_trainer_artifact)
            if not model_evaluation_artifact.is_model_accepted:
                print("training model is not better than the best model")
            model_pusher_artifact = self.start_model_pusher(model_evaluation_artifact)
            
            TrainingPipeline.is_pipeline_running=False
            self.sync_artifact_dir_to_s3()
            self.sync_saved_model_dir_to_s3()
        except Exception as e:
            raise NetworkSecurityException(e,sys)