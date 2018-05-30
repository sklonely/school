import gspread  # 雲端
import datetime  # 時間
import time
import sys
import AT  # AT命令
import final  # 車距計算
import colorama  # cmd字形顏色
from oauth2client.service_account import ServiceAccountCredentials  # google oauth


# 宣告區開始
# colorama.init(autoreset=True)#设置颜色设置自动恢复
def init():
    try:
        global scope, creds, client, sheet
        scope = ['https://www.googleapis.com/auth/drive']  # host sever
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            sys.path[0] + '\client_secret.json', scope)  # atuh 驗證
        client = gspread.authorize(creds)  # 雲端硬碟宣告
        sheet = client.open('test').sheet1  # 試算表宣告
        print(sheet)
    except:
        print("NetWork 404")
        time.sleep(5)
        init()


init()

# AT.init()  # 設定通訊口
# 宣告區結束


def fireTruck():
    try:
        print("救護車上傳GPS位置程式開始")
        falg = 0
        lastLatLng = ""
        while 1:
            # 取得自己最新的位置
            if falg:
                while 1:
                    # print("GPS in")
                    latLng = AT.GPS()
                    # print("GPS out")
                    if (latLng.find(",,")):
                        break
                    else:
                        print("失去衛星訊號 嘗試連接")
                timer = datetime.datetime.now()  # 取得現在時間
                carState = final.mydata(latLng, lastLatLng)  # 車狀態[時速,方向]
                # print("insert in")
                sheet.insert_row(
                    [str(timer), latLng, carState[0], carState[1]],
                    3)  # 在row 3 插入資料
                lastLatLng = latLng
                print("update success: ", latLng)
                time.sleep(3)  # 暫停3秒
            else:  # 第一次沒自己上次的資料
                while 1:
                    # print("GPS in")
                    latLng = AT.GPS()
                    print("GPS out")
                    if (latLng.find(",,")):
                        break
                    else:
                        print("失去衛星訊號 嘗試連接")
                timer = datetime.datetime.now()  # 取得現在時間
                # print("insert in")
                sheet.insert_row([str(timer), latLng, 0], 3)  # 在row 3 插入資料
                lastLatLng = latLng
                print("update success: ", latLng)
                falg = 1
                time.sleep(3)  # 暫停3秒
    except KeyboardInterrupt:
        print("\n程式結束")


def car():
    try:
        carLast = 0  # 初始化 上次位置
        falg = 0
        while 1:
            if falg:  # 第一次近來不做 因為沒有上次車子的位置
                # print("f") DEBUG
                # 資料獲取
                while 1:  # 如果兩個變數沒值就繼續找(因為救護車可能再上傳資料)
                    values_list = sheet.row_values(3)  # 取得救護車 最新位置
                    print(values_list[1])
                    values_list1 = sheet.row_values(4)  # 取得救護車 上次位置
                    if (values_list[1].find(",,") == -1) and (
                            values_list1[1].find(",,") == -1):
                        break
                    else:
                        print("資料出錯 重新載入")

                carNow = AT.GPS()  # 取得自己最新的位置
                if (carNow.find(",,") == "-1"):
                    print("失去衛星定位 正在嘗試連接")
                else:
                    ambCarM = final.AMBandmy(
                        carNow, values_list[1]
                    )  # final.AMBandmy(carNow,values_list) #車跟救護車[距離(M),方向]
                    carState = final.mydata(carNow, carLast)  # 車狀態[時速,方向]
                    ambState = final.AMBdata(values_list[1],
                                             values_list1[1])  # 救護車[時速,方向]
                    # 判斷及計算開始
                    if (ambCarM[0] <= 1000):
                        print("\n請小心附近有救護車: ")
                        print("  " + ambCarM[1] + "方 " + str(ambCarM[0]) +
                              " 公尺")
                        print("行車資訊:" + str(carState[0]) + "公里/小時 方向" +
                              carState[1])
                        print("救護車資訊:" + str(ambState[0]) + "公里/小時 方向" +
                              ambState[1])
                    carLast = carNow  # 更新車位置上次的資料
                # print("救護車0 : "+values_list[1]+"救護車1 : "+values_list1[1]+"車0 : "+carNow+"\n車1 : "+carLast) #DEBUG
                time.sleep(3)
            else:
                while 1:
                    carLast = AT.GPS()
                    if (carLast.find(",,")):
                        break
                # carLast="+CGPSINFO:2245.200007,N,12022.475822,E,150417,104220.0,87.6,0.0,46.6"#更新車位置上次的資料
                falg = 1
                print("一般車車輛提示程式開始運行:\n")
    except KeyboardInterrupt:
        print("\n程式結束")


# t=thd.Thread(target = timerun(3))

# sheet.update_cell(A1,"1") #update
# result=sheet.cell("A1").value#get
# print(final.AMBandmy("'+CGPSINFO:2245.200007,N,12022.475822,E,150418,104221.0,87.6,0.0,46.6\n","+CGPSINFO: 2245.700007,N,12022.475822,E,150418,104220.0,87.6,0.0,46.6"))
# '+CGPSINFO: ,,,,,,,,
print("\n\n")
car()
"""
ser.readline()
ser.write()
"""
