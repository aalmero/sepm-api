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
