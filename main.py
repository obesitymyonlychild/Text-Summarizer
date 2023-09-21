from src.TextSummarizer.logging import logger
from TextSummarizer.pipeline.data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.data_transformation import DataTransformationTrainingPipeline

logger.info("Welcome to your logging")

STAGE_NAME = "data_ingestion"
try:
    logger.info(f">>>>>>> Starting {STAGE_NAME} <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Finished {STAGE_NAME} <<<<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "data_validation"
try:
    logger.info(f">>>>>>> Starting {STAGE_NAME} <<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>> Finished {STAGE_NAME} <<<<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "data_transformation"
try:
    logger.info(f">>>>>>> Starting {STAGE_NAME} <<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>> Finished {STAGE_NAME} <<<<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
