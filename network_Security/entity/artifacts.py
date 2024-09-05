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
class DataTransformatiArtifact:
    def __init__(self):
        pass
    
@dataclass
class DataValidationArtifact:
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
 