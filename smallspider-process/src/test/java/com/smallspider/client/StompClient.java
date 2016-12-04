package com.smallspider.client;

import com.smallspider.activemq.StompListener;
import com.smallspider.communication.JobInfoConnector;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by yangyang on 2016/12/4.
 */
public class StompClient {
    public static void main(String[] args) throws Exception {
        StompListener listener = new StompListener(new JobInfoConnector("127.0.0.1", 61613));

        Map<String, String> params = new HashMap<String, String>();
        params.put("username", "user");
        params.put("password", "password");
        params.put("destination", "/topic/job51");
        params.put("ack","auto");
        params.put("timeout", "6000");

        listener.start(params);

        Thread thread = new Thread(listener);
        thread.start();

        Thread.sleep(100000);
        listener.stop();
    }
}
