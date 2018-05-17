import requests
import time
import hashlib

BASE_URL = 'https://rjygfdoa.api.lncldapi.com/1.1/'
# BASE_URL = 'https://api.leancloud.cn/1.1/'


def init_class():
    pass


def get_sign(app_key):
    timestamp = get_timestamp()
    return "%s,%s" % (get_md5("%d%s" % (timestamp, app_key)), timestamp)


def get_timestamp():
    return int(time.time() * 1000)


def get_md5(str):
    hash_md5 = hashlib.md5(str)
    return hash_md5.hexdigest()


def get_id_key(wf):
    app_id = wf.stored_data('app_id')
    app_key = wf.stored_data('app_key')
    return app_id, app_key


def get_headers(app_id, app_key):
    return {'X-LC-Id': app_id, 'X-LC-Sign': get_sign(app_key), 'Content-Type': 'application/json'}


def post_request(app_id, app_key, url, data):
    r = requests.post(BASE_URL + url, json=data,
                      headers=get_headers(app_id, app_key))
    return r.json()


def get_request(app_id, app_key, url, params=None):
    r = requests.get(BASE_URL + url, params=params,
                     headers=get_headers(app_id, app_key))
    return r.json()


def delete_img_request(delete):
    r = requests.get(delete)
    return r.text


def delete_request(app_id, app_key, url):
    r = requests.delete(BASE_URL + url, headers=get_headers(app_id, app_key))
    return r.json()


def save_url(url, delete, wf):
    app_id, app_key = get_id_key(wf)
    if app_id and app_key:
        data = {u'url': url, u'delete': delete}
        post_request(app_id, app_key, u'classes/image', data)


def get_list(wf):
    app_id, app_key = get_id_key(wf)
    if app_id and app_key:
        params = {u'order': u'-createdAt'}
        result = get_request(app_id, app_key, u'classes/image', params=params)
        return result[u'results']


def get_delete_list(wf, delete):
    app_id, app_key = get_id_key(wf)
    if app_id and app_key:
        params = {u'where': u'{"delete":"%s"}' % delete}
        result = get_request(app_id, app_key, u'classes/image', params=params)
        return result[u'results']


def delete_url(wf, object_id, delete):
    app_id, app_key = get_id_key(wf)
    delete_img_request(delete)
    if app_id and app_key:
        return delete_request(app_id, app_key, u'classes/image/'+object_id)
