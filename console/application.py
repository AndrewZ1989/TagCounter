from appLogging.logger import CustomLogger
from synonyms.storage import Store

logger = CustomLogger()
store = Store()


def runAppendSynonym(shortName, fullName:str):
    store.append(shortName, fullName)


def runGet(resourcePath :str):
    logger.info(resourcePath)

    pass


def runView(resourcePath :str):
    logger.debug(f"Getting tags info for {resourcePath}")
    pass
