package com.smallspider.service;

import com.smallspider.entity.JobInfo;
import com.smallspider.mapper.JobInfoMapper;

/**
 * Created by yangyang on 2016/12/4.
 */
public class JobInfoService {
    private JobInfoMapper jobInfoMapper;

    public JobInfoMapper getJobInfoMapper() {
        return jobInfoMapper;
    }

    public void setJobInfoMapper(JobInfoMapper jobInfoMapper) {
        this.jobInfoMapper = jobInfoMapper;
    }

    public void saveMessage(JobInfo jobInfo) {
        jobInfoMapper.add(jobInfo);
    }
}
