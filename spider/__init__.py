# coding=utf-8
__author__ = 'yangyang'
from job51Spider import Job51Spider
from job51Spider import JobInfoSearcher

if __name__ == '__main__':
    html = Job51Spider.catch_html("http://search.51job.com/list/180200,000000,0000,00,9,99,Java%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=")

    jobinfo_searcher = JobInfoSearcher()
    jobinfo_searcher.findall_job_info(html, {'id': 'resultList', 'regexp_el': 'div', 'regexp_span':'span'})