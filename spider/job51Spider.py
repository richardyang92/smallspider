# coding=utf-8
__author__ = 'yangyang'
from spider import SmallSpider
from spider import Searcher
from bs4 import BeautifulSoup
import re


class Job51Spider(SmallSpider):
    def __init__(self, start_url):
        SmallSpider.__init__(self)
        self.__startURL = start_url

    @property
    def start_url(self):
        return self.__startURL

    @staticmethod
    def catch_html(url):
        return SmallSpider._catch_url(url).read()


class JobInfo:
    def __init__(self):
        self.__job_name = ''
        self.__company_name = ''
        self.__company_link = ''
        self.__address = ''
        self.__payments = ''
        self.__publish_time = ''

    def set_job_name(self, job_name):
        self.__job_name = job_name

    def get_job_name(self):
        return self.__job_name

    def set_company_name(self, job_name):
        self.__company_name = job_name

    def get_company_name(self):
        return self.__company_name

    def set_company_link(self, company_link):
        self.__company_link = company_link

    def get_company_link(self):
        return self.__company_link

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def set_payments(self, payments):
        self.__payments = payments

    def get_payments(self):
        return self.__payments

    def set_publish_time(self, publish_time):
        self.__publish_time = publish_time

    def get_publish_time(self):
        return self.__publish_time


class JobInfoSearcher:
    def __init__(self):
        pass

    @staticmethod
    def find_job_info(html, dict):
        bs = BeautifulSoup(html, 'lxml')
        job_info_list = Searcher.findall_element_by_id(bs, dict.get('id'))

        job_info_obj_list = []
        if job_info_list.__len__() == 1:
            job_form = job_info_list[0]
            job_form_els = Searcher.findall_element_by_regexp(job_form, dict.get('regexp_el'))
            for job_form_el in job_form_els:
                if job_form_el['class'] == ['el']:
                    span_list = Searcher.findall_element_by_regexp(job_form_el, dict.get('regexp_span'))
                    job_info_obj = JobInfo()
                    for span in span_list:
                        if not span.has_attr('class'):
                            job_info_obj.set_job_name(span.a.string.strip())
                            #print job_info_obj.get_job_name()
                        else:
                            if span['class'] == ['t2']:
                                job_info_obj.set_company_name(span.a.string)
                                job_info_obj.set_company_link(span.a['href'])
                                #print job_info_obj.get_company_name()
                                #print job_info_obj.get_company_link()
                            elif span['class'] == ['t3']:
                                job_info_obj.set_address(span.string)
                                #print job_info_obj.get_address()
                            elif span['class'] == ['t4']:
                                job_info_obj.set_payments(span.string)
                                #print job_info_obj.get_payments()
                            elif span['class'] == ['t5']:
                                job_info_obj.set_publish_time(span.string)
                                #print job_info_obj.get_publish_time()
                    job_info_obj_list.append(job_info_obj)
        return job_info_obj_list

    @staticmethod
    def search_total_index(html):
        total_index_pattern = re.compile('<span class="td".*?</span>')
        match = re.search(total_index_pattern, html)
        match_string = match.group().split(u'<span class="td">共'.encode('gbk'))[1].split(u'页，到第</span>'.encode('gbk'))[0]
        return int(match_string)

    @staticmethod
    def search_next_url(html):
        bs = BeautifulSoup(html, 'lxml')
        div_list = Searcher.findall_element_by_regexp(bs, 'div')

        for div in div_list:
            if div.has_attr('class') and div['class'] == ['dw_page']:
                li_list = Searcher.findall_element_by_regexp(div, 'li')
                for li in li_list:
                    if li.has_attr('class') and li['class'] == ['bk']:
                        a_lists = Searcher.findall_element_by_regexp(li, '^a')
                        for a_list in a_lists:
                            if a_list.string == u'下一页':
                                return a_list['href']