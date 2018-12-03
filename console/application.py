from appLogging.logger import CustomLogger
from synonyms.storage import SynonymsStore
from tagParsing.parser import TagParser
from tagParsing.storage import TagsStorage

logger = CustomLogger()
store = SynonymsStore()


def runAppendSynonym(shortName, fullName: str):
    store.append(shortName, fullName)


def runGet(resourcePath: str):
    logger.info(resourcePath)

    with TagsStorage() as storage:
        parser = TagParser(resourcePath, storage, store)
        parser.countTagsInfo()

    logger.info("Done.")


def runView(resourcePath: str):
    logger.debug(f"Getting tags info for {resourcePath}")

    with TagsStorage() as storage:
        parser = TagParser(resourcePath, storage, store)
        tags = parser.getTagInfo()
        if tags is None:
            logger.info("No data")
            return
        for key, value in tags.items():
            logger.info(f"{key} - {value}")