# coding=utf-8
__author__ = 'yangyang'

import stomp


class ListenerBase(object):
    def on_error(self, headers, message):
        print('received an error %s' % message.decode('utf-8').encode('gbk'))
    def on_message(self, headers, message):
        print('received a message %s' % message.decode('utf-8').encode('gbk'))


class ActiveMQConnector:
    def __init__(self, host, port):
        self.__host = host
        self.__port = port

    def create_connection(self, listener):
        connection = stomp.Connection([(self.__host,self.__port)])
        connection.set_listener('', listener)
        connection.start()
        return connection

    def connect(self, connection, username, password):
        connection.connect(username, password)

    def subscribe(self, connection, destination, id=1, ack='auto'):
        connection.subscribe(destination=destination, id=id, ack=ack)

    def send(self, connection, messgae, destination):
        connection.send(body=messgae, destination=destination)

    def close_connection(self, connection):
        connection.disconnect()