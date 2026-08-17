import websockets, asyncio

client_list = set()


async def broadcast(message):
    for client in client_list:
        await client.send(message)

async def handler(websocket):
    client_list.add(websocket)

    try:
        async for message in websocket:
            print(f"Client: {message}")

            await broadcast(message)
    finally:
        client_list.remove(websocket)


async def main():
    async with websockets.serve(handler, "localhost", 8000):
        print("Server started")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())


