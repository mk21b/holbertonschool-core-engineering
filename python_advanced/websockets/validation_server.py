#!/usr/bin/env python3
"""A WebSocket server that validates messages (OK: / ERR:EMPTY)."""

import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    """Validate each message and reply with OK: or ERR:EMPTY."""
    try:
        async for message in websocket:
            if len(message.strip()) == 0:
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{message}")
    except ConnectionClosed:
        pass


async def main():
    """Start the WebSocket server on localhost:8765 and run it forever."""
    async with serve(connection_handler, "localhost", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
