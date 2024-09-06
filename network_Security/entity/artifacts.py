import datetime
import os
from network_Security.constants import training_pipeline
from dataclasses import dataclass

@dataclass
class TrainingPipelineArtifact:
    def __init__(self):
        pass
    
@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str
    
    
@dataclass
class DataValidationArtifact:
    validation_status:bool
    valid_training_file_path:str
    valid_test_file_path:str
    invalid_train_file_path:str
    invalid_ttest_file_path:str
    drift_report_file_path:str
@dataclass
class DataTransformatiArtifact:
    def __init__(self):
        pass
    

    
@dataclass
class  ModelEvaluationArtifact:
    def __init__(self):
        pass
    
@dataclass
class ModelPusherArtifact:
    def __init__(self):
        pass
    
     
@dataclass
class ModelTrainerArtifact :
    def __init__(self):
        pass
 