import websocket
import _thread
import time
import ssl


# ws = websockets.connect('wss://chat.wasd.tv/socket.io/?EIO=3&transport=websocket')
# async def test():
#     async with ws as websocket:
#
#         ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
#         await websocket.send("hello")
#         response = await websocket.recv()
#         print(response)
#
#
#
# asyncio.get_event_loop().run_until_complete(test())
# ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

def ws_message(ws, message):
    print("WebSocket thread: %s" % message)

def ws_open(ws):
    abob = ['']
    ws.send(
        '42["join",{"streamId":1101250,"channelId":1257895,"jwt":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxNTIwMTM1LCJ1c2VyX3JvbGUiOiJVU0VSIiwiaWF0IjoxNjYwMzM1NTQyLCJleHAiOjE2NjAzNjQzNDJ9.2SFZ5omIrz3EXH2Y5L_cfxn4ncEJ-Reo1bhpXOAKc48","excludeStickers":true}]' + "\n")
    ws.send(
        '42["message",{"streamId":1101250,"streamerId":1379611,"channelId":1257895,"jwt":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxNTIwMTM1LCJ1c2VyX3JvbGUiOiJVU0VSIiwiaWF0IjoxNjYwMzM1NTQyLCJleHAiOjE2NjAzNjQzNDJ9.2SFZ5omIrz3EXH2Y5L_cfxn4ncEJ-Reo1bhpXOAKc48","message":"как дела?"}]' + "\n")
def on_error(ws, error):
    print(error)

def ws_thread(*args):
    ws = websocket.WebSocketApp("wss://chat.wasd.tv/socket.io/?EIO=3&transport=websocket",  on_message = ws_message, on_error = on_error, on_open=ws_open)
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
    ws.send(
        '42["join",{"streamId":1101250,"channelId":1257895,"jwt":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxNTIwMTM1LCJ1c2VyX3JvbGUiOiJVU0VSIiwiaWF0IjoxNjYwMzM1NTQyLCJleHAiOjE2NjAzNjQzNDJ9.2SFZ5omIrz3EXH2Y5L_cfxn4ncEJ-Reo1bhpXOAKc48","excludeStickers":true}]')


_thread.start_new_thread(ws_thread, ())


while True:
    time.sleep(5)
    print("Main thread: %d" % time.time())