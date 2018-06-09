import math
import re


def mydata(my1, my2):
    #  my1="+CGPSINFO: 2242.484940,N,12021.608459,E,150518,101255.0,,54.6,180.4"
    #  my2="+CGPSINFO: 2242.559644,N,12021.609622,E,150518,101250.0,,51.1,179.6"
    #  my1:第二次座標 my2:第一次座標
    mylast = []
    mynext = []
    mylastGPS = ''
    mynextGPS = ''
    a = my2.find(" ")
    b = my2.find("N", 10)
    c = my2.find("E")
    for i in range(a + 1, b - 1):
        mylastGPS = mylastGPS + my2[i]
    mylastGPS = mylastGPS + ","
    for j in range(b + 2, c - 1):
        mylastGPS = mylastGPS + my2[j]
    mylastGPS = mylastGPS + ","
    for k in range(c + 9, c + 15):
        mylastGPS = mylastGPS + my2[k]
    a = my1.find(" ")
    b = my1.find("N", 10)
    c = my1.find("E")
    for i in range(a + 1, b - 1):
        mynextGPS = mynextGPS + my1[i]
    mynextGPS = mynextGPS + ","
    for j in range(b + 2, c - 1):
        mynextGPS = mynextGPS + my1[j]
    mynextGPS = mynextGPS + ","
    for k in range(c + 9, c + 15):
        mynextGPS = mynextGPS + my1[k]
    mylastdata = re.findall(r'\d+', mylastGPS)
    mynextdata = re.findall(r'\d+', mynextGPS)
    if (len(mylastdata) != 5 or len(mynextdata) != 5
            or (mylastdata[4] == mynextdata[4])):
        s = -1
        f = ''
    elif (len(mylastdata) == 5 or len(mynextdata) == 5):
        t = mylastdata[0] + '.' + mylastdata[1]
        if len(mylastdata[0]) < 3:
            anlast = float(t) / 60
        elif len(mylastdata[0]) == 3:
            anlast = float(t[0]) + float(t[1:]) / 60
        elif len(mylastdata[0]) == 4:
            anlast = float(t[0:2]) + float(t[2:]) / 60
        elif len(mylastdata[0]) == 5:
            anlast = float(t[0:3]) + float(t[3:]) / 60
        mylast.insert(0, anlast)
        t = mylastdata[2] + '.' + mylastdata[3]
        if len(mylastdata[2]) < 3:
            aelast = float(t) / 60
        elif len(mylastdata[2]) == 3:
            aelast = float(t[0]) + float(t[1:]) / 60
        elif len(mylastdata[2]) == 4:
            aelast = float(t[0:2]) + float(t[2:]) / 60
        elif len(mylastdata[2]) == 5:
            aelast = float(t[0:3]) + float(t[3:]) / 60
        mylast.insert(1, aelast)
        t = mynextdata[0] + '.' + mynextdata[1]
        if len(mynextdata[0]) < 3:
            annext = float(t) / 60
        elif len(mynextdata[0]) == 3:
            annext = float(t[0]) + float(t[1:]) / 60
        elif len(mynextdata[0]) == 4:
            annext = float(t[0:2]) + float(t[2:]) / 60
        elif len(mynextdata[0]) == 5:
            annext = float(t[0:3]) + float(t[3:]) / 60
        mynext.insert(0, annext)
        t = mynextdata[2] + '.' + mynextdata[3]
        if len(mynextdata[2]) < 3:
            aenext = float(t) / 60
        elif len(mynextdata[2]) == 3:
            aenext = float(t[0]) + float(t[1:]) / 60
        elif len(mynextdata[2]) == 4:
            aenext = float(t[0:2]) + float(t[2:]) / 60
        elif len(mynextdata[2]) == 5:
            aenext = float(t[0:3]) + float(t[3:]) / 60
        mynext.insert(1, aenext)
        t1 = mylastdata[4]
        t2 = mynextdata[4]
        if int(t2[4:]) > int(t1[4:]):
            z = int(t2[4:]) - int(t1[4:])
        elif int(t2[4:]) < int(t1[4:]):
            z = int(t2[4:]) + 60 - int(t1[4:])
        x = float(mylast[0]) - float(mynext[0])
        y = float(mylast[1]) - float(mynext[1])
        xk = x * 111
        yk = y * 111
        d = math.sqrt(xk**2 + yk**2)
        s = round((d / z) * 3600, 3)
        if mynext[1] - mylast[1] == 0 and mynext[0] - mylast[0] != 0:
            if mynext[0] - mylast[0] > 0:
                f = '北'
            elif mynext[0] - mylast[0] < 0:
                f = '南'
        elif mynext[1] - mylast[1] == 0 and mynext[0] - mylast[0] == 0:
            f = '靜止'
        elif mynext[1] - mylast[1] != 0:
            if mynext[0] - mylast[0] > 0:
                if ((mynext[0] - mylast[0]) /
                    (mynext[1] - mylast[1])) >= 2.5 or (
                        (mynext[0] - mylast[0]) /
                        (mynext[1] - mylast[1])) <= -2.5:
                    f = '北'
                elif ((mynext[0] - mylast[0]) /
                      (mynext[1] - mylast[1])) > 0.5 and (
                          (mynext[0] - mylast[0]) /
                          (mynext[1] - mylast[1])) < 2.5:
                    f = '東北'
                elif ((mynext[0] - mylast[0]) /
                      (mynext[1] - mylast[1])) < 0.5 and (
                          (mynext[0] - mylast[0]) /
                          (mynext[1] - mylast[1])) >= 0:
                    f = '東'
                elif ((mynext[0] - mylast[0]) /
                      (mynext[1] - mylast[1])) < -0.5 and (
                          (mynext[0] - mylast[0]) /
                          (mynext[1] - mylast[1])) > -2.5:
                    f = '西北'
                elif ((mynext[0] - mylast[0]) /
                      (mynext[1] - mylast[1])) > -0.5 and (
                          (mynext[0] - mylast[0]) /
                          (mynext[1] - mylast[1])) <= 0:
                    f = '西'
            elif mynext[0] - mylast[0] < 0:
                if ((mynext[0] - mylast[0]) /
                    (mynext[1] - mylast[1])) >= 2.5 or (
                        (mynext[0] - mylast[0]) /
                        (mynext[1] - mylast[1])) <= -2.5:
                    f = '南'
                elif ((mynext[0] - mylast[0]) /
                      (mynext[1] - mylast[1])) > 0.5 and (
                          (mynext[0] - mylast[0]) /
                          (mynext[1] - mylast[1])) < 2.5:
                    f = '西南'
                elif (
                    (mynext[0] - mylast[0]) /
                    (mynext[1] - mylast[1])) < 0.5 and (
                        (mynext[0] - mylast[0]) / (mynext[1] - mylast[1])) > 0:
                    f = '西'
                elif ((mynext[0] - mylast[0]) /
                      (mynext[1] - mylast[1])) < -0.5 and (
                          (mynext[0] - mylast[0]) /
                          (mynext[1] - mylast[1])) > -2.5:
                    f = '東南'
                elif (
                    (mynext[0] - mylast[0]) /
                    (mynext[1] - mylast[1])) > -0.5 and (
                        (mynext[0] - mylast[0]) / (mynext[1] - mylast[1])) < 0:
                    f = '東'
    return s, f


