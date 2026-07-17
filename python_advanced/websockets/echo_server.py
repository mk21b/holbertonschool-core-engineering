#!/usr/bin/env python3
"""A minimal WebSocket echo server built with the websockets library."""

import asyncio
from websockets.asyncio.server import serve


async def connection_handler(websocket):
    """Send every incoming text message back to the sender."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the WebSocket server on localhost:8765 and run it forever."""
    async with serve(connection_handler, "localhost", 8765) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
