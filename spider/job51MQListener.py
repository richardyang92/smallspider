# coding=utf-8
__author__ = 'yangyang'

from mq.activemqConnector import ListenerBase


class Job51MQListener(ListenerBase):
    def on_message(self, headers, message):
        super(Job51MQListener, self).on_message(headers, message)