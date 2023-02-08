import urllib

class Computers(object):
    def __init__(self, session):
        super(Computers, self).__init__()
        self._session = session

    def getComputers(self):
        metadata = {
            'tags':['computers', 'configure'],
            'operation': 'getComputers'
        }

        resource = f'/computers'

        return self._session.get(metadata, resource)

    def getComputer(self, computerName: str):
        metadata = {
            'tags':['computer', 'configure'],
            'operation': 'getComputer'
        }

        computerName = urllib.parse.quote(str(computerName), safe='')
        resource = f'/computers/?computerName={computerName}'

        return self._session.get(metadata, resource)
