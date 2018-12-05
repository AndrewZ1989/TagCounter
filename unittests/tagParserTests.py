import unittest
from tagParsing.parser import TagParser, UrlReader
from tagParsing.storage import TagsStorage
from unittest.mock import MagicMock
from synonyms.storage import SynonymsStore


class MyTestCase(unittest.TestCase):
    def test_get_and_view_Tags(self):
        resourcePath = "secretPath"

        synonymsstore = SynonymsStore(None)
        synonymsstore.getFullName = MagicMock(return_value=None)


        tags = {}
        tagsstore = TagsStorage()
        def side_effect(path, val):
            tags[path] = val
        tagsstore.saveTagsFor = MagicMock(side_effect=side_effect)

        urlReader = UrlReader()
        urlReader.readUrl = MagicMock(return_value="<html><div><div/></div></html>")


        parser = TagParser(resourcePath, tagsstore, synonymsstore, urlReader)
        parser.countTagsInfo()


        self.assertEqual(tags[resourcePath]["html"], 1)
        self.assertEqual(tags[resourcePath]["div"], 2)


if __name__ == '__main__':
    unittest.main()
