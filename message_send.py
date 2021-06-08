import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import smtplib
from email.mime.text import MIMEText

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

pushPlusToken = 'XXXXXXXXXXXXXXX'
serverjSendkey = 'XXXXXXXXXXXXXXXx'
sendFromAddr = 'xxx@163.com'
sendFromPassword = 'XXXXXXXX'
neteaseSMTPServer = 'smtp.163.com'


def send_email_163(sendFromAddr, sendFromPassword, sendToAddr, smtpServer, emailSubject, emailMessage):
    """发送消息到目标邮箱

    Args:
            sendFromAddr ([str]): 发送者的邮箱
            sendFromPassword ([str]): 发送者邮箱密码
            sendToAddr ([str]): 接收者邮箱
            smtpServer ([str]): SMTP服务器
            message ([str]): 发送的消息
    Returns:
            [str]: 发送成功返回标题 发送失败返回None
    """

    try:
        mimeMessageText = MIMEText(
            _text=emailMessage, _subtype='plain', _charset='utf-8')
        mimeMessageText['Subject'] = emailSubject
        mimeMessageText['To'] = sendToAddr
        mimeMessageText['From'] = sendFromAddr

        server = smtplib.SMTP_SSL(smtpServer, 994)
        server.login(sendFromAddr, sendFromPassword)
        server.sendmail(sendFromAddr, [sendToAddr], mimeMessageText.as_string())
        server.close()
        return emailSubject
    except:
        return


def sendPushPlusOneInfo(title, info, template):
    """一对一通过PushPlus发送消息

    Args:
        title ([str]): 消息标题
        info ([str]): 消息体
        template ([str]): 消息模板 如json,text

    Returns:
        [str]: 发送成功返回标题 发送失败返回None
    """
    url = 'http://pushplus.hxtrip.com/send'
    headers = {'Content-Type': 'application/json'}
    data = {
        'token': pushPlusToken,
        'title': title,
        'content': info,
        'template': template
    }
    body = json.dumps(data).encode(encoding='utf-8')
    try:
        rep = requests.post(url=url, data=body, headers=headers)
        if rep.status_code == 200:
            return title
        else:
            return
    except:
        return


def sendPushPlusGroupInfo(title, info, template, groupID):
    """一对群组通过PushPlus发送消息

    Args:
        title ([str]): 消息标题
        info ([str]): 消息体
        template ([str]): 消息模板 如json,text
        groupID ([str]): 组号

    Returns:
        [str]: 发送成功返回标题 发送失败返回None
    """
    url = 'http://pushplus.hxtrip.com/send'
    headers = {'Content-Type': 'application/json'}
    data = {
        'token': pushPlusToken,
        'title': title,
        'content': info,
        'template': template,
        'topic': groupID
    }
    body = json.dumps(data).encode(encoding='utf-8')
    try:
        rep = requests.post(url=url, data=body, headers=headers)
        if rep.status_code == 200:
            return title
        else:
            return
    except:
        return


def sendServerJOneInfo(title, content):
    """ 一对一通过Server酱发送消息

    Args:
        title: 消息标题
        content: 消息体

    Returns: 发送成功返回标题 发送失败返回None

    """
    url = 'https://sctapi.ftqq.com/' + serverjSendkey + '.send'
    data = {
        'title': title,
        'desp': content
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'}
    try:
        requests.post(url=url, data=data)
        return title
    except:
        return


if __name__ == '__main__':
    sendEmail163 = send_email_163(sendFromAddr, sendFromPassword,
                                  '1971134857@qq.com', neteaseSMTPServer, 'CMACCKK', "Hello, I'm CMACCKK")
    if sendEmail163 is None:
        print('163邮箱信息发送失败')
    else:
        print('163邮箱信息发送成功 标题为{}'.format(sendEmail163))
    # sendServerJ = sendServerJOneInfo("test", "test")
    # if sendServerJ is None:
    #     print("Server酱信息发送失败")
    # else:
    #     print("Server酱信息发送成功{}".format("sendServerJ"))
    # sendPushPlusOne = sendPushPlusOneInfo('test', {'testOne': 'first', 'testTwo': 'second'}, 'json')
    # if sendPushPlusOne is None:
    #     print('PushPlus单人发送失败')
    # else:
    #     print('PushPlus单人发送成功 标题为{}'.format(sendPushPlusOne))
    # sendPushPlusGroup = sendPushPlusOneInfo('test', {'testGroupOne': 'first', 'testGroupTwo': 'second'}, 'json')
    # if sendPushPlusGroup is None:
    #     print('PushPlus群组发送失败')
    # else:
    #     print('PushPlus群组发送成功 标题为{}'.format(sendPushPlusGroup))