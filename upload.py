import requests

SMMS_URL = "https://sm.ms/api/upload"


def upload_smms(path, upload_name):
    smfile = {'smfile': open(path, 'rb')}
    r = requests.post(SMMS_URL, files=smfile)
    result = r.json()
    if result['code'] == 'success':
        url = result['data']['url']
        delete = result['data']['delete']
        return url, delete
    else:
        return False, False
