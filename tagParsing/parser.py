import urllib.request

from synonyms.storage import SynonymsStore
from tagParsing.storage import TagsStorage
from urllib.parse import urlparse
from bs4 import BeautifulSoup


class UrlReader:

    def readUrl(self, url):
        try:
            req = urllib.request.Request(url)
            response = urllib.request.urlopen(req)
            if response is None:
                return None;
            return response.read().decode("utf-8")
        except:
            return None


class TagParser:

    def __init__(self, path, storage: TagsStorage, synonyms: SynonymsStore, urlReader: UrlReader):
        self.urlReader = urlReader
        self.synonyms = synonyms
        self.storage = storage
        self.path = path

    def getTagInfo(self):
        taginfo = self.storage.getTagsFor(self.path)
        if taginfo is None:
            fullname = self.synonyms.getFullName(self.path)
            if fullname is not None:
                return self.storage.getTagsFor(fullname)
        return taginfo

    def countTagsInfo(self):
        tagsinfo = self._doCountTags()
        self.storage.saveTagsFor(self.path, tagsinfo)


    def _doCountTags(self):
        html = self.urlReader.readUrl(self.path)
        if html is None:
            self.path = self.synonyms.getFullName(self.path)
            html = self.urlReader.readUrl(self.path)
            if html is None:
                return None

        soup = BeautifulSoup(html, 'html.parser')
        tagsinfo = {}
        for tag in soup.findAll():
            key = tag.name
            tagsinfo[key] = tagsinfo[key] + 1 if key in tagsinfo else 1
        return tagsinfo


    @staticmethod
    def _urivalidator(x):
        try:
            result = urlparse(x)
            return all([result.scheme, result.netloc, result.path])
        except:
            return False


