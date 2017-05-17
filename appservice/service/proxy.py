# -*- coding:utf-8 -*-
'''
Created on 2017年5月17日

@author: chuangzl
'''

import web
import json
import uuid
import sys
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

urls = (
    '/proxy', 'proxy'
)

app = web.application(urls, globals())

class proxy:
    def GET(selfs):
        #web.header('content-type','text/json')
        get = web.ctx.get
        status = web.ctx.status
        print get
        print status

        #return_str = str(endpoint_json)
        #return_str = return_str.replace("'", "\"");
        return "ok"
    
if __name__ == '__main__':
    app.run()