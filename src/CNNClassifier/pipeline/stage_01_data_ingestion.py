from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.data_ingestion import DataIngestion
from CNNClassifier import logger

Stage_name = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __int__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.downlad_files()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
