# coding=utf8
"""
Simple TCP socket client
Copyright (c) 2023 webtoucher
Distributed under the BSD 3-Clause license. See LICENSE for more info.
"""

import queue
import socket

from datetime import datetime
from eventemitter import EventEmitter
from threading import Thread
from typing import Optional


class SimpleSocketClientException(socket.error):
    pass


class SimpleSocketClient(EventEmitter):
    def __init__(self, host: str, port: int):
        self.__host = host
        self.__port = port
        self.__socket = None
        self.__thread = None
        self.__outgoing_messages = None
        self.__connected = False
        self.__keep_answer = False

    def connect(self) -> None:
        self.__thread = Thread(target=self.__threading, args=(self,))
        self.__thread.start()
        while not client.__connected:
            pass

    def disconnect(self) -> None:
        self.__connected = False

    @staticmethod
    def __threading(client):
        client.__incoming_messages = queue.Queue()
        client.__outgoing_messages = queue.Queue()
        client.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if client.__socket.fileno() < 0:
            raise SimpleSocketClientException('Error with creating sockets')
        client.__socket.connect((client.__host, client.__port))
        client.__connected = True
        client.emit('connect', (client.__host, client.__port))
        while client.__connected:
            try:
                if client.__socket.fileno() > 0:
                    message = client.__outgoing_messages.get_nowait()
                else:
                    client.disconnect()
                    continue
            except queue.Empty:
                continue

            try:
                if message:
                    client.__socket.sendall(message)
                    if client.__keep_answer:
                        client.__receive_message()
            except ConnectionResetError:
                client.disconnect()

        client.emit('disconnect', (client.__host, client.__port))
        client.__incoming_messages = None
        client.__outgoing_messages = None
        client.__socket.close()
        client.__socket = None

    def send(self, message: bytes) -> None:
        if not self.__connected:
            raise SimpleSocketClientException()
        self.__outgoing_messages.put(message)

    def ask(self, message: bytes, timeout=1.) -> Optional[bytes]:
        self.__keep_answer = True

        try:
            self.send(message)
        except SimpleSocketClientException as err:
            self.__keep_answer = False
            raise err

        start_time = datetime.now()
        while True:
            if not self.__connected:
                self.__keep_answer = False
                raise SimpleSocketClientException()
            if (datetime.now() - start_time).total_seconds() > timeout:
                self.__keep_answer = False
                raise TimeoutError
            try:
                answer = self.__incoming_messages.get_nowait()
                self.__keep_answer = False
                return answer
            except queue.Empty:
                continue

    def __receive_message(self):
        data_from_server = self.__socket.recv(1024)
        if data_from_server:
            self.__incoming_messages.put(data_from_server)

    def __disconnected(self):
        self.__thread.join()


if __name__ == '__main__':
    pass
