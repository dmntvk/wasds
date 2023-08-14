# from chatbot import Ui_MainWindow
# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow, qApp
# import requests
# import random
# import time
# import _thread
# import websocket
# import ssl
# import re
#
#
# id_stream = input("Введите id трансляции: ")
# id_chanel = input("Введите id  канала: ")
#
# class MyMainWindow(QMainWindow, Ui_MainWindow):
#     def __init__(self, parent=None):
#         super(MyMainWindow, self).__init__(parent)
#         qApp.installEventFilter(self)
#         self.setupUi(self)
#         self.show()
#         file = open('acc.txt').read().split('\n')
#         for account in file:
#             global login, pwd
#             login = account.split(":")[0]
#             pwd = account.split(":")[1]
#             proxys = account.split(":")[2]
#             ports = account.split(":")[3]
#             self.pushButton.clicked.connect(self.sendmess)
#             self.auntef()
#             self.loadlogin()
#         self.pushButton.clicked.connect(self.sendmess)
#
#
#
#
#     global loglist, tokenlis
#     loglist = []
#     tokenlis = []
#     def auntef(self):
#         url = 'https://wasd.tv/api/v2/auth/tokens'
#         headers = {'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
#                    'device-type': 'iPhone',
#                    'os-version': 'iOS 14.2',
#                    'accept-language': 'en-us',
#                    'app-version': '1.15',
#                    'g-recaptcha-version': 'V2_IOS',
#                    'network-type': 'WIFI',
#                    'os': 'iOS',
#                    'sec-ch-ua-platform': '"macOS"',
#                    'pragma': 'no-cache',
#                    'device-name': 'iPhone8,1',
#                    'locale': 'en-US',
#                    'sec-ch-ua-mobile': '?0',
#                    'g-recaptcha-response': '03ANYolqt4XG_Elu0XZ-5ub4awvWNiEnyC-u4c5sWVdnT-a47NTQpaasyKIUXNoWWiNXyPPKz-6J4o2SAOgeqP_0mkctvyiVBsAeZAgqX0IKyRqJUTZOfY_sEUu9Mgb8_YWMJ73OyR0MgBYlQGVfCOjscaE_hbUUANJxuaMey3XtaHXdRZnZeOG38GG8YMEyPNJaCFS8SbMamoqeiurahr-DxNsBGMqTX13nv3YFDi_CJtfrQtU3VnHWHZpF896ymxotlIvuizB2hkE5FsY-AB_JKgPVH3MnKdLHOvYuJctr2XAGamiBaiVO6c6pStfx4Ydl9flvywGU6boG2OFusd6nqdYW5Ry7r0K6i9zcaiig4fn-rami9-mcvpiigwV4DB_5Hj9IlsNseA-hWmHcOLD0Ku_kByER_6vtrKkkFGEyur4AbzEhZed2A6F7OMq6_6e-tApqtXXuivoRsTfTeNlynOiLLDrya8GCWGShhd6GmtAAqRI5a5wCiKo_gEhequOPwO4DSVu6NG',
#                    'user-agent': 'WASD/124 CFNetwork/1206 Darwin/20.1.0',
#                    'content-type': 'application/json',
#                    'wudid': 'ios_E27F6FAF-FE38-4ACB-955F-6C4A2F23ACCE',
#                    'accept': 'application/json, text/plain',
#                    'cache-control': 'no-cache'
#                    }
#         cookies = {
#             'captcha-passed-token': random.SystemRandom().choice(['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjAwOTk5OTUsImV4cCI6MTY3NTY1MTk5NX0.P_NuD1fr5IFZQ7pkX6zk_6wnHsC4gNp1MLBuvFeY_OM',
#                                                                   'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjAyMjg5MDMsImV4cCI6MTY3NTc4MDkwM30.zUvCASOu4erIoeLjne4aI7m9Ke2-_s4MdHHJF5MG7ts',
#                                                                   'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjAyMzE1MzUsImV4cCI6MTY3NTc4MzUzNX0.Ig0GiLVBUfj3Rr6bMtVxn7o6C0YIyDRw-lZA2JDCWek'])
#         }
#         data = {"user_email": f"{login}", "user_password": f"{pwd}"}
#
#         req = requests.post(url, headers=headers, json=data, cookies=cookies)
#         w = (req.text)
#         if '"access_token":' in w:
#             access_token = w[w.find('"access_token":') + 15:w.find(",")]
#         bots = []
#         for x in range(1):
#             psw = ''
#             for x in range(9):
#                 psw = psw + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnm'))
#             byb = psw + '-cv4s-4f89-9ae5-913f2e823127'
#             bots.append(byb)
#         url = 'https://wasd.tv/api/v2/profiles/current'
#         for x in bots:
#             cookies = {'wudid': x,
#                        'wudid_us': '1d455290-dcc5-4f89-9ae5-913f2e823127',
#                        'wasd-access-token': access_token,
#                        'session_id': '22c8e2ed-24c7-44b9-80a7-66dbf14e4bdb',
#                        'wasd-quick-reg-token': '8f_Iyq55BqrfvVXOEKXdJNV9f1wdgCUvSljyh6yDoAM.quTu9sAhdZ4DpyhMVhDxS47yBgSjdtmRfQG0KAhDYIY',
#                        'tmr_detect': '1%7C1659997084467',
#                        'tmr_reqNum': '147',
#                        '_dc_gtm_UA-26459082-21': '1'
#                        }
#             req = requests.get(url, headers=headers, cookies=cookies)
#             w = req.text
#             print(req.text)
#             if '"user_login":"' in w:
#                 logins = w[w.find('"user_login":"') + 14:w.find('","user_profile"')]
#                 loglist.append(logins)
#
#         url = 'https://wasd.tv/api/auth/chat-token'
#         headers = {'accept': 'application/json',
#                    'accept-encoding': 'gzip, deflate, br',
#                    'content-type': 'application/json',
#                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
#                    }
#
#         cookies = {
#             'wasd-access-token': access_token,
#             'captcha-passed-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjAwODMyMTIsImV4cCI6MTY3NTYzNTIxMn0.XJH6A1f3RhynIBunRZo_RhG8DJwdo3mzIzPJfsTW2Sk'
#         }
#         req = requests.get(url, headers=headers, cookies=cookies)
#         w = (req.text)
#         if '"result":"' in w:
#             chat_token = w[w.find('{"result":"') + 11:w.find('"}')]
#             tokenlis.append(chat_token)
#
#
#
#     def loadlogin(self):
#         _translate = QtCore.QCoreApplication.translate
#         a = 0
#         for x in range(0, len(loglist)):
#             self.comboBox.addItem(loglist[x])
#
#     def sendmess(self):
#         def abse():
#
#             massage = self.lineEdit.text()
#             print(massage)
#             clic = self.comboBox.currentText()
#             print(clic)
#         abse()
#
#         for x in [loglist]:
#             if self.comboBox.currentText() == x:
#                 logtok = {}
#                 for i in range(0, len(loglist)):
#                     logtok[loglist[i]] = tokenlis[i]
#                 print(logtok)
#                 def on_message(ws, message):
#                     print(message)
#
#                 def on_error(ws, error):
#                     print(error)
#
#                 def on_close(ws):
#                     print("### closed ###")
#
#                 def on_open(ws):
#                     def run(*args):
#                         for i in range(1):
#                             time.sleep(1)
#                             ws.send(
#                                 '42["join",{"streamId"' + f'{id_stream},"channelId":{id_chanel},"jwt":"{logtok[(x)]}"' + ',"excludeStickers":true}]')
#                             time.sleep(1)
#                             ws.send(
#                                 '42["message",{"streamId"'+ f':{id_stream},"streamerId":1379611,"channelId":{id_chanel},"jwt":"{logtok[(x)]}","message":"{massage}"'+ '}]')
#                             print('42["message",{"streamId"'+ f':{id_stream},"streamerId":1379611,"channelId":{id_chanel},"jwt":"{logtok[(x)]}","message":"{massage}"'+ '}]')
#                         time.sleep(1)
#                         ws.close()
#
#                     _thread.start_new_thread(run, ())
#
#                 websocket.enableTrace(True)
#                 ws = websocket.WebSocketApp("wss://chat.wasd.tv/socket.io/?EIO=3&transport=websocket",
#                                             on_message=on_message,
#                                             on_error=on_error,
#                                             on_close=on_close
#                                             )
#                 ws.on_open = on_open
#                 ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
#
#     def but(self):
#         self.pushButton.clicked.connect(self.sendmess)
#
#
#
#
#
#
#
#
#     # def aboba(self):
#     #     url = 'https://wasd.tv/api/chat/streams/1099093/messages?limit=10&offset=0'
#     #
#     #     headers = {'accept': 'application/json',
#     #                'accept-encoding': 'gzip, deflate, br',
#     #                'content-type': 'application/json',
#     #                'user-agent': random.SystemRandom().choice([
#     #                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
#     #                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15'])
#     #                }
#     #     req = requests.get(url, headers=headers)
#     #
#     #     w = req.text
#     #     wl = req.text
#     #     message = []
#     #     logind = []
#     #
#     #     def mess(w):
#     #         while True:
#     #             if '"message":"' in w:
#     #                 access_token = w[w.find('"message":"') + 11:w.find('","user_login":')]
#     #                 message.append(access_token)
#     #             else:
#     #                 break
#     #             w = w.replace('"message":"', '', 1)
#     #             w = w.replace('","user_login":', '', 1)
#     #
#     #     mess(w)
#     #
#     #     def logins(wl):
#     #         while True:
#     #             if '"user_login":"' in wl:
#     #                 access_token = wl[wl.find('"user_login":"') + 14:wl.find('","user_avatar":')]
#     #                 logind.append(access_token)
#     #             else:
#     #                 break
#     #             wl = wl.replace('"user_login":"', '', 1)
#     #             wl = wl.replace('","user_avatar":', '', 1)
#     #
#     #     logins(wl)
#     #     fulmes = {}
#     #     for i in range(0, len(message)):
#     #         fulmes[message[i]] = logind[i]
#     #     print(fulmes)
#     #     ski = "\n"
#     #     _translate = QtCore.QCoreApplication.translate
#     #     self.textBrowser.setHtml(_translate("MainWindow", f'{
#     #                                                         for key in fulmes:
#     #                                                             key}'))
#
#
#
#     # def loadchat(self):
#     #     url = 'https://wasd.tv/api/chat/streams/1099093/messages?limit=10&offset=0'
#     #
#     #     headers = {'accept': 'application/json',
#     #                'accept-encoding': 'gzip, deflate, br',
#     #                'content-type': 'application/json',
#     #                'user-agent': random.SystemRandom().choice([
#     #                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
#     #                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15'])
#     #                }
#     #     req = requests.get(url, headers=headers)
#     #
#     #     w = req.text
#     #     wl = req.text
#     #     message = []
#     #     logind = []
#     #
#     #     def mess(w):
#     #         while True:
#     #             if '"message":"' in w:
#     #                 access_token = w[w.find('"message":"') + 11:w.find('","user_login":')]
#     #                 message.append(access_token)
#     #             else:
#     #                 break
#     #             w = w.replace('"message":"', '', 1)
#     #             w = w.replace('","user_login":', '', 1)
#     #     mess(w)
#     #     def logins(wl):
#     #         while True:
#     #             if '"user_login":"' in wl:
#     #                 access_token = wl[wl.find('"user_login":"') + 14:wl.find('","user_avatar":')]
#     #                 logind.append(access_token)
#     #             else:
#     #                 break
#     #             wl = wl.replace('"user_login":"', '', 1)
#     #             wl = wl.replace('","user_avatar":', '', 1)
#     #     logins(wl)
#     #     fulmes = {}
#     #     for i in range(0, len(message)):
#     #         fulmes[message[i]] = logind[i]
#     #     print(fulmes)
#
#
#
#
#
#
#
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     window = QtWidgets.QMainWindow()
#     chat = MyMainWindow()
#     chat.setupUi(window)
#     sys.exit(app.exec_())


