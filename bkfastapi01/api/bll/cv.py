from api.dal.accessFiles import accessFiles

class cv():
    def __init__(self):
        self.accessFiles = accessFiles()



#mapper zone

    def get_cvs(self):
        return self.accessFiles.fileCV()
