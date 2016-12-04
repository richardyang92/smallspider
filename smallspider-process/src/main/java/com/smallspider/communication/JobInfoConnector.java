package com.smallspider.communication;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.TypeReference;
import com.smallspider.activemq.StompConnectorBase;
import com.smallspider.entity.JobInfo;
import com.smallspider.service.JobInfoService;

import java.util.Map;

/**
 * Created by yangyang on 2016/12/4.
 */
public class JobInfoConnector extends StompConnectorBase {
    private JobInfoService jobInfoService;

    public JobInfoService getJobInfoService() {
        return jobInfoService;
    }

    public void setJobInfoService(JobInfoService jobInfoService) {
        this.jobInfoService = jobInfoService;
    }

    public JobInfoConnector(String host, int port) {
        super(host, port);
    }

    @Override
    public void onMessage(String message) {
        System.out.println("message received from Python: " + message);
        Map<String, Object> map = JSON.parseObject(
                message, new TypeReference<Map<String, Object>>() {});

        JobInfo jobInfo = new JobInfo();
        for (Map.Entry<String, Object>  entry : map.entrySet()) {
            String key = entry.getKey();
            String value = (String) entry.getValue();

            if (key.equals("_JobInfo__job_name")) {
                jobInfo.setJobName(value);
            } else if (key.equals("_JobInfo__company_name")) {
                jobInfo.setCompanyName(value);
            } else if (key.equals("_JobInfo__company_link")) {
                jobInfo.setCompanyLink(value);
            } else if (key.equals("_JobInfo__address")) {
                jobInfo.setAddress(value);
            } else if (key.equals("_JobInfo__publish_time")) {
                jobInfo.setPublishTime(value);
            } else if (key.equals("_JobInfo__payments")) {
                jobInfo.setPayments(value);
            }
        }
        jobInfoService.saveMessage(jobInfo);
    }
}
