import json
from pathlib import Path

class accessFiles():
    def __init__(self):
        self.path = Path(__file__).cwd()

    def fileCV(self):
        tmpFile = self.path / "api/dal/files/cv.json"

        with open(tmpFile, 'r') as cvJson:
            dataCvJson = json.load(cvJson)
        cvJson.close()
        return dataCvJson