from chatbot import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp
import requests
import random
import time
import _thread
import websocket
import ssl

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
chat = Ui_MainWindow()
chat.setupUi(window)
window.show()


global loglist, tokenlis
loglist = []
tokenlis = []




def auntef():
    time.sleep(10)
    access_token = 0
    url = 'https://wasd.tv/api/v2/auth/tokens'
    headers = {'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
               'device-type': 'iPhone',
               'os-version': 'iOS 14.2',
               'accept-language': 'en-us',
               'app-version': '1.15',
               'g-recaptcha-version': 'V2_IOS',
               'network-type': 'WIFI',
               'os': 'iOS',
               'sec-ch-ua-platform': '"macOS"',
               'pragma': 'no-cache',
               'device-name': 'iPhone8,1',
               'locale': 'en-US',
               'sec-ch-ua-mobile': '?0',
               'g-recaptcha-response': random.SystemRandom().choice(['03ANYolqt4XG_Elu0XZ-5ub4awvWNiEnyC-u4c5sWVdnT-a47NTQpaasyKIUXNoWWiNXyPPKz-6J4o2SAOgeqP_0mkctvyiVBsAeZAgqX0IKyRqJUTZOfY_sEUu9Mgb8_YWMJ73OyR0MgBYlQGVfCOjscaE_hbUUANJxuaMey3XtaHXdRZnZeOG38GG8YMEyPNJaCFS8SbMamoqeiurahr-DxNsBGMqTX13nv3YFDi_CJtfrQtU3VnHWHZpF896ymxotlIvuizB2hkE5FsY-AB_JKgPVH3MnKdLHOvYuJctr2XAGamiBaiVO6c6pStfx4Ydl9flvywGU6boG2OFusd6nqdYW5Ry7r0K6i9zcaiig4fn-rami9-mcvpiigwV4DB_5Hj9IlsNseA-hWmHcOLD0Ku_kByER_6vtrKkkFGEyur4AbzEhZed2A6F7OMq6_6e-tApqtXXuivoRsTfTeNlynOiLLDrya8GCWGShhd6GmtAAqRI5a5wCiKo_gEhequOPwO4DSVu6NG',
                                                                         '03ANYolqsrubBsFcGN125ioPmSovX_Q1gtWynqYDwB9Oip8oXMONzn_Q1MJV3OBoyaO3kT54a3Pe-I_OQ-f6hmHk1ibX3CI3MTtJ1xWbqY0vse74Z2hBBEBK2lWDqVmhUZD5kb22z4RJ_cfrEc-FjGIuVjObFebx3HqOn3Cgqh7b1OYHFwW5sLKBLlhbD6FFpM575LBBEdwY05fF2DK39NiYPFS4njPwWbyAOJofcTiWYNaZ8xvq1oOUmwdYa76mDxOXhGPEzYxgK3BNyYlqn5ZG9bqmXOY4gWBoForpO7Hw5AAcDz7eHLNRjoPJSKplU-x7OMJ0BHysVy3pY5-Y6YYeOxbuR1Tr3bSOxncwJAbYgbcam5AryU0wiDc0jRHFCYUFDWkG4IM0V5jDiHP-rPrmQ5sOagnX0oVG43q2jksHhfZKig9UaFjSd-9GjGVj8GUbNhgcYgVYfyqi3OkS8VZYLuKatxVekrm8wS14RsO_6oQkbq19rh85T-4c7VCGSVKk9bZou_0LT0',
                                                                        '03ANYolqu-uuHzWE0A8pgCnUNFSWnDzSa6AmJS4sqvlKFTz536uNwAOC1eGfIOQj-e9JCgx2nr4XbhTiOs1hyhWZjhzSkVQo5SfWRvNRj_aQNeg6ug7jAzsT9qxVv7LuHDowa5bgW0HG-IRRWEbboVoahm36c6JoB7vjF25_dzv7Nm6IxcGeollF6HoX3roOIoXCKPzOFDWURZ84jy0rLpScS-tYQDVFiCR5dUP6ZPOxIwGauX2GA_8vzlNlE-R4E22N9e8xzrLav2O0Oc6x9Eq2hqUpwINRGNO1KXauzA0ov_QkVHUUa1jqY9ZJzT3VIS8FtGhnKkXgBPW0WXZfhrZQwIfbRH8Qns_-lwdd5KhFfEc1YLALM4heRl4hMK61oICo0gbXUXTEnkvBxpFKQDNLIdz_gBa7mzM0dogD4Mtb_TxKCu5RZJAgMWVNIklZLBRXF0RPGqpF9VTftiCd7R0reu3NY10wB3_4faZMxudBdLIwqKv0RSXRaNh8AQIMMneByOT7jg5mXm33p_hBfg2DQh12K4sOdPiw',
                                                                     '03ANYolqskb71vFW91_-MMh73erN2EFML2PUlKpKuABWLC7_o9UVZ3bHqdcpnvC8A7MQJXv8t7yvhBe2_m5-G_ocGF0WidB_ALiZKZmVz4ZjpiNO6GdZ4NDwrHwH0sIl4x7m79CTaZrUymXLMyAtPHeaR4eH8lGGVeo2j9ggaa4YckwawywvWNDwsyu_2ZNjRhlxMVNqR-0U3YtN-O1XTpFehXmD89cp-3iBV2aQtXd4CZ-V3O011z3PmCi01vq_Ccn4bahXrhKm0rDeYDR-j66PYpz7kzfmVvY58hYcGIuQrpkbX1XyEykq_GogWvzKvwG5xv0qRhonGP9mzJpqLsnD6iPeWK2RHFMRKjqJ4EFum4yzhJHvF-vnu8XV6oBgGm6khyxLVKmLsbcnvXNX_Zj5UEKHVx6CFTWXG1v9nvks_Nlud4EInbpM6v_sINzw-M88C8mtCiJR2N7TMVW2nvzmL5dnXosFYKRxd-E8DwwJu-8fAy9rjrpif3_QV4v_WURVMy5kgd_Fiv',
                                                                     '03ANYolqs7-KPeXDNXcpn-VPYG2A6vKiHuC1_S9lgwFLM8SgXd3TpHp0GoSNmPUNX-wTaBw3CCba5NI7NXCsKcOmVQ3yzn9QZnSfeojW8oJQZFIpobxZAtvMoAE-1Chvb3jGzCBSk2zSmYE-wWKKutLeN6CiodQUyMn9OvT-2rLNcpuUYZ1RuTUpwWFrED_T_Gw-BViW-9mSDjtwWz-uY_FHRY5P0-sepTyV7SbNDlj5DllHXe6BMbzvgvbsTX0e26dCH0GJzLnC5RttGirLgu_neowDr-TxTUxxHPI58P030ymH1rhIS-CkLBEhicYcf1tM0YDaDBgsYdMc55Gb-xz_RjqlbYHuOBDk9xJFAGwi2psJ6tAlI6TTJBLpDjHJc8iZ_PdJJ_s4hMD4CDVkQxiLzzqSJCyADQvOrnbhX14m-jayf-aNmng6o66WUGCulZpbgVydqTaLyhEEkgJdHa1KKXbIypn449eqYULw1vxKNu3RjdrTqsZjx5b9wQoEmL_h0jEC3-LWSs',
                                                                     '03ANYolqsj7gzwGy3Iw-tClioLHQ09sL6tOxchwfrsx0mwq52OqUco-76ne_NAKRccuc2q4C6wIAeBepGmvqkK0ti1PIqdZYYaC1fr1Q1hSgHsBaiTw12Veh2EujPA-Mg3Q47LAU6goihFADGLAy89UP3pVCkJWwyyZf-GkTWKqOsfrhg4Gvyl5Sa2fO0xyAKBGMo2NtnErtUXVe_ZIs6yR6Vu8jBY9SydMBzD6Lebz1H1lq4bzMhZNQYfyk9HfbRkNNZqqnSW7rfLtdLuQX-XRfeEYYzr5rWyqO3QabDCYuFvXSYsrL7vPBnlgq1xV5LMc5xwpjG4lkfsUOZuzpulbPvUQVqI-esoiZPuZ9LRZrmMrG3lwbgDDAlG71KCiub9lQAuAXTx7hs8bqugpuXCi9fIa3ivou1cD2FZcZ-ZePQrIxl7ZxJ7UCUpNE8wfPvVyuproWDBw30gG4ojlAK5H9diDWzOVh2TOWv5Z0DUdnU5kNoLoF-bXcGKb3iJyYETGyT-gIXh0MY8',
                                                                     '03ANYolqt86_eWlzNtTtDLvML8f5_4L9-XvgFfBfvvlKuLrIo7dyCiUNnI6epCuRo-epEH0eQXnPdmWurx-crZO9u4I3ypjJ9xBoUFMtwMgWpKkVFqwK99e4iiNZMx9hmuQHsz9z2z2YCS2u0sEmkz3wma2yLMd4BfMWihGPMIwbQnUpSjBUHd4gHLd7Q73TSRikZaAEtUGBMvQSq7orNjK7J_sNH5S8RYsCOjOmJ-6VV9QwIs0N5EiX5O_pnW889HBXLZC9M3AXrK8j-cAtRc0rhfnLH8BlWHr67QBnnoNnYz4K9Q49YtcmKGM_ym0iGGNLzgqaUjR8FS015oF2cgVyOApgNU6XoohCvkm6Rf9k9SPd32uOQty7g90pr2uZL6mvRGqKhc5OlDe0CewErhqTi_Ne8ELF-zHXBrmcp95iKZNYIdW2NZ-QYJ3zYrsx2OHhYxUyEFmu3Yrd6qVXmf4G4aHIpJb31WVjOBkiV8KihF2Wkbr4FM8DLb-SYliiJcHt2M2RfKfJAK',
                                                                     '03ANYolqv_kojq9yGnypiBcop2gtk5_gbqI6Xrj4LOeenE6kAH4KUabxkOb2uENRw2Kv5XiKbQSuzUIAkIxTsyVzyl_XOji7ZbnNOXE-8WVAN86r2izH_Ca2aYs4HZqwZsSpT2_rBoeKxeHsexdDQntwzAgDj-gEqwrOKMIgv2qacGkk40gIfjNUN6mdzkMQ0a_nd92bxFi6RJh58aFj27zjSSl3i478K9AhTpgLqONUecz4vHq7eCd7Uq2F_64G-5ocxqH6IzqS4SlamuFXWyXBRLfwlgar6ouB_hty_WpLSwu59yN1Q0-nkrYXzcZh1qHZ2X8ZpQAxRAq_NpQu9sY-bGBJESUlpORTq7id-OB3KGZ5DqQ2kAVamqCrjMIZskXstjTkS5oVMGrtIyJaWnYhaDWf_sXuoD2asCFC5AeubaoPmMfVbhSzGQtGT3W1S6L1-B2VNO3Izfzrryp0g4Lti1wpXhbEocFKflvf8NtuHzzks9MHnYZewKtA2LZvuZdgnwf7Bxx5Oi',
                                                                     '03ANYolqsBf1bY99YDGKPLFhvRI_ZBM36osm-efY--NFXOsEGOH-RScrGXeFosxCz464wJa58eC-Qjlcv4WdSt4EbNOu4lbbxFyCsIhcLjeUlFWW_Fbn4ebzta4TYK-c8OleoXJmouTbg0tDIWVM8xqde8iEKk6JDYZkHbQXFWNR3N1l1cMo58yK8nNz5ltBDDckcLfn6QjAvvg0La1-QIQrGkGBQjU1md1Cl0CtzCFT7SNrIxtweJKN5xMlZhBjYQkCHUeP1Oog2rP_1hAMN-YJwI4MeYOUz-I_mYPHEtELRB4bJBUbjIbzgUASb2Ewn5VjCTJma3UZiI8w8VHFrsg0tL3FxxcldVIf_f0mha9MEyFpUjWHe3nhVIDwgCqT3JPkMg7ZEJo9pnE4ihHxsn_7RwemGpd4EDzeXjBSni2rvzbDxKTYylw5oEoCX62AjhZd-7q0jqygpkXfibmaZBgPIiNL9SSrAkWFo7l0dbdVsO12sHW1V81Vn2uI7st8N60dKUBa6_KnRD']),
               'user-agent': 'WASD/124 CFNetwork/1206 Darwin/20.1.0',
               'content-type': 'application/json',
               'wudid': 'ios_E27F6FAF-FE38-4ACB-955F-6C4A2F23ACCE',
               'accept': 'application/json, text/plain',
               'cache-control': 'no-cache'
               }
    cookies = {
        'captcha-passed-token': random.SystemRandom().choice(['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjAyNzIxNjgsImV4cCI6MTY3NTgyNDE2OH0.CEUH-nzd185FoMb6dX3yDIoDHHReGMOptRMrWyIJ5xY',
                                                                  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjAzMjI3OTUsImV4cCI6MTY3NTg3NDc5NX0.bv4vYu95pUehkmLq9BqYB3i5ZdQwNtlNsZAlhJ_NOdo',
                                                                  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjAzMjM3NDgsImV4cCI6MTY3NTg3NTc0OH0.vXoAMrIhSxNzBxNnMwUpuMdt7QQ389Tilw0e0RtWqAU',
                                                                  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjAzMjM4MjcsImV4cCI6MTY3NTg3NTgyN30.hhxqf8QOd4MD7OUkwe9Hgodt4gs4vzNdJSa881MRSAE',
                                                                  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjA2NjY3MTQsImV4cCI6MTY3NjIxODcxNH0.Es8w8OgEoYTaDpLm5gkUJFL1zjqgACPZ7jroOsRUbwI',
                                                                  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjA2NjY2ODUsImV4cCI6MTY3NjIxODY4NX0.7MpoYOJTiXh2pHyw_q_ZdxYOY1svXDLlrC6icb3St8o',
                                                                  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjA2NjY2NTYsImV4cCI6MTY3NjIxODY1Nn0.3ovaI5IXnAAKDJyeLKMkmpsf4YNHpqXcGgMc4KcTGxk',
                                                                  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjA2NjY1MzYsImV4cCI6MTY3NjIxODUzNn0.S9deMpYBRe-ApSdkw3Mcn5AvrwtFhKVxn3rnY7jmZ1I',
                                                                  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjA2NjY3NDcsImV4cCI6MTY3NjIxODc0N30.FRmYUpj2-s9r-Oh2jWKyykPBb490P5pos8U_I3546Ms',
                                                                  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjEwMDEzNzMsImV4cCI6MTY3NjU1MzM3M30.rM3FBISK6Bb22euEG0t9zFrfqkfygPae7InZ9zJ_np4',
                                                                  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjEwMDE0NDQsImV4cCI6MTY3NjU1MzQ0NH0.Ia39keFfpspH2U0LDuLSV6y3bWKMDIf71QFb-fLXkZ4',
                                                                  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjEwMDE1MDQsImV4cCI6MTY3NjU1MzUwNH0.TixywoPqb_Yp-1iOyfjKJBHvCaS8ojXum-PtJnQEJbM'
                                                                  ])
    }
    data = {"user_email": f"{login}", "user_password": f"{pwd}"}

    req = requests.post(url, headers=headers, json=data, cookies=cookies)
    w = (req.text)
    if '"access_token":' in w:
        access_token = w[w.find('"access_token":') + 15:w.find(",")]
    bots = []
    for x in range(1):
        psw = ''
        for x in range(9):
            psw = psw + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnm'))
        byb = psw + '-cv4s-4f89-9ae5-913f2e823127'
        bots.append(byb)
    url = 'https://wasd.tv/api/v2/profiles/current'
    for x in bots:
        cookies = {'wudid': x,
                   'wudid_us': '1d455290-dcc5-4f89-9ae5-913f2e823127',
                   'wasd-access-token': access_token,
                   'session_id': '22c8e2ed-24c7-44b9-80a7-66dbf14e4bdb',
                   'wasd-quick-reg-token': '8f_Iyq55BqrfvVXOEKXdJNV9f1wdgCUvSljyh6yDoAM.quTu9sAhdZ4DpyhMVhDxS47yBgSjdtmRfQG0KAhDYIY',
                   'tmr_detect': '1%7C1659997084467',
                   'tmr_reqNum': '147',
                   '_dc_gtm_UA-26459082-21': '1'
                   }
        req = requests.get(url, headers=headers, cookies=cookies)
        w = req.text
        print(req.text)
        if '"user_login":"' in w:
            logins = w[w.find('"user_login":"') + 14:w.find('","user_profile"')]
            loglist.append(logins)

    url = 'https://wasd.tv/api/auth/chat-token'
    headers = {'accept': 'application/json',
               'accept-encoding': 'gzip, deflate, br',
               'content-type': 'application/json',
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
               }
    proxies = {'http': f'http://{proxys}:{ports}',
               }
    cookies = {
        'wasd-access-token': access_token,
        'captcha-passed-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjAwODMyMTIsImV4cCI6MTY3NTYzNTIxMn0.XJH6A1f3RhynIBunRZo_RhG8DJwdo3mzIzPJfsTW2Sk'
    }
    req = requests.get(url, headers=headers, cookies=cookies, proxies=proxies)
    w = (req.text)
    if '"result":"' in w:
        chat_token = w[w.find('{"result":"') + 11:w.find('"}')]
        tokenlis.append(chat_token)







