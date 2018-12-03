import sqlite3


class TagsStorage:

    def __init__(self):
        self._innerStore = {}

    def getTagsFor(self, path):
        if path in self._innerStore:
            return self._innerStore[path]
        return None

    def saveTagsFor(self, path, tagsInfo: {str: int}):
        self._innerStore[path] = tagsInfo

    def __enter__(self):
        self.conn = sqlite3.connect('tags.db')
        return self

    def __exit__(self, *args):
        self.conn.close()