package com.smallspider.activemq;

import org.apache.activemq.transport.stomp.StompConnection;

import java.io.IOException;

/**
 * Created by yangyang on 2016/12/4.
 */
public abstract class StompConnectorBase {
    protected String host;
    protected int port;

    public StompConnectorBase(String host, int port) {
        this.host = host;
        this.port = port;
    }

    public StompConnection createConnection() {
        StompConnection connection = new StompConnection();
        try {
            connection.open(host, port);
            return connection;
        } catch (IOException e) {
            return null;
        }
    }

    public void connect(StompConnection connection, String username, String password) throws Exception {
        connection.connect(username, password);
    }

    public void subscribe(StompConnection connection, String destination, String ack) throws Exception {
        connection.subscribe(destination, ack);
    }

    public void closeConnection(StompConnection connection) throws IOException {
        connection.close();
    }

    public abstract void onMessage(String message);
}
