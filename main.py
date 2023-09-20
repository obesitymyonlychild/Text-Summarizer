from src.TextSummarizer.logging import logger
from TextSummarizer.pipline.data_ingestion_1 import DataIngestionTrainingPipeline

logger.info("Welcome to your logging")

STAGE_NAME = "data_ingestion"
try:
    logger.info(f">>>>>>> Starting {STAGE_NAME} <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Finished {STAGE_NAME} <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e