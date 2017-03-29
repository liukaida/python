# encoding=utf8

import itchat, time
from itchat.content import *

from interface.otherrobot import get_moli_answer

get_moli_answer('你好！')


def fill_answer_names(answer_str, question_user_name, answer_user_name=u'凯'):
    # print answer_str, type(answer_str)
    # answer_str = answer_str.decode("UTF-8")
    answer_str = answer_str.replace('[name]', question_user_name.encode("UTF-8"))
    answer_str = answer_str.replace('[cqname]', answer_user_name.encode("UTF-8"))
    # print answer_str, type(answer_str)
    return answer_str


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    print '------text_reply start-------'
    question = msg['Text']
    question_user_name = msg['User']['NickName']
    question = question.encode("UTF-8")
    answer_str = get_moli_answer(question)
    answer = fill_answer_names(answer_str, question_user_name, u'凯')
    itchat.send(u'%s' % answer.decode("UTF-8"), msg['FromUserName'])
    # itchat.send(u'%s' % msg['Content'], msg['FromUserName'])
    print '------text_reply end-------'
    print msg


def robot_run():
    # 登录
    itchat.auto_login(hotReload=True)

    # 向文件传输助手发送消息
    itchat.send('login', toUserName='filehelper')  # 发消息文件传输助手

    itchat.run()


robot_run()
