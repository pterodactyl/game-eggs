#!/usr/bin/env python3
import argparse
import random
import socket
import struct
import sys
import time
from dataclasses import dataclass
from typing import List


SERVERDATA_RESPONSE_VALUE = 0
SERVERDATA_EXECCOMMAND = 2
SERVERDATA_AUTH_RESPONSE = 2
SERVERDATA_AUTH = 3


@dataclass
class RconPacket:
    request_id: int
    packet_type: int
    body: str


class RconClient:
    def __init__(self, host: str, port: int, timeout: float, debug: bool = False):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.debug = debug
        self.sock: socket.socket | None = None

    def connect(self) -> None:
        self.sock = socket.create_connection((self.host, self.port), timeout=self.timeout)
        self.sock.settimeout(self.timeout)
        if self.debug:
            print(f"[DEBUG] Connected to {self.host}:{self.port}")

    def close(self) -> None:
        if self.sock:
            self.sock.close()
            self.sock = None

    def _send_packet(self, request_id: int, packet_type: int, body: str) -> None:
        if not self.sock:
            raise RuntimeError("Socket is not connected")

        payload = body.encode("utf-8") + b"\x00\x00"
        packet = struct.pack("<ii", request_id, packet_type) + payload
        data = struct.pack("<i", len(packet)) + packet
        self.sock.sendall(data)

        if self.debug:
            print(
                f"[DEBUG] -> SEND id={request_id} type={packet_type} len={len(packet)} body={body!r}"
            )
            print(f"[DEBUG] -> HEX  {data.hex(' ')}")

    def _recv_packet(self) -> RconPacket:
        if not self.sock:
            raise RuntimeError("Socket is not connected")

        raw_size = self._recv_exact(4)
        size = struct.unpack("<i", raw_size)[0]
        if size < 10:
            raise ValueError(f"Invalid packet size: {size}")

        raw_packet = self._recv_exact(size)
        request_id, packet_type = struct.unpack("<ii", raw_packet[:8])

        raw_body = raw_packet[8:-2]
        body = raw_body.decode("utf-8", errors="replace")

        if self.debug:
            print(
                f"[DEBUG] <- RECV id={request_id} type={packet_type} len={size} body={body!r}"
            )
            print(f"[DEBUG] <- HEX  {raw_size.hex(' ')} {raw_packet.hex(' ')}")

        return RconPacket(request_id=request_id, packet_type=packet_type, body=body)

    def _recv_exact(self, n: int) -> bytes:
        if not self.sock:
            raise RuntimeError("Socket is not connected")

        chunks: List[bytes] = []
        remaining = n
        while remaining > 0:
            chunk = self.sock.recv(remaining)
            if not chunk:
                raise ConnectionError("Connection closed by remote host")
            chunks.append(chunk)
            remaining -= len(chunk)
        return b"".join(chunks)

    def authenticate(self, password: str) -> bool:
        auth_id = random.randint(1, 2_000_000_000)
        self._send_packet(auth_id, SERVERDATA_AUTH, password)

        deadline = time.time() + self.timeout
        got_auth_response = False

        while time.time() < deadline:
            try:
                packet = self._recv_packet()
            except socket.timeout:
                break

            if packet.packet_type == SERVERDATA_AUTH_RESPONSE:
                got_auth_response = True
                if packet.request_id == -1:
                    return False
                if packet.request_id == auth_id:
                    return True

        return got_auth_response

    def execute(self, command: str, settle_time: float, idle_timeout: float) -> list[RconPacket]:
        command_id = random.randint(1, 2_000_000_000)
        self._send_packet(command_id, SERVERDATA_EXECCOMMAND, command)

        packets: list[RconPacket] = []
        end_time = time.time() + max(settle_time, 0)

        while time.time() < end_time:
            try:
                packet = self._recv_packet()
                packets.append(packet)
                end_time = time.time() + idle_timeout
            except socket.timeout:
                break
            except ConnectionError:
                break

        return packets


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Low-level RCON probe for troubleshooting server/client protocol issues"
    )
    parser.add_argument("--host", required=True, help="RCON host")
    parser.add_argument("--port", required=True, type=int, help="RCON TCP port")
    parser.add_argument("--password", required=True, help="RCON password")
    parser.add_argument(
        "--command",
        action="append",
        default=[],
        help="Command to execute (use multiple --command for multiple commands)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=3.0,
        help="Socket timeout in seconds (default: 3.0)",
    )
    parser.add_argument(
        "--settle-time",
        type=float,
        default=2.0,
        help="Initial max wait for command responses in seconds (default: 2.0)",
    )
    parser.add_argument(
        "--idle-timeout",
        type=float,
        default=0.35,
        help="Wait extension after each received packet in seconds (default: 0.35)",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Print packet-level debug including hex bytes",
    )

    args = parser.parse_args()

    commands = args.command or ["info"]

    client = RconClient(args.host, args.port, args.timeout, debug=args.debug)

    try:
        client.connect()

        authenticated = client.authenticate(args.password)
        if not authenticated:
            print("AUTH FAILED")
            return 2

        print("AUTH OK")

        for index, command in enumerate(commands, start=1):
            print(f"\n=== COMMAND {index}: {command} ===")
            packets = client.execute(
                command=command,
                settle_time=args.settle_time,
                idle_timeout=args.idle_timeout,
            )

            if not packets:
                print("No response packets received (empty/timed out).")
                continue

            for i, packet in enumerate(packets, start=1):
                printable_body = packet.body if packet.body else "<EMPTY>"
                print(
                    f"[{i}] id={packet.request_id} type={packet.packet_type} body={printable_body}"
                )

    except (TimeoutError, socket.timeout):
        print("Timeout while connecting/reading packets")
        return 3
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1
    finally:
        client.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
