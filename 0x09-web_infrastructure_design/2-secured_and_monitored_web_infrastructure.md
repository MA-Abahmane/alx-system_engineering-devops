
![alt text](https://github.com/MA-Abahmane/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure.png?raw=true)


On a whiteboard, design a three-server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.

# Requirements:
 
# You must add:
3 firewalls
1 SSL certificate to serve www.foobar.com over HTTPS
3 monitoring clients (data collector for Sumologic or other monitoring services)


# You must be able to explain some specifics about this infrastructure:

For every additional element, why you are adding it
- 
What are firewalls for
-
- a firewall is a network security system that monitors and controls
 incoming and outgoing network traffic based on predetermined security
 rules. A firewall typically establishes a barrier between a trusted 
 network and an untrusted network, such as the Internet.

Why is the traffic served over HTTPS
-
- HTTPS uses the SSL/TLS protocol to encrypt communications so that attackers can't steal data. SSL/TLS also confirms that a website server is who it says it is, preventing impersonations. This stops multiple kinds of cyber attacks (just like food safety prevents illness).
 
What monitoring is used for
- 
- Monitoring is a process to periodically collect, analyse and use information to actively manage performance, maximise positive impacts and minimise the risk of adverse impacts.

How the monitoring tool is collecting data
-
- Data collection is the process of systematically gathering quantitative and/or qualitative data used for purposes of monitoring, evaluation, and/or learning (MEL). Performance monitoring data are used to reveal whether project and activity implementation is on track and whether expected results are being achieved.

Explain what to do if you want to monitor your web server QPS
-
- to monitor your web server QPS you need to
Identify the metrics you want to monitor.
Choose a monitoring tool.
Configure the monitoring tool.
Collect data.
Analyze the data.


# You must be able to explain what the issues are with this infrastructure:

Why terminating SSL at the load balancer level is an issue
-
- 
Terminating SSL at the load balancer level can be an issue because it exposes unencrypted traffic between the load balancer and the back-end servers. This can be a security risk, as an attacker could intercept the traffic and read sensitive data.

Why having only one MySQL server capable of accepting writes is an issue
-
- Having only one MySQL server capable of accepting writes is an issue because it creates a single point of failure. If that server goes down, no new writes can be made to the database, which can cause a significant disruption to your application.

Why having servers with all the same components (database, web server and application server) might be a problem
-
- There are a few reasons why having servers with all the same components (database, web server, and application server) might be a problem:

- Single point of failure: If one server goes down, all of the components on that server will be unavailable. This could include the database, the web server, and the         
    application server.
- Security risk: If one server is compromised, all of the components on that server could be compromised. This could include the database, the web server, and the application     server.
- Difficult to manage: It can be difficult to manage servers with all the same components. This is because you need to make sure that all of the components are configured         correctly and that they are all up to date.
- Not scalable: If you need to increase the capacity of your servers, you will need to increase the capacity of all of the components on those servers. This can be expensive      and time-consuming.

