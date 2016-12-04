package com.smallspider.activemq;

import org.apache.activemq.transport.stomp.StompConnection;
import org.apache.activemq.transport.stomp.StompFrame;

import java.util.Map;

/**
 * Created by yangyang on 2016/12/4.
 */
public class StompListener implements Runnable {
    private StompConnectorBase stompConnector;
    private StompConnection connection;
    private boolean runFlag;
    private int timeout;

    public StompListener(StompConnectorBase stompConnector) {
        this.stompConnector = stompConnector;
        this.connection = stompConnector.createConnection();
    }

    public void setTimeout(int timeout) {
        this.timeout = timeout;
    }

    public StompListener start(Map<String, String> params) throws Exception {
        stompConnector.connect(this.connection, params.get("username"), params.get("password"));
        stompConnector.subscribe(this.connection, params.get("destination"), params.get("ack"));
        this.timeout = Integer.parseInt(params.get("timeout"));
        this.runFlag = true;
        return this;
    }

    public void stop() throws Exception {
        this.runFlag = false;
        stompConnector.closeConnection(connection);
    }

    public void run() {
        while (runFlag) {
            try {
                StompFrame message = connection.receive(timeout);
                String textMessage = message.getBody();

                if (textMessage != null) {
                    System.out.println("接收到消息了！");
                    stompConnector.onMessage(textMessage);
                }
            } catch (Exception e) {
                //
            }
            try {
                Thread.sleep(10);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