def AMBdata(amb1, amb2):
    # t:暫存 ambd1:讀取amb1字串所有數字  ambd2:讀取amb2字串所有數字 an1:第一次輸入緯度 ae1:第一次輸入經度 an2:第二次輸入緯度 ae2:第二次輸入精度
    ambf = []
    ambl = []
    amba = ''
    ambb = ''
    a = amb1.find(" ")
    b = amb1.find("N", 10)
    c = amb1.find("E")
    for i in range(a + 1, b - 1):
        amba = amba + amb1[i]
    amba = amba + ","
    for j in range(b + 2, c - 1):
        amba = amba + amb1[j]
    amba = amba + ","
    for k in range(c + 9, c + 15):
        amba = amba + amb1[k]
    a = amb2.find(" ")
    b = amb2.find("N", 10)
    c = amb2.find("E")
    for i in range(a + 1, b - 1):
        ambb = ambb + amb2[i]
    ambb = ambb + ","
    for j in range(b + 2, c - 1):
        ambb = ambb + amb2[j]
    ambb = ambb + ","
    for k in range(c + 9, c + 15):
        ambb = ambb + amb2[k]
    ambd1 = re.findall(r'\d+', amba)
    ambd2 = re.findall(r'\d+', ambb)
    if (len(ambd1) != 5 or len(ambd2) != 5) or (ambd1[4] == ambd2[4]):
        s = -1
        f = ''
    elif len(ambd1) == 5 and len(ambd2) == 5:
        t = ambd1[0] + '.' + ambd1[1]
        if len(ambd1[0]) < 3:
            an1 = float(t) / 60
        elif len(ambd1[0]) == 3:  # 判斷緯度小於10
            an1 = float(t[0]) + float(t[1:]) / 60
        elif len(ambd1[0]) == 4:  # 判斷緯度小於100
            an1 = float(t[0:2]) + float(t[2:]) / 60
        elif len(ambd1[0]) == 5:  # 判斷緯度大於等於100
            an1 = float(t[0:3]) + float(t[3:]) / 60
        # an1=round(an1,5)
        ambf.insert(0, an1)
        t = ambd1[2] + '.' + ambd1[3]
        if len(ambd1[2]) < 3:
            ae1 = float(t) / 60
        elif len(ambd1[2]) == 3:  # 判斷經度小於10
            ae1 = float(t[0]) + float(t[1:]) / 60
        elif len(ambd1[2]) == 4:  # 判斷經度小於100
            ae1 = float(t[0:2]) + float(t[2:]) / 60
        elif len(ambd1[2]) == 5:  # 判斷經度大於等於100
            ae1 = float(t[0:3]) + float(t[3:]) / 60
        # ae1=round(ae1,5)
        ambf.insert(1, ae1)
        t = ambd2[0] + '.' + ambd2[1]
        if len(ambd2[0]) < 3:
            an2 = float(t) / 60
        elif len(ambd2[0]) == 3:  # 判斷緯度小於10
            an2 = float(t[0]) + float(t[1:]) / 60
        elif len(ambd2[0]) == 4:  # 判斷緯度小於100
            an2 = float(t[0:2]) + float(t[2:]) / 60
        elif len(ambd2[0]) == 5:  # 判斷緯度大於等於100
            an2 = float(t[0:3]) + float(t[3:]) / 60
        # an2=round(an2,5)
        ambl.insert(0, an2)
        t = ambd2[2] + '.' + ambd2[3]
        if len(ambd2[2]) < 3:
            ae2 = float(t) / 60
        elif len(ambd2[2]) == 3:  # 判斷經度小於10
            ae2 = float(t[0]) + float(t[1:]) / 60
        elif len(ambd2[2]) == 4:  # 判斷經度小於100
            ae2 = float(t[0:2]) + float(t[2:]) / 60
        elif len(ambd2[2]) == 5:  # 判斷經度大於等於100
            ae2 = float(t[0:3]) + float(t[3:]) / 60
        # ae2=round(ae2,5)
        ambl.insert(1, ae2)
        # t1,t2:暫存 z:時間差(秒) x:緯度差 y:經度差 xk:緯度差(公里) yk經度差(公里) d:距離(公里) s:速度(公里/時)
        t1 = ambd1[4]
        t2 = ambd2[4]
        if int(t1[4:]) > int(t2[4:]):
            z = int(t2[4:]) + 60 - int(t1[4:])
        elif int(t1[4:]) < int(t2[4:]):
            z = int(t2[4:]) - int(t1[4:])
        x = float(ambl[0]) - float(ambf[0])
        y = float(ambl[1]) - float(ambf[1])
        # x=round(float(ambf[0])-float(ambl[0]),6)
        # y=round(float(ambf[1])-float(ambl[1]),6)
        xk = x * 111
        yk = y * 111
        d = math.sqrt(xk**2 + yk**2)
        # d=round(math.sqrt(xk**2+yk**2),2)
        s = round((d / z) * 3600, 3)
        if ambf[1] - ambl[1] == 0 and ambf[0] - ambl[0] != 0:
            if ambf[0] - ambl[0] > 0:
                f = '北'
            elif ambf[0] - ambl[0] < 0:
                f = '南'
        elif ambf[1] - ambl[1] != 0:
            if ambf[0] - ambl[0] > 0:
                if ((ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) >= 2.5 or (
                    (ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) <= -2.5:
                    f = '北'
                elif ((ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) > 0.5 and (
                    (ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) < 2.5:
                    f = '東北'
                elif ((ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) < 0.5 and (
                    (ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) >= 0:
                    f = '東'
                elif ((ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) < -0.5 and (
                    (ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) > -2.5:
                    f = '西北'
                elif ((ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) > -0.5 and (
                    (ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) <= 0:
                    f = '西'
            elif ambf[0] - ambl[0] < 0:
                if ((ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) >= 2.5 or (
                    (ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) <= -2.5:
                    f = '南'
                elif ((ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) > 0.5 and (
                    (ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) < 2.5:
                    f = '西南'
                elif ((ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) < 0.5 and (
                    (ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) > 0:
                    f = '西'
                elif ((ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) < -0.5 and (
                    (ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) > -2.5:
                    f = '東南'
                elif ((ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) > -0.5 and (
                    (ambf[0] - ambl[0]) / (ambf[1] - ambl[1])) < 0:
                    f = '東'
        elif ambf[1] - ambl[1] == 0 and ambf[0] - ambl[0] == 0:
            f = '靜止'
    return s, f


def AMBandmy(my1, amb1):
    myf = []
    ambf = []
    mya = ''
    amba = ''
    a = my1.find(" ")
    b = my1.find("N", 10)
    c = my1.find("E")
    for i in range(a + 1, b - 1):
        mya = mya + my1[i]
    mya = mya + ","
    for j in range(b + 2, c - 1):
        mya = mya + my1[j]
    mya = mya + ","
    for k in range(c + 9, c + 15):
        mya = mya + my1[k]
    a = amb1.find(" ")
    b = amb1.find("N", 10)
    c = amb1.find("E")
    for i in range(a + 1, b - 1):
        amba = amba + amb1[i]
    amba = amba + ","
    for j in range(b + 2, c - 1):
        amba = amba + amb1[j]
    amba = amba + ","
    for k in range(c + 9, c + 15):
        amba = amba + amb1[k]
    myd1 = re.findall(r'\d+', mya)
    ambd1 = re.findall(r'\d+', amba)
    if len(myd1) != 5 or len(ambd1) != 5:
        d = -1
        f = ''
    elif len(myd1) == 5 and len(ambd1) == 5:
        t = myd1[0] + '.' + myd1[1]
        if len(myd1[0]) < 3:
            an1 = float(t) / 60
        elif len(myd1[0]) == 3:  # 判斷緯度小於10
            an1 = float(t[0]) + float(t[1:]) / 60
        elif len(myd1[0]) == 4:  # 判斷緯度小於100
            an1 = float(t[0:2]) + float(t[2:]) / 60
        elif len(myd1[0]) == 5:  # 判斷緯度大於等於100
            an1 = float(t[0:3]) + float(t[3:]) / 60
        # an1=round(an1,5)
        myf.insert(0, an1)
        t = myd1[2] + '.' + myd1[3]
        if len(myd1[2]) < 3:
            an1 = float(t) / 60
        elif len(myd1[2]) == 3:  # 判斷經度小於10
            ae1 = float(t[0]) + float(t[1:]) / 60
        elif len(myd1[2]) == 4:  # 判斷經度小於100
            ae1 = float(t[0:2]) + float(t[2:]) / 60
        elif len(myd1[2]) == 5:  # 判斷經度大於等於100
            ae1 = float(t[0:3]) + float(t[3:]) / 60
        # ae1=round(ae1,5)
        myf.insert(1, ae1)
        t = ambd1[0] + '.' + ambd1[1]
        if len(ambd1[0]) < 3:
            an1 = float(t) / 60
        elif len(ambd1[0]) == 3:  # 判斷緯度小於10
            an2 = float(t[0]) + float(t[1:]) / 60
        elif len(ambd1[0]) == 4:  # 判斷緯度小於100
            an2 = float(t[0:2]) + float(t[2:]) / 60
        elif len(ambd1[0]) == 5:  # 判斷緯度大於等於100
            an2 = float(t[0:3]) + float(t[3:]) / 60
        # an2=round(an2,5)
        ambf.insert(0, an2)
        t = ambd1[2] + '.' + ambd1[3]
        if len(ambd1[2]) < 3:
            an1 = float(t) / 60
        elif len(ambd1[2]) == 3:  # 判斷經度小於10
            ae2 = float(t[0]) + float(t[1:]) / 60
        elif len(ambd1[2]) == 4:  # 判斷經度小於100
            ae2 = float(t[0:2]) + float(t[2:]) / 60
        elif len(ambd1[2]) == 5:  # 判斷經度大於等於100
            ae2 = float(t[0:3]) + float(t[3:]) / 60
        # ae2=round(ae2,5)
        ambf.insert(1, ae2)
        # x:緯度差 y:經度差 xk:緯度差(公尺) yk經度差(公尺) d:距離(公尺)
        x = float(myf[0]) - float(ambf[0])
        y = float(myf[1]) - float(ambf[1])
        # x=round(float(myf[0])-float(ambf[0]),6)
        # y=round(float(myf[1])-float(ambf[1]),6)
        xm = x * 111000
        ym = y * 111000
        d = round(math.sqrt(xm**2 + ym**2), 3)

        if myf[1] - ambf[1] == 0 and myf[0] - ambf[0] != 0:
            if myf[0] - ambf[0] > 0:
                f = '北'
            elif myf[0] - ambf[0] < 0:
                f = '南'
        elif myf[1] - ambf[1] != 0:
            if myf[0] - ambf[0] > 0:
                if ((myf[0] - ambf[0]) / (myf[1] - ambf[1])) >= 2.5 or (
                    (myf[0] - ambf[0]) / (myf[1] - ambf[1])) <= -2.5:
                    f = '北'
                elif ((myf[0] - ambf[0]) / (myf[1] - ambf[1])) > 0.5 and (
                    (myf[0] - ambf[0]) / (myf[1] - ambf[1])) < 2.5:
                    f = '東北'
                elif ((myf[0] - ambf[0]) / (myf[1] - ambf[1])) < 0.5 and (
                    (myf[0] - ambf[0]) / (myf[1] - ambf[1])) >= 0:
                    f = '東'
                elif ((myf[0] - ambf[0]) / (myf[1] - ambf[1])) < -0.5 and (
                    (myf[0] - ambf[0]) / (myf[1] - ambf[1])) > -2.5:
                    f = '西北'
                elif ((myf[0] - ambf[0]) / (myf[1] - ambf[1])) > -0.5 and (
                    (myf[0] - ambf[0]) / (myf[1] - ambf[1])) <= 0:
                    f = '西'
            elif myf[0] - ambf[0] < 0:
                if ((myf[0] - ambf[0]) / (myf[1] - ambf[1])) >= 2.5 or (
                    (myf[0] - ambf[0]) / (myf[1] - ambf[1])) <= -2.5:
                    f = '南'
                elif ((myf[0] - ambf[0]) / (myf[1] - ambf[1])) > 0.5 and (
                    (myf[0] - ambf[0]) / (myf[1] - ambf[1])) < 2.5:
                    f = '西南'
                elif ((myf[0] - ambf[0]) / (myf[1] - ambf[1])) < 0.5 and (
                    (myf[0] - ambf[0]) / (myf[1] - ambf[1])) > 0:
                    f = '西'
                elif ((myf[0] - ambf[0]) / (myf[1] - ambf[1])) < -0.5 and (
                    (myf[0] - ambf[0]) / (myf[1] - ambf[1])) > -2.5:
                    f = '東南'
                elif ((myf[0] - ambf[0]) / (myf[1] - ambf[1])) > -0.5 and (
                    (myf[0] - ambf[0]) / (myf[1] - ambf[1])) < 0:
                    f = '東'
        elif myf[1] - ambf[1] == 0 and myf[0] - ambf[0] == 0:
            f = '無'
    return d, f
