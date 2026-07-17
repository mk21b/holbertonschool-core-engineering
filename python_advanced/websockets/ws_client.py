#!/usr/bin/env python3
"""A minimal WebSocket client built with the websockets library."""

import os
import asyncio
from websockets.asyncio.client import connect


async def connect_and_send(uri: str, text: str) -> str:
    """Open a connection, send text once, and return the reply."""
    async with connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        return response


async def main():
    """Send one message to the server and print its reply."""
    uri = os.environ.get("WS_URI", "ws://localhost:8765")
    message = "demo"
    response = await connect_and_send(uri, message)
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
