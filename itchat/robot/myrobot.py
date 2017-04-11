# encoding=utf8
import json

import itchat, time
from itchat.content import *

from interface.otherrobot import get_moli_answer

# get_moli_answer('你好！')

# 全局变量
global cur_robot_xiaobin  # 是否使用小冰机器人
cur_robot_xiaobin = True
global answer_xiaobin  # 全局小冰回复
answer_xiaobin = ''
global pre_asker  # 全局提问人
pre_asker = ''


def fill_answer_names(answer_str, question_user_name, answer_user_name=u'凯'):
    # print answer_str, type(answer_str)
    # answer_str = answer_str.decode("UTF-8")
    answer_str = answer_str.replace('[name]', question_user_name.encode("UTF-8"))
    answer_str = answer_str.replace('[cqname]', answer_user_name.encode("UTF-8"))
    # print answer_str, type(answer_str)
    return answer_str





@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    print '------download_files start------'
    msg['Text'](msg['FileName'])
    if cur_robot_xiaobin:
        get_xiaobin_file_answer(msg)
        # itchat.send('@img@%s' % 'scissors.gif', msg['FromUserName'])
    else:
        # itchat.send(u'%s' % answer.decode("UTF-8"), msg['FromUserName'])
        itchat.send('@img@%s' % 'scissors.gif', msg['FromUserName'])
    print '------download_files end------'
    # return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def download_files(msg):
    print '------download_files start------'
    msg['Text'](msg['FileName'])
    if cur_robot_xiaobin:
        get_xiaobin_file_answer(msg)
        # itchat.send('@img@%s' % 'scissors.gif', msg['FromUserName'])
    else:
        # itchat.send(u'%s' % answer.decode("UTF-8"), msg['FromUserName'])
        itchat.send('@img@%s' % 'scissors.gif', msg['FromUserName'])
    print '------download_files end------'
    # return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isMpChat=True)
def download_files(msg):
    print '------download_files start------'
    msg['Text'](msg['FileName'])
    if cur_robot_xiaobin:
        get_xiaobin_file_answer(msg)
        # get_xiaobin_answer(msg)
        # itchat.send('@img@%s' % 'scissors.gif', msg['FromUserName'])
    else:
        # itchat.send(u'%s' % answer.decode("UTF-8"), msg['FromUserName'])
        itchat.send('@img@%s' % 'scissors.gif', msg['FromUserName'])
    print '------download_files end------'
    # return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    print '------text_reply start-------'
    print json.dumps(msg, ensure_ascii=False)
    question = msg['Text']
    question_user_name = msg['User']['NickName']
    question = question.encode("UTF-8")
    if cur_robot_xiaobin:
        get_xiaobin_answer(msg)
    else:
        answer_str = get_moli_answer(question)
        answer = fill_answer_names(answer_str, question_user_name, u'凯')
        itchat.send(u'%s' % answer.decode("UTF-8"), msg['FromUserName'])
    # itchat.send(u'%s' % msg['Content'], msg['FromUserName'])
    print '------text_reply end-------'


@itchat.msg_register(TEXT, isGroupChat=True)
def group_reply(msg):
    print '------group_reply start-------'
    print json.dumps(msg, ensure_ascii=False)
    question = msg['Text']
    question_user_name = msg['User']['NickName']
    question = question.encode("UTF-8")
    if cur_robot_xiaobin:
        get_xiaobin_answer(msg)
    else:
        answer_str = get_moli_answer(question)
        answer = fill_answer_names(answer_str, question_user_name, u'凯')
        itchat.send(u'%s' % answer.decode("UTF-8"), msg['FromUserName'])
    # itchat.send(u'%s' % msg['Content'], msg['FromUserName'])
    print '------group_reply end-------'


@itchat.msg_register(TEXT, isMpChat=True)
def mpchat_reply(msg):
    print '------mpchat_reply start-------'
    print json.dumps(msg, ensure_ascii=False)
    question = msg['Text']
    question_user_name = msg['User']['NickName']
    question = question.encode("UTF-8")

    if cur_robot_xiaobin:
        get_xiaobin_answer(msg)
    else:
        answer_str = get_moli_answer(question)
        answer = fill_answer_names(answer_str, question_user_name, u'凯')
        itchat.send(u'%s' % answer.decode("UTF-8"), msg['FromUserName'])
    # itchat.send(u'%s' % msg['Content'], msg['FromUserName'])
    print '------group_reply end-------'


def robot_run():
    # 登录
    itchat.auto_login(hotReload=True)

    # 向文件传输助手发送消息
    itchat.send('login', toUserName='filehelper')  # 发消息文件传输助手
    itchat.send('oK', toUserName='liukai13545872077')  # 发消息liukai

    itchat.run()


def get_xiaobin_answer(msg):
    """
    调用小冰机器人
    :param question:
    :return:
    """
    print '------get_xiaobin_answer start-------'
    global cur_robot_xiaobin
    global pre_asker
    global answer_xiaobin
    time.sleep(3)
    if msg['User']['Alias'] == 'xiaoice-ms':
        answer_xiaobin = msg['Text'].replace(u'小冰', u'凯')
        itchat.send(answer_xiaobin, pre_asker)
    else:
        itchat.send(msg['Text'], toUserName='xiaoice-ms')
        pre_asker = msg['FromUserName']
        print 'ask xiaobin:%s ,from %s' % (msg['Text'], pre_asker)
    print '------get_xiaobin_answer end-------'


def get_xiaobin_file_answer(msg):
    """
    发送附件给小冰机器人
    :param question:
    :return:
    """
    print '------get_xiaobin_file_answer start-------'
    global cur_robot_xiaobin
    global pre_asker
    global answer_xiaobin
    time.sleep(3)
    # if msg['User']['Alias'] == 'xiaoice-ms':
    if msg['User'].get('Alias', '') == 'xiaoice-ms':
        answer_xiaobin = '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])
        itchat.send(answer_xiaobin, pre_asker)
    else:
        question = '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])
        itchat.send(question, toUserName='xiaoice-ms')
        pre_asker = msg['FromUserName']
        print 'ask xiaobin:%s ,from %s' % (question, pre_asker)
    print '------get_xiaobin_file_answer end-------'

# itchat.send('@img@%s' % 'scissors.gif', msg['FromUserName'])
# return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])
robot_run()

