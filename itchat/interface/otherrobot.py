# encoding=utf8


import urllib2



def get_moli_answer(question):
    """
    调用茉莉机器人
    :param question:
    :return:
    """
    print '---------get_moli_answer start-----------'
    print 'question:%s' % question
    url = 'http://i.itpk.cn/api.php?question=' + question
    req = urllib2.Request(url)
    # req.add_header('IAF',abc.token_authiaas)
    try:
        resp = urllib2.urlopen(req)
    except urllib2.HTTPError, error:
        print "CALL MOLIROBOT ERR!", error

    response = resp.read()
    print 'response:%s' % response
    print '---------get_moli_answer end-----------'
    return response

