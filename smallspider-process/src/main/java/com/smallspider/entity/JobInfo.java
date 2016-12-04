package com.smallspider.entity;

/**
 * Created by yangyang on 2016/12/4.
 */
public class JobInfo {
    private int id;
    private String jobName;
    private String companyName;
    private String companyLink;
    private String address;
    private String payments;
    private String publishTime;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getJobName() {
        return jobName;
    }

    public void setJobName(String jobName) {
        this.jobName = jobName;
    }

    public String getCompanyName() {
        return companyName;
    }

    public void setCompanyName(String companyName) {
        this.companyName = companyName;
    }

    public String getCompanyLink() {
        return companyLink;
    }

    public void setCompanyLink(String companyLink) {
        this.companyLink = companyLink;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPayments() {
        return payments;
    }

    public void setPayments(String payments) {
        this.payments = payments;
    }

    public String getPublishTime() {
        return publishTime;
    }

    public void setPublishTime(String publishTime) {
        this.publishTime = publishTime;
    }
}
