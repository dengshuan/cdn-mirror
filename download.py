#!/usr/bin/env python
import urllib
import json
import os, errno

with open('ajax.googleapis.com.json', 'r') as f:
    json_data = json.load(f)
    
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

for key in json_data.keys():
    lib = json_data[key]
    if type(lib['url']) == list:
        for u in lib['url']:
            default_version = u.split('/')[4]
            for version in lib['versions']:
                path = u.replace(default_version, version)
                url = 'http://' + path
                directory = path.rpartition('/')[0]
                mkdir_p(directory)
                print 'Retrieve {}'.format(url)
                urllib.urlretrieve(url, path)

    else:
        u = lib['url']
        default_version = u.split('/')[4]
        for version in lib['versions']:
            path = u.replace(default_version, version)
            url = 'http://' + path
            directory = path.rpartition('/')[0]
            mkdir_p(directory)
            print 'Retrieve {}'.format(url)
            urllib.urlretrieve(url, path)
