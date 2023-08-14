import datetime
import pyautogui as auto
import subprocess
import win32api
import time
import os, sys

def click4Game(auto,imageName,inputStr):
    time.sleep(0.5)
    sc = auto.screenshot()
    los = auto.locateOnScreen(imageName, grayscale=False)
    print(imageName,los)
    # print("los:",los)
    x, y=auto.center(los)  # 获得中心点
    auto.mouseDown(x, y)
    time.sleep(0.5)
    auto.mouseUp()
    # auto.click(x,y,clicks=6, interval=0.25)
    # time.sleep(2)
    if inputStr != "":
        auto.typewrite(inputStr, interval=0.25)
    return;

def rightClick4Game(auto,imageName,inputStr):
    time.sleep(0.5)
    sc = auto.screenshot()
    los = auto.locateOnScreen(imageName)
    # print(imageName)
    # print("los:",los)
    print(imageName, los)
    x, y=auto.center(los)  # 获得中心点
    auto.mouseDown(x, y,button='right')
    auto.mouseUp(x, y, button='right')
    # time.sleep(1)
    # auto.mouseUp()
    # auto.click(x,y,clicks=6, interval=0.25)
    # time.sleep(2)
    if inputStr != "":
        auto.typewrite(inputStr, interval=0.25)
    return;

def doubleClick4Game(auto,imageName,inputStr):
    time.sleep(0.5)
    sc = auto.screenshot()
    los = auto.locateOnScreen(imageName, grayscale=True)
    print(imageName, los)
    x, y= auto.center(los)  # 获得中心点
    auto.doubleClick(x, y)
    auto.doubleClick(x, y)
    time.sleep(1)
    if inputStr != "":
        auto.typewrite(inputStr, interval=0.25)
    return;

def clickOnDefaultXY():
    auto.mouseDown()
    time.sleep(0.5)
    auto.mouseUp()

def deleteFile(path):
    # 判断文件是否存在
    if (os.path.exists(path)):
        os.remove(path)
    else:
        print("要删除的文件不存在！")

def testCase1():
    testResult = 0;
    subprocess.Popen('taskkill /F /im ev.exe', shell=True,stdout=subprocess.PIPE)
    time.sleep(0.5)
    deleteFile("C:\\Users\\admin\\Documents\\新项目")
    time.sleep(0.5)
    prs=subprocess.Popen(["C:\\Program Files (x86)\\evkworld\\bin\\ev.exe"])
    time.sleep(5)
    # 初始化 删除旧项目文件C:\Users\admin\Documents
    print(auto.size())
    # click4Game(auto,'窗口最大化.png','')
    # time.sleep(2)
    # click4Game(auto,'更新取消.png','')
    # click4Game(auto,'密码登录.png','')
    #     # click4Game(auto,'账号.png','Helloworld')
    #     # click4Game(auto,'游客登录.png','')
    #     # click4Game(auto,'新建项目.png','')
    #     # click4Game(auto,'保存.png','')
    #     # click4Game(auto,'自定义.png','')
    #     # click4Game(auto,'1920_1080.png','')
    #     # click4Game(auto,'新建项目确认.png','')
    #     # click4Game(auto,'添加事件.png','')
    #     # click4Game(auto,'选中对象.png','')

    time.sleep(10)

    start = time.clock()
    click4Game(auto, '微信截图_20190621110218.png', '')
    # click4Game(auto, '新建项目.png', '')
    elapsed = (time.clock() - start)
    print("Time used:", elapsed)
    # click4Game(auto,'密码登录.png','')
    # click4Game(auto,'账号.png','Helloworld')
    # click4Game(auto,'游客登录.png','')
    # click4Game(auto,'新建项目.png','')
    # click4Game(auto,'保存.png','')
    # click4Game(auto,'自定义.png','')
    # click4Game(auto,'1920_1080.png','')
    # click4Game(auto,'新建项目确认.png','')
    # click4Game(auto,'新建可视对象.png','')
    # click4Game(auto,'添加对象-文本.png','')
    # click4Game(auto,'添加对象-确认.png', '')
    # rightClick4Game(auto,'添加对象-默认文本控件1.png', '')
    # click4Game(auto, '添加对象-重命名.png', '')
    # auto.typewrite('aaaaaaaaaa')
    # clickOnDefaultXY()
    # button7location = auto.locateOnScreen('对象名字缩略.png', grayscale=True)
    # print('button7location:',button7location)
    # click4Game(auto,'对象名字缩略.png','')
    # # auto.screenshot()
    # # time.sleep(2)
    # button8location = auto.locateOnScreen('新建对象-hover提示.png', grayscale=True)
    # print('button8location:',button8location)
    #
    # if button7location == None or button8location == None:
    #     print('test failure')
    # else:
    #     testResult=1
    # time.sleep(6)
    win32api.TerminateProcess(int(prs._handle), -1)
    return testResult
# sc = auto.screenshot()
# time.sleep(2)
# number7_location = auto.locateOnScreen('cancel.png')
# time.sleep(2)
# print("number7_location",number7_location)
#
# x,y = auto.center(number7_location)
# print(number7_location)
#
#
# click4Game(x, y)
# time.sleep(2)
# im = auto.screenshot()
#
# los=auto.locateOnScreen('密码登录.png')
# x2, y2 = auto.center(los)  # 获得中心点
# click4Game(x2, y2)
# time.sleep(2)
#
#
# los=auto.locateOnScreen('账号.png')
# x, y = auto.center(los)  # 获得中心点
# click4Game(x, y)
# auto.typewrite('Helloworld!', interval=0.25)

for i in range(1):
    try:
        testResult=testCase1()
    except:
        print('测试出错')
        # testCase1()world
        continue
    else:
        if testResult == 0:
            print('测试不通过')
        else:
            print('测试通过')
            break
    finally:
        pass
        # break


