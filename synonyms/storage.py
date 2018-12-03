import yaml
from appLogging.logger import CustomLogger


class SynonymsStore:

    def __init__(self):
        self._doRead(self._loadYaml)

    def getFullName(self, shortName):
        if shortName in self._yaml:
            return self._yaml[shortName]
        else:
            return None

    def append(self, shortName, fullName):
        self.__yaml[shortName] = fullName
        self._doWrite(self._saveYaml)

    def _get_yaml(self):
        return self.__yaml

    def _set_yaml(self, y):
        self.__yaml = y

    _yaml = property(_get_yaml, _set_yaml)

    _logger = CustomLogger()



    def _loadYaml(self, stream):
        self._yaml = yaml.load(stream)
        self._logger.debug(self._yaml)

    def _saveYaml(self, stream):
        yaml.dump(self._yaml, stream)

    def _do(self, action, fileMode):
        with open("synonyms.yaml", fileMode) as stream:
            try:
                action(stream)
            except yaml.YAMLError as exc:
                self._logger.error(exc)

    def _doRead(self, action):
        self._do(action, 'r')

    def _doWrite(self, action):
        self._do(action, 'w')