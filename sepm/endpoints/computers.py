import urllib

class Computers(object):
    def __init__(self, session):
        super(Computers, self).__init__()
        self._session = session

    def getComputers(self, **kwargs):
        metadata = {
            'tags':['computers', 'configure'],
            'operation': 'getComputers'
        }

        resource = f'/computers'

        params = {k.strip(): v for k, v in kwargs.items()}

        return self._session.get(metadata, resource, params)


