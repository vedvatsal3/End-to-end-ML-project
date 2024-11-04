from src.mlProject import logger
from src.mlProject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.mlProject.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from src.mlProject.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from src.mlProject.pipeline.stage04_model_trainer import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<\n\nx========")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<\n\nx========")
except Exception as e:
    logger.exception(e)
    raise e 



STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<\n\nx========")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<\n\nx========")
except Exception as e:
    logger.exception(e)
    raise e 