from synonyms.storage import SynonymsStore
from tagParsing.parser import TagParser, UrlReader
from tagParsing.storage import TagsStorage

store = SynonymsStore("synonyms.yaml")


def runAppendSynonym(shortName, fullName: str):
    store.append(shortName, fullName)


def runGet(resourcePath: str):
    with TagsStorage() as storage:
        parser = TagParser(resourcePath, storage, store, UrlReader())
        parser.countTagsInfo()


def runView(resourcePath: str):
    with TagsStorage() as storage:
        parser = TagParser(resourcePath, storage, store, UrlReader())
        return parser.getTagInfo()