file = open('acc.txt').read().split('\n')
for account in file:
    global login, pwd
    login = account.split(":")[0]
    pwd = account.split(":")[1]
    proxys = account.split(":")[2]
    ports = account.split(":")[3]
    auntef()

def loadlogin():
    _translate = QtCore.QCoreApplication.translate
    a = 0
    for x in range(0, len(loglist)):
        chat.comboBox.addItem(loglist[x])

loadlogin()

def sendmess():
    massage = chat.lineEdit.text()
    id_stream = chat.lineEdit_2.text()
    id_chanel = chat.lineEdit_3.text()
    streamerid = chat.lineEdit_4.text()
    for x in loglist:
        if chat.comboBox.currentText() == x:
            logtok = {}
            for i in range(0, len(loglist)):
                logtok[loglist[i]] = tokenlis[i]
            print(logtok)

            def on_message(ws, message):
                print(message)

            def on_error(ws, error):
                print(error)

            def on_close(ws):
                print("### closed ###")

            def on_open(ws):
                def run(*args):
                    for i in range(1):
                        time.sleep(1)
                        ws.send(
                            '42["join",{"streamId":' + f'{id_stream},"channelId":{id_chanel},"jwt":"{logtok[(x)]}","excludeStickers":true' + '}]')
                        time.sleep(1)
                        ws.send(
                            '42["message",{"streamId"' + f':{id_stream},"streamerId":{streamerid},"channelId":{id_chanel},"jwt":"{logtok[(x)]}","message":"{massage}"' + '}]')
                    time.sleep(1)
                    ws.close()

                _thread.start_new_thread(run, ())

            websocket.enableTrace(True)
            ws = websocket.WebSocketApp("wss://chat.wasd.tv/socket.io/?EIO=3&transport=websocket",
                                        on_message=on_message,
                                        on_error=on_error,
                                        on_close=on_close
                                        )
            ws.on_open = on_open
            ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
            chat.lineEdit.clear()



chat.pushButton.clicked.connect(sendmess)



sys.exit(app.exec_())