from CNNClassifier import logger
from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

Stage_name = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

Stage_name = "Prepare Base Model stage"

try:
    logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e