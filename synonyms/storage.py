import yaml
from appLogging.logger import CustomLogger


class SynonymsStore:

    _logger = CustomLogger()

    def __init__(self, yamlPath):
        self._yamlPath = yamlPath
        if yamlPath is not None:
            self._doRead(self._loadYaml)

    def getFullName(self, shortName):
        if shortName in self._yaml:
            return self._yaml[shortName]
        else:
            return None

    def getAllValues(self):
        return self._yaml.values()

    def append(self, shortName, fullName):
        self._yaml[shortName] = fullName
        self._doWrite(self._saveYaml)

    def _loadYaml(self, stream):
        self._yaml = yaml.load(stream)
        self._logger.debug(self._yaml)

    def _saveYaml(self, stream):
        yaml.dump(self._yaml, stream)

    def _do(self, action, fileMode):
        with open(self._yamlPath, fileMode) as stream:
            try:
                action(stream)
            except yaml.YAMLError as exc:
                self._logger.error(exc)

    def _doRead(self, action):
        self._do(action, 'r')

    def _doWrite(self, action):
        self._do(action, 'w')