import os
import sys
from network_Security.exception.exception import NetworkSecurityException
from network_Security.logger.logger import logging

from network_Security.pipeline.training_pipeline import TrainingPipeline


def start_training():
    try:
        model_trainer=TrainingPipeline()
        model_trainer.run_pipeline()
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
    
if __name__=='__main__':
    start_training()
    