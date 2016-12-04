# coding=utf-8
__author__ = 'yangyang'
from job51Spider import Job51Spider, JobInfoSearcher
from job51MQListener import Job51MQListener
from mq.activemqConnector import ActiveMQConnector
import json

start_url = 'http://search.51job.com/list/180200,000000,0000,00,9,99,Java%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
next_url = ''
default_dict = {'id': 'resultList', 'regexp_el': 'div', 'regexp_span': 'span'}
mq_server = {'host': '127.0.0.1', 'port': '61613', 'username': 'user', 'password': 'password'}
destination = '/topic/job51'


if __name__ == '__main__':
    activemq_connector = ActiveMQConnector(mq_server.get('host'), mq_server.get('port'))
    connection = activemq_connector.create_connection(Job51MQListener())
    activemq_connector.connect(connection, mq_server.get('username'), mq_server.get('password'))
    #activemq_connector.subscribe(connection, destination)

    html = Job51Spider.catch_html(start_url)
    total_index = JobInfoSearcher.search_total_index(html)
    for i in range(0, total_index):
        if i == 0:
            first_results = JobInfoSearcher.find_job_info(html, default_dict)
            for j in first_results:
                j_dict = j.__dict__
                j_json = json.dumps(j_dict, ensure_ascii=False)
                activemq_connector.send(connection, j_json, destination)
            next_url = JobInfoSearcher.search_next_url(html)
        elif i > 0:
            next_html = Job51Spider.catch_html(next_url)
            next_results = JobInfoSearcher.find_job_info(next_html, default_dict)
            for k in next_results:
                k_dict = k.__dict__
                k_json = json.dumps(k_dict, ensure_ascii=False)
                activemq_connector.send(connection, k_json, destination)
            next_url = JobInfoSearcher.search_next_url(next_html)

            if next_url is None:
                break

    activemq_connector.close_connection(connection)