# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import re
import  time
import itchat
from itchat.content import *

import TuringAPI as TA


#@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])
#def text_reply(msg):
#    message_a_reply=TA.reply_turing(msg.text)
    #while True:
    #time.sleep(0.2)
    #print(msg['FromUserName'])
 #   print(message_a_reply)
 #   itchat.send(message_a_reply,toUserName=msg['FromUserName'])
    #print msg['FromUserName']

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    msg.user.send('%s' % (TA.reply_turing(msg.text)))

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        msg.user.send(u'@%s\u2005I  %s' % (
            msg.actualNickName, TA.reply_turing(msg.text)))

itchat.auto_login(True)
itchat.run(True)



