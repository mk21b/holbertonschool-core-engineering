#!/usr/bin/env python3
"""A WebSocket server that unicasts each message back
to its sender with U:."""

import asyncio
from websockets.asyncio.server import serve


connected_clients = set()


async def connection_handler(websocket):
    """Unicast each message back to its sender with U:."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    finally:
        connected_clients.remove(websocket)


async def main():
    """Start the WebSocket server on localhost:8765 and run it forever."""
    async with serve(connection_handler, "localhost", 8765) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
