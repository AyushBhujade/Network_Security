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
    DataTransformatiConfig,
    DataValidationConfig,
    ModelEvaluationConfig,
    ModelPusherConfig,
    ModelTrainerConfig  
)

from network_Security.entity.artifacts import (
    TrainingPipelineArtifact,
    DataIngestionArtifact,
    DataTransformatiArtifact,
    DataValidationArtifact,
    ModelEvaluationArtifact,
    ModelPusherArtifact,
    ModelTrainerArtifact 
)

class TrainingPipeline:
    def __init__(self):
        pass
    
    def start_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def run_pipeline(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)