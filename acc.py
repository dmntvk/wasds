import requests
import random
import time
from threading import Thread
import os
import sys


def abobs():
    def token():
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
                   'g-recaptcha-response': random.SystemRandom().choice([
                       '03ANYolqt4XG_Elu0XZ-5ub4awvWNiEnyC-u4c5sWVdnT-a47NTQpaasyKIUXNoWWiNXyPPKz-6J4o2SAOgeqP_0mkctvyiVBsAeZAgqX0IKyRqJUTZOfY_sEUu9Mgb8_YWMJ73OyR0MgBYlQGVfCOjscaE_hbUUANJxuaMey3XtaHXdRZnZeOG38GG8YMEyPNJaCFS8SbMamoqeiurahr-DxNsBGMqTX13nv3YFDi_CJtfrQtU3VnHWHZpF896ymxotlIvuizB2hkE5FsY-AB_JKgPVH3MnKdLHOvYuJctr2XAGamiBaiVO6c6pStfx4Ydl9flvywGU6boG2OFusd6nqdYW5Ry7r0K6i9zcaiig4fn-rami9-mcvpiigwV4DB_5Hj9IlsNseA-hWmHcOLD0Ku_kByER_6vtrKkkFGEyur4AbzEhZed2A6F7OMq6_6e-tApqtXXuivoRsTfTeNlynOiLLDrya8GCWGShhd6GmtAAqRI5a5wCiKo_gEhequOPwO4DSVu6NG',
                       '03ANYolqsrubBsFcGN125ioPmSovX_Q1gtWynqYDwB9Oip8oXMONzn_Q1MJV3OBoyaO3kT54a3Pe-I_OQ-f6hmHk1ibX3CI3MTtJ1xWbqY0vse74Z2hBBEBK2lWDqVmhUZD5kb22z4RJ_cfrEc-FjGIuVjObFebx3HqOn3Cgqh7b1OYHFwW5sLKBLlhbD6FFpM575LBBEdwY05fF2DK39NiYPFS4njPwWbyAOJofcTiWYNaZ8xvq1oOUmwdYa76mDxOXhGPEzYxgK3BNyYlqn5ZG9bqmXOY4gWBoForpO7Hw5AAcDz7eHLNRjoPJSKplU-x7OMJ0BHysVy3pY5-Y6YYeOxbuR1Tr3bSOxncwJAbYgbcam5AryU0wiDc0jRHFCYUFDWkG4IM0V5jDiHP-rPrmQ5sOagnX0oVG43q2jksHhfZKig9UaFjSd-9GjGVj8GUbNhgcYgVYfyqi3OkS8VZYLuKatxVekrm8wS14RsO_6oQkbq19rh85T-4c7VCGSVKk9bZou_0LT0',
                       '03ANYolqu-uuHzWE0A8pgCnUNFSWnDzSa6AmJS4sqvlKFTz536uNwAOC1eGfIOQj-e9JCgx2nr4XbhTiOs1hyhWZjhzSkVQo5SfWRvNRj_aQNeg6ug7jAzsT9qxVv7LuHDowa5bgW0HG-IRRWEbboVoahm36c6JoB7vjF25_dzv7Nm6IxcGeollF6HoX3roOIoXCKPzOFDWURZ84jy0rLpScS-tYQDVFiCR5dUP6ZPOxIwGauX2GA_8vzlNlE-R4E22N9e8xzrLav2O0Oc6x9Eq2hqUpwINRGNO1KXauzA0ov_QkVHUUa1jqY9ZJzT3VIS8FtGhnKkXgBPW0WXZfhrZQwIfbRH8Qns_-lwdd5KhFfEc1YLALM4heRl4hMK61oICo0gbXUXTEnkvBxpFKQDNLIdz_gBa7mzM0dogD4Mtb_TxKCu5RZJAgMWVNIklZLBRXF0RPGqpF9VTftiCd7R0reu3NY10wB3_4faZMxudBdLIwqKv0RSXRaNh8AQIMMneByOT7jg5mXm33p_hBfg2DQh12K4sOdPiw']),
                   'user-agent': 'WASD/124 CFNetwork/1206 Darwin/20.1.0',
                   'content-type': 'application/json',
                   'wudid': 'ios_E27F6FAF-FE38-4ACB-955F-6C4A2F23ACCE',
                   'accept': 'application/json, text/plain',
                   'cache-control': 'no-cache'
                   }
        cookies = {
            'captcha-passed-token': random.SystemRandom().choice([
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjAyNzIxNjgsImV4cCI6MTY3NTgyNDE2OH0.CEUH-nzd185FoMb6dX3yDIoDHHReGMOptRMrWyIJ5xY',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjAzMjI3OTUsImV4cCI6MTY3NTg3NDc5NX0.bv4vYu95pUehkmLq9BqYB3i5ZdQwNtlNsZAlhJ_NOdo',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjAzMjM3NDgsImV4cCI6MTY3NTg3NTc0OH0.vXoAMrIhSxNzBxNnMwUpuMdt7QQ389Tilw0e0RtWqAU',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjAzMjM4MjcsImV4cCI6MTY3NTg3NTgyN30.hhxqf8QOd4MD7OUkwe9Hgodt4gs4vzNdJSa881MRSAE',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjA2NjY3MTQsImV4cCI6MTY3NjIxODcxNH0.Es8w8OgEoYTaDpLm5gkUJFL1zjqgACPZ7jroOsRUbwI',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjA2NjY2ODUsImV4cCI6MTY3NjIxODY4NX0.7MpoYOJTiXh2pHyw_q_ZdxYOY1svXDLlrC6icb3St8o',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjA2NjY2NTYsImV4cCI6MTY3NjIxODY1Nn0.3ovaI5IXnAAKDJyeLKMkmpsf4YNHpqXcGgMc4KcTGxk',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjA2NjY1MzYsImV4cCI6MTY3NjIxODUzNn0.S9deMpYBRe-ApSdkw3Mcn5AvrwtFhKVxn3rnY7jmZ1I',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjA2NjY3NDcsImV4cCI6MTY3NjIxODc0N30.FRmYUpj2-s9r-Oh2jWKyykPBb490P5pos8U_I3546Ms'
            ])
        }
        data = {"user_email": f"{login}", "user_password": f"{pwd}"}

        req = requests.post(url, headers=headers, json=data, cookies=cookies)
        time.sleep(10)
        w = (req.text)
        print(w)

        if req.text == '{"error":{"status_code":400,"code":"INVALID_CREDENTIALS","details":"Invalid credentials provided"}}':
            print('Не правильный пасс')
        if '"access_token":' in w:
            access_token = w[w.find('"access_token":') + 15:w.find(',')]
        if '"refresh_token":"' in w:
            refresh = w[w.find('","refresh_token":') + 18:w.find(',"enabled_2fa')]
        return access_token, refresh
    asd = token()
    ref = asd[1]


    def newtok():
        url = 'https://wasd.tv/api/v2/auth/refresh'
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
                   'g-recaptcha-response': random.SystemRandom().choice([
                       '03ANYolqt4XG_Elu0XZ-5ub4awvWNiEnyC-u4c5sWVdnT-a47NTQpaasyKIUXNoWWiNXyPPKz-6J4o2SAOgeqP_0mkctvyiVBsAeZAgqX0IKyRqJUTZOfY_sEUu9Mgb8_YWMJ73OyR0MgBYlQGVfCOjscaE_hbUUANJxuaMey3XtaHXdRZnZeOG38GG8YMEyPNJaCFS8SbMamoqeiurahr-DxNsBGMqTX13nv3YFDi_CJtfrQtU3VnHWHZpF896ymxotlIvuizB2hkE5FsY-AB_JKgPVH3MnKdLHOvYuJctr2XAGamiBaiVO6c6pStfx4Ydl9flvywGU6boG2OFusd6nqdYW5Ry7r0K6i9zcaiig4fn-rami9-mcvpiigwV4DB_5Hj9IlsNseA-hWmHcOLD0Ku_kByER_6vtrKkkFGEyur4AbzEhZed2A6F7OMq6_6e-tApqtXXuivoRsTfTeNlynOiLLDrya8GCWGShhd6GmtAAqRI5a5wCiKo_gEhequOPwO4DSVu6NG',
                       '03ANYolqsrubBsFcGN125ioPmSovX_Q1gtWynqYDwB9Oip8oXMONzn_Q1MJV3OBoyaO3kT54a3Pe-I_OQ-f6hmHk1ibX3CI3MTtJ1xWbqY0vse74Z2hBBEBK2lWDqVmhUZD5kb22z4RJ_cfrEc-FjGIuVjObFebx3HqOn3Cgqh7b1OYHFwW5sLKBLlhbD6FFpM575LBBEdwY05fF2DK39NiYPFS4njPwWbyAOJofcTiWYNaZ8xvq1oOUmwdYa76mDxOXhGPEzYxgK3BNyYlqn5ZG9bqmXOY4gWBoForpO7Hw5AAcDz7eHLNRjoPJSKplU-x7OMJ0BHysVy3pY5-Y6YYeOxbuR1Tr3bSOxncwJAbYgbcam5AryU0wiDc0jRHFCYUFDWkG4IM0V5jDiHP-rPrmQ5sOagnX0oVG43q2jksHhfZKig9UaFjSd-9GjGVj8GUbNhgcYgVYfyqi3OkS8VZYLuKatxVekrm8wS14RsO_6oQkbq19rh85T-4c7VCGSVKk9bZou_0LT0',
                       '03ANYolqu-uuHzWE0A8pgCnUNFSWnDzSa6AmJS4sqvlKFTz536uNwAOC1eGfIOQj-e9JCgx2nr4XbhTiOs1hyhWZjhzSkVQo5SfWRvNRj_aQNeg6ug7jAzsT9qxVv7LuHDowa5bgW0HG-IRRWEbboVoahm36c6JoB7vjF25_dzv7Nm6IxcGeollF6HoX3roOIoXCKPzOFDWURZ84jy0rLpScS-tYQDVFiCR5dUP6ZPOxIwGauX2GA_8vzlNlE-R4E22N9e8xzrLav2O0Oc6x9Eq2hqUpwINRGNO1KXauzA0ov_QkVHUUa1jqY9ZJzT3VIS8FtGhnKkXgBPW0WXZfhrZQwIfbRH8Qns_-lwdd5KhFfEc1YLALM4heRl4hMK61oICo0gbXUXTEnkvBxpFKQDNLIdz_gBa7mzM0dogD4Mtb_TxKCu5RZJAgMWVNIklZLBRXF0RPGqpF9VTftiCd7R0reu3NY10wB3_4faZMxudBdLIwqKv0RSXRaNh8AQIMMneByOT7jg5mXm33p_hBfg2DQh12K4sOdPiw']),
                   'user-agent': 'WASD/124 CFNetwork/1206 Darwin/20.1.0',
                   'content-type': 'application/json',
                   'wudid': 'ios_E27F6FAF-FE38-4ACB-955F-6C4A2F23ACCE',
                   'accept': 'application/json, text/plain',
                   'cache-control': 'no-cache'
                   }
        cookies = {
            'captcha-passed-token': random.SystemRandom().choice([
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjAyNzIxNjgsImV4cCI6MTY3NTgyNDE2OH0.CEUH-nzd185FoMb6dX3yDIoDHHReGMOptRMrWyIJ5xY',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjAzMjI3OTUsImV4cCI6MTY3NTg3NDc5NX0.bv4vYu95pUehkmLq9BqYB3i5ZdQwNtlNsZAlhJ_NOdo',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjAzMjM3NDgsImV4cCI6MTY3NTg3NTc0OH0.vXoAMrIhSxNzBxNnMwUpuMdt7QQ389Tilw0e0RtWqAU',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjAzMjM4MjcsImV4cCI6MTY3NTg3NTgyN30.hhxqf8QOd4MD7OUkwe9Hgodt4gs4vzNdJSa881MRSAE',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjA2NjY3MTQsImV4cCI6MTY3NjIxODcxNH0.Es8w8OgEoYTaDpLm5gkUJFL1zjqgACPZ7jroOsRUbwI',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjA2NjY2ODUsImV4cCI6MTY3NjIxODY4NX0.7MpoYOJTiXh2pHyw_q_ZdxYOY1svXDLlrC6icb3St8o',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjA2NjY2NTYsImV4cCI6MTY3NjIxODY1Nn0.3ovaI5IXnAAKDJyeLKMkmpsf4YNHpqXcGgMc4KcTGxk',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjA2NjY1MzYsImV4cCI6MTY3NjIxODUzNn0.S9deMpYBRe-ApSdkw3Mcn5AvrwtFhKVxn3rnY7jmZ1I',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjA2NjY3NDcsImV4cCI6MTY3NjIxODc0N30.FRmYUpj2-s9r-Oh2jWKyykPBb490P5pos8U_I3546Ms'
            ])
        }
        data = {"refresh_token":f"{ref}"}

        req = requests.post(url, headers=headers, json=data, cookies=cookies)
        w = (req.text)

        if '"access_token":' in w:
            access_token = w[w.find('"access_token":') + 15:w.find(',')]
        if '"refresh_token":"' in w:
            refresh = w[w.find('","refresh_token":') + 18:w.find('}')]

        asd =(access_token, refresh)
        return asd

    def zapros():
        access_token = asd[0]
        while True:
            url = 'https://wasd.tv/api/streams/1109566/views'

            headers = {'accept': 'application/json',
                       'accept-encoding': 'gzip, deflate, br',
                       'content-type': 'application/json',
                       'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
                       }
            cookies = {
                'wasd-access-token': access_token,
                'wasd-refresh-token': 'BZwuZaqCbdY38_ibXupoAsHDjSn_k5bXmmlMO_tiXeQ.BzX3rI7Z6LXsjo5luB3nFs1MJVsjomyvAsMnZTyC3d8',
                'captcha-passed-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiR1VFU1QiLCJpYXQiOjE2NjAwODMyMTIsImV4cCI6MTY3NTYzNTIxMn0.XJH6A1f3RhynIBunRZo_RhG8DJwdo3mzIzPJfsTW2Sk'
            }
            data = {"view_dtime": "2022-08-08T19:55:26.840Z"}

            req = requests.post(url, headers=headers, cookies=cookies, json=data)

            print(req.text, "5 минут прошло)")
            if req.text == '{"error":{"status_code":401,"code":"AUTH_TOKEN_EXPIRED","details":{}}}':
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                time.sleep(300)
    thss = Thread(target=zapros, args=())
    thss.start()





file = open('acc.txt').read().split('\n')
for account in file:
    login = account.split(":")[0]
    pwd = account.split(":")[1]
    proxys = account.split(":")[2]
    ports = account.split(":")[3]
    abobs()