import websockets
import asyncio
import json


async def consumer_handler(frames):
    async for frame in frames:
        trade = json.loads(frame)
        """
        {'e': 'trade', 'E': 1626174462256, 's': 'BTCUSDT', 't': 954321238, 'p': '32969.44000000', 'q': '0.00097300',
         'b': 6818067079, 'a': 6818068546, 'T': 1626174462255, 'm': True, 'M': True}
        """
        print(trade)


async def connect():
    async with websockets.connect("wss://stream.binance.com:9443/ws/btcusdt@trade") as ws:
        await consumer_handler(ws)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(connect())
    loop.run_forever()
