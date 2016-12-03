# coding=utf-8
__author__ = 'yangyang'

import urllib2
import re


class SmallSpider:
    def __init__(self):
        pass

    @staticmethod
    def _catch_url(url):
        request_header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'close'
        }
        request_timeout = 1000
        request = urllib2.Request(url, None, request_header)
        response = urllib2.urlopen(request, None, request_timeout)

        return response


class Searcher:
    def __init__(self):
        pass

    @staticmethod
    def findall_element_by_id(soup, id):
        return soup.find_all(id=id)

    @staticmethod
    def findall_element_by_regexp(soup, regexp):
        return soup.find_all(re.compile(regexp))