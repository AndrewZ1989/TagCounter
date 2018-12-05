from baseapplication import app
from appLogging.logger import CustomLogger

logger = CustomLogger()

def runAppendSynonym(shortName, fullName: str):
    app.append(shortName, fullName)


def runGet(resourcePath: str):
    logger.info(resourcePath)
    app.runGet(resourcePath)
    logger.info("Done.")


def runView(resourcePath: str):
    logger.debug(f"Getting tags info for {resourcePath}")
    tags = app.runView(resourcePath)
    if tags is None:
        logger.info("No data")
        return
    for key, value in tags.items():
        logger.info(f"{key} - {value}")