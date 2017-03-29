# encoding=utf8

import itchat, time
from itchat.content import *


# 回复发给自己的消息
# import itchat
#
# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     return msg['Text']
#
# itchat.auto_login()
# itchat.run()

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    print 'text_reply start'
    itchat.send(u'这里是自动回复%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])
    print u'这里是自动回复%s,%s,%s' % (msg['Type'], msg['Text'], msg['FromUserName'])
    # itchat.send(u'%s' % msg['Content'], msg['FromUserName'])
    print msg


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    print 'download_files start'
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    print 'add_friend start'
    itchat.add_friend(**msg['Text'])  # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])


@itchat.msg_register(TEXT, isGroupChat=True)
def groupchat_reply(msg):
    print 'text_reply start'
    # 判断是否@本号
    if msg['isAt']:
        itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])
    else:
        itchat.send(u'[自动回复]@%s 群发: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])
    print u'群%s,%s,%s' % (msg['ActualNickName'], msg['Content'], msg['FromUserName'])
    print msg


# 最简单的回复 通过如下代码，可以完成回复所有文本信息（包括群聊
@itchat.msg_register
def simple_reply(msg):
    print 'simple_reply start'
    if msg['Type'] == TEXT:
        return u'[自动回复]I received: %s' % msg['Content']
    print msg


# 登录
itchat.auto_login(hotReload=True)

# 向文件传输助手发送消息
itchat.send('Hello, filehelper', toUserName='filehelper')  # 发消息文件传输助手
itchat.send(u'发个消息试试', toUserName='liukai003201')  # 发消息自己，toUserName为None时，默认发给自己
itchat.send(u'你好！', toUserName='game')  # 发给公众号
# itchat.send(u'你好，武汉！', toUserName='cmccwh')  # 发给订阅号
itchat.send(u'你好么！', toUserName='xiaoice-ms')  # 发给机器人


# 获取联系人，还有其它信息在itchat.get_contact里面待研究
def lk_get_contact():
    contact = itchat.get_contact
    # print contact.im_self.chatroomList[0]
    # print contact.im_self.memberList[0]
    for member in contact.im_self.memberList:
        print str(member)


# 请确保该程序目录下存在：gz.gif以及xlsx.xlsx,toUserName=None时，为发送给自己
def lk_send_file():
    # itchat.send('@img@%s' % 'gz.gif',toUserName=None)
    itchat.send('@img@%s' % 'gz.gif')
    itchat.send('@fil@%s' % 'xlsx.xlsx')
    itchat.send('@vid@%s' % 'demo.mp4')


# 未来得急测试的方法
def lk_no_test():
    # 获取好友列表
    itchat.get_friends

    # 获取自己的用户信息，返回自己的属性字典
    itchat.search_friends()
    # 获取特定UserName的用户信息
    itchat.search_friends(userName='@abcdefg1234567')
    # 获取任何一项等于name键值的用户
    itchat.search_friends(name='littlecodersh')
    # 获取分别对应相应键值的用户
    itchat.search_friends(wechatAccount='littlecodersh')
    # 三、四项功能可以一同使用
    itchat.search_friends(name='LittleCoder机器人', wechatAccount='littlecodersh')

    # 获取特定UserName的公众号，返回值为一个字典
    itchat.search_mps(userName='@abcdefg1234567')
    # 获取名字中含有特定字符的公众号，返回值为一个字典的列表
    itchat.search_mps(name='LittleCoder')
    # 以下方法相当于仅特定了UserName
    itchat.search_mps(userName='@abcdefg1234567', name='LittleCoder')

    # 查询所有联系人
    aaa = itchat.get_friends
    # 查询所有好友
    for each in aaa.im_self.memberList:
        print each
        for k, v in each.items():
            print k, '=', v
    # 查询所有群
    for each in aaa.im_self.chatroomList:
        print each
        for k, v in each.items():
            print k, '=', v
    # 查询所有公众号
    for each in aaa.im_self.mpList:
        print each
        for k, v in each.items():
            print k, '=', v
    # 查询所有消息列表
    for each in aaa.im_self.msgList:
        print each
        for k, v in each.items():
            print k, '=', v



# 样例
def signin():
    # 查找公众号，进行签到
    user = itchat.search_mps(name='Nulll.me')
    UserName = user[0]['UserName']
    itchat.send(msg=u'3', toUserName=UserName)
    itchat.dump_login_status()
    # pickleDumps('flag', localDay)  # 如果执行成功写入标致文件
    exit()


def find_group_sendmsg():
    # 查找群，并发送消息,已测试通过（刘凯）
    print 'find_group_sendmsg start'
    user = itchat.search_chatrooms(name=u'新技术交流小组')
    username = user[0]['UserName']
    print username
    itchat.send(msg=u'test', toUserName=username)
    itchat.dump_login_status()
    # pickleDumps('flag', localDay)  # 如果执行成功写入标致文件


itchat.run()
