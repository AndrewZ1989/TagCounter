import sqlite3
import pickle
import datetime


def adapt_dict(dict):
    return pickle.dumps(dict)

class TagsStorage:

    tablename = "Data"
    sqlite3.register_adapter(dict, adapt_dict)
    sqlite3.register_converter("dict", pickle.loads)

    def __init__(self):
        pass

    def getTagsFor(self, path):
        dbcur = self.conn.cursor()
        query = f"select path, date, tags from {self.tablename} where path == ? order by date DESC limit 1"
        dbcur.execute(query, (path,))

        dbrecord = dbcur.fetchone()
        if dbrecord is None:
            return None

        rawtagsinfo = dbrecord[2]
        return pickle.loads(rawtagsinfo)

    def saveTagsFor(self, path, tagsInfo: {str: int}):
        dbcur = self.conn.cursor()
        dbcur.execute(f"insert into {self.tablename} values (?, ?, ?)", (path, str(datetime.datetime.now()), tagsInfo))
        dbcur.connection.commit()

    def __enter__(self):
        self.conn = sqlite3.connect('tags.db', detect_types=sqlite3.PARSE_DECLTYPES)
        self._initDatabase()
        return self

    def __exit__(self, *args):
        self.conn.close()

    def _initDatabase(self):
        dbcur = self.conn.cursor()
        dbcur.execute(''' CREATE TABLE IF NOT EXISTS {0}
                     (path text, date text, tags blob)'''.format(self.tablename))
        dbcur.connection.commit()


class MemoryFile(object):
    def __init__(self):
        self.data = []

    def write(self, stuff):
        self.data.append(stuff)

    def getBytes(self):
        return self.data

    def setBytes(self, data):
        self.data = data