package com.smallspider.client;

import com.smallspider.activemq.StompListener;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by yangyang on 2016/12/4.
 */
public class JobInfoClient {
    public static void main(String[] args) throws Exception {
        ApplicationContext context = new ClassPathXmlApplicationContext("classpath:META-INF/spring/applicationContext.xml");
/*        JobInfo jobInfo = new JobInfo();
        jobInfo.setJobName("JAVA开发工程师");
        jobInfo.setCompanyName("scsdcwedqw");
        jobInfo.setCompanyLink("http://jobs.51job.com/all/co4058443.html");
        jobInfo.setAddress("csdcsdecw");
        jobInfo.setPayments("6000-9000/月");
        jobInfo.setPublishTime("11-27");*/

        Map<String, String> params = new HashMap<String, String>();
        params.put("username", "user");
        params.put("password", "password");
        params.put("destination", "/topic/job51");
        params.put("ack", "auto");
        params.put("timeout", "6000");

        StompListener listener = (StompListener) context.getBean("stompListener");
        listener.start(params);

        Thread thread = new Thread(listener);
        thread.start();

        Thread.sleep(100000);
        listener.stop();

    }
}
