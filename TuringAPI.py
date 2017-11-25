# # encoding=utf8
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import requests
def reply_turing(message):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : '61a109ce6aba453fb8a6820f4bddd9cc', #
        'info'   : message, # here is the message we will send to the server
        'userid' : '117820', # we can changge the name here
    }
    # 我们通过如下命令发送一个post请求
    r = requests.post(apiUrl, data=data).json()

    # we can see the message here
    print(message)
    print(r.get('text'))
    return  r.get('text')
