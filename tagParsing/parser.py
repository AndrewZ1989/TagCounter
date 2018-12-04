import urllib.request

from synonyms.storage import SynonymsStore
from tagParsing.storage import TagsStorage
from urllib.parse import urlparse
from bs4 import BeautifulSoup

class TagParser:

    def __init__(self, path, storage: TagsStorage, synonyms: SynonymsStore):
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
        tagsinfo = self._doCountTags(self.path)
        self.storage.saveTagsFor(self.path, tagsinfo)

    @staticmethod
    def _urivalidator(x):
        try:
            result = urlparse(x)
            return all([result.scheme, result.netloc, result.path])
        except:
            return False

    @staticmethod
    def _readUrl(path):
        req = urllib.request.Request('http://www.voidspace.org.uk')
        response = urllib.request.urlopen(req)
        return response.read().decode("utf-8")


    def _doCountTags(self, path):
        if not self._urivalidator(path):
            path = self.synonyms.getFullName(path)

        html = self._readUrl(path)
        soup = BeautifulSoup(html, 'html.parser')

        tagsinfo = {}
        for tag in soup.findAll():
            key = tag.name
            tagsinfo[key] = tagsinfo[key] + 1 if key in tagsinfo else 1
        return tagsinfo