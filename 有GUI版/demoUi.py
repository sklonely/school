# -*- coding: utf-8 -*-
# import自動修復 程式碼片段Stste
lestModName = ""
err = ""
while 1:
    try:
        import sys
        import os
        # 要import的東西放這下面
        from PyQt5 import QtCore, QtGui, QtWidgets
        sys.path.append(sys.path[0] + '/mods/')  # 將自己mods的路徑加入倒python lib裡面
        import time
        import requests
        import httplib2
        import AT  # AT命令
        import googlesheet
        import final  # 車距計算
    except ModuleNotFoundError:  # python 3.5以上適用
        err = str(sys.exc_info()[1])[17:-1]
        if (lestModName != err):
            print("缺少mod: " + err + " 正在嘗試進行安裝")
            os.system("pip install " + err)
            lestModName = err
        else:
            print("無法修復import問題 請人工檢查", "mod name: " + err)
            sys.exit()
    except ImportError:  # python 3.5以下適用
        err = str(sys.exc_info()[1])[17:-1]
        if (lestModName != err):
            print("缺少mod: " + err + " 正在嘗試進行安裝")
            os.system("pip install " + err)
            lestModName = err
        else:
            print("無法修復import問題 請人工檢查", "mod name: " + err)
            sys.exit()
    else:
        del lestModName, err
        break
# import自動修復 程式碼片段


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # UI
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(779, 480)
        MainWindow.setWindowTitle("車聯網專題Demo視窗")
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAccessibleName("")
        MainWindow.setStyleSheet("")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 無邊框
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("border:2px;\n" "border-radius:15px")
        self.centralwidget.setObjectName("centralwidget")
        self.frame_10 = QtWidgets.QFrame(self.centralwidget)
        self.frame_10.setGeometry(QtCore.QRect(0, 0, 781, 491))
        self.frame_10.setAutoFillBackground(False)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.frame = QtWidgets.QFrame(self.frame_10)
        self.frame.setGeometry(QtCore.QRect(20, 20, 741, 131))
        self.frame.setStyleSheet("background-color:rgb(230,230,230,200)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 381, 81))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(40)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:rgb(255,255,255,0)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(410, 30, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Haettenschweiler")
        font.setPointSize(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:rgb(255,255,255,0)")
        self.label_4.setObjectName("label_4")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(990, 100, 1001, 131))
        self.frame_2.setStyleSheet("background-color:rgb(138,181,251)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3.raise_()
        self.label_4.raise_()
        self.frame_2.raise_()
        self.frame_3 = QtWidgets.QFrame(self.frame_10)
        self.frame_3.setGeometry(QtCore.QRect(20, 160, 741, 131))
        self.frame_3.setStyleSheet("background-color:rgb(230,230,230,200)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(990, 100, 1001, 131))
        self.frame_4.setStyleSheet("background-color:rgb(138,181,251)")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(10, 20, 501, 91))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(39)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color:rgb(255,255,255,0)")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(550, 40, 171, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(30)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color:rgb(255,255,255,0)")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(470, 60, 71, 31))
        self.label_15.setStyleSheet("background-color:rgb(255,255,255,0)")
        self.label_15.setObjectName("label_15")
        self.frame_6 = QtWidgets.QFrame(self.frame_10)
        self.frame_6.setGeometry(QtCore.QRect(550, 300, 211, 161))
        self.frame_6.setStyleSheet("background-color:rgb(230,230,230,200)")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setGeometry(QtCore.QRect(10, 10, 201, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(255,255,255,0)")
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        self.label_7.setGeometry(QtCore.QRect(40, 80, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Haettenschweiler")
        font.setPointSize(24)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color:rgb(255,255,255,0)")
        self.label_7.setObjectName("label_7")
        self.frame_5 = QtWidgets.QFrame(self.frame_10)
        self.frame_5.setGeometry(QtCore.QRect(290, 300, 241, 161))
        self.frame_5.setStyleSheet("background-color:rgb(230,230,230,200)")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 201, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color:rgb(255,255,255,0)")
        self.label_8.setObjectName("label_8")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setEnabled(True)
        self.frame_7.setGeometry(QtCore.QRect(40, 70, 61, 31))
        self.frame_7.setStyleSheet("background-color:rgb(0,255,0)")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setGeometry(QtCore.QRect(30, 40, 61, 41))
        self.frame_8.setStyleSheet("background-color:rgb(255,0,0)")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_13 = QtWidgets.QFrame(self.frame_5)
        self.frame_13.setGeometry(QtCore.QRect(40, 120, 61, 31))
        self.frame_13.setStyleSheet("background-color:rgb(255,255,0)")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.frame_14 = QtWidgets.QFrame(self.frame_13)
        self.frame_14.setGeometry(QtCore.QRect(30, 40, 61, 41))
        self.frame_14.setStyleSheet("background-color:rgb(255,255,0)")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setGeometry(QtCore.QRect(130, 60, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Haettenschweiler")
        font.setPointSize(22)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color:rgb(255,255,255,0)")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_5)
        self.label_12.setGeometry(QtCore.QRect(130, 110, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Haettenschweiler")
        font.setPointSize(22)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color:rgb(255,255,255,0)")
        self.label_12.setObjectName("label_12")
        self.frame_9 = QtWidgets.QFrame(self.frame_10)
        self.frame_9.setGeometry(QtCore.QRect(20, 300, 251, 161))
        self.frame_9.setStyleSheet("background-color:rgb(230,230,230,200)")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_2 = QtWidgets.QLabel(self.frame_9)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Haettenschweiler")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgb(255,255,255,0)")
        self.label_2.setObjectName("label_2")
        self.label_16 = QtWidgets.QLabel(self.frame_10)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 781, 481))
        self.label_16.setStyleSheet("border:2px;\n" "border-radius:20px")
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(sys.path[0] + "/UIimg/true.jpg"))
        self.label_16.setObjectName("label_16")
        self.label_16.raise_()
        self.frame.raise_()
        self.frame_3.raise_()
        self.frame_6.raise_()
        self.frame_5.raise_()
        self.frame_9.raise_()
        # UIEND

        # timer
        self.uiThread = MyThread()  # 创建一个线程
        self.uiThread.sec_changed_signal.connect(
            self.uiUpData)  # 觸發訊號導正到timeup去
        self.uiThread.start()
        self.carThread = MyCarThread()  # 创建一个线程
        self.carThread.timerTime = 3  # 設定timer每5秒動作一次
        self.carThread.sec_changed_signal.connect(
            self.carUpData)  # 觸發訊號導正到timeup去
        self.carThread.start()
        # end timer

        # 宣告區
        self.carLast = 0  # 車初始化 上次位置
        self.falg = 0
        self.timeCounter = 0
        self.state = ["0 KM/H", "無", "99999", "0"]
        # 結束宣告區
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("MainWindow", "目前時速："))
        self.label_4.setText(_translate("MainWindow", "299km/h"))
        self.label_13.setText(_translate("MainWindow", "救護車方位："))
        self.label_14.setText(_translate("MainWindow", "左前方"))
        #self.label_15.setText(_translate("MainWindow", "箭頭圖片"))
        self.label.setText(_translate("MainWindow", "目前時間"))
        self.label_7.setText(_translate("MainWindow", "00:00:00"))
        self.label_8.setText(_translate("MainWindow", "系統狀態"))
        self.label_11.setText(_translate("MainWindow", "GPS"))
        self.label_12.setText(_translate("MainWindow", "NET"))
        self.label_2.setText(_translate("MainWindow", "你別..真的別左轉"))

    def uiUpData(self, localtime):
        _translate = QtCore.QCoreApplication.translate
        # 時間
        self.label_7.setText(_translate("MainWindow", localtime))
        # 車況
        self.label_14.setText(_translate("MainWindow", self.state[1]))
        self.label_4.setText(_translate("MainWindow", self.state[0]))
        self.label_2.setText(
            _translate("MainWindow", "距離: " + self.state[2] + "公尺"))
        # 狀態表
        if (self.state[3] == "1"):
            self.frame_13.setStyleSheet("background-color:rgb(0,255,0)")  # NET
        else:
            self.frame_13.setStyleSheet("background-color:rgb(255,0,0)")  # NET
        self.frame_7.setStyleSheet("background-color:rgb(0,255,0)")  # GPS

    def carUpData(self, stateIn):
        self.state = stateIn


class MyThread(QtCore.QThread):

    sec_changed_signal = QtCore.pyqtSignal(str)  # 回傳型態：str

    def __init__(self, sec=1000, parent=None):
        super().__init__(parent)
        self.sec = sec  # 默认1000秒
        self.timerTime = 1
        self.sels = 0

    def run(self):
        for i in range(self.sec):
            self.sec_changed_signal.emit(
                time.strftime("%H:%M:%S", time.localtime()))  # 觸發函式
            time.sleep(self.timerTime)


class MyCarThread(QtCore.QThread):

    sec_changed_signal = QtCore.pyqtSignal(list)  # 回傳型態：list

    def __init__(self, sec=100000, parent=None):
        super().__init__(parent)
        self.sec = sec  # 默认1000秒
        self.timerTime = 3
        self.state = ["0 KM/H", "無", "99999", "0"]
        self.falg = 0
        self.netFalg = 0
        self.sheet = googlesheet.GoogleSheet()
        try:
            self.sheet.init('test')
        except httplib2.ServerNotFoundError:
            self.netFalg = 0
            print("無網路重新連接...")
        else:
            self.netFalg = 1
            print("連接成功")

    def run(self):
        for i in range(self.sec):
            self.netTest()
            try:
                if self.netFalg:  # 網路旗標 有無網路
                    if self.falg:  # 第一次近來不做 因為沒有上次車子的位置
                        carNow = AT.GPS()
                        print(carNow)
                        carState = final.mydata(carNow,
                                                self.carLast)  # 車狀態[時速,方向]
                        while 1:
                            values_list = self.sheet.row_values(
                                3)  # 取得救護車 最新位置
                            values_list1 = self.sheet.row_values(
                                4)  # 取得救護車 上次位置
                            if (values_list and values_list1):
                                break
                            print("sheet 抓不到資料...")
                            time.sleep(0.5)

                        ambCarM = final.AMBandmy(
                            carNow, values_list[1])  # 車跟救護車[距離(M),方向]
                        ambState = final.AMBdata(values_list[1],
                                                 values_list1[1])  # 救護車[時速,方向]
                        self.carLast = carNow

                        self.state = [
                            str(carState[0]) + " KM/H",
                            str(ambCarM[1]),
                            str(ambCarM [0]),
                            str(self.netFalg)
                        ]

                    else:
                        self.carLast = AT.GPS()
                        self.falg = 1

                        self.state = [
                            "0 KM/H", "無", "99999",
                            str(self.netFalg)
                        ]
                else:
                    self.state = ["0 KM/H", "無", "99999", str(self.netFalg)]
            except:
                self.state = ["0 KM/H", "無", "99999", str(self.netFalg)]

            self.sec_changed_signal.emit(self.state)  # 觸發函式
            time.sleep(self.timerTime)

    def netTest(self):  # 網路檢測
        try:
            requests.get('https://www.google.com.tw/')
        except requests.exceptions.ConnectionError:
            self.netFalg = 0
            print("失去網路訊號重新連接中...")
        else:
            print()
            self.netFalg = 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
