
![alt text](https://github.com/MA-Abahmane/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack.png?raw=true)


# A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a LAMP stack.
-
- On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via www.foobar.com. Start your explanation by having a user wanting to access your website.


# Requirements:

- You must use:
1 server
1 web server (Nginx)
1 application server
1 application files (your code base)
1 database (MySQL)
1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

- You must be able to explain some specifics about this infrastructure:
  
What is a server
-
- Servers act as platforms for sharing data (images & files) and applications
(email and drive) across various devices.

What is the role of the domain name
-
- Purpose. Domain names serve to identify Internet resources, such as computers, networks, and services,
- with a text-based label that is easier to memorize than the numerical addresses used in the Internet protocols.

What type of DNS record www is in www.foobar.com
-
- www is a CNAME (Canonical Name) DNS record-type in www.foobar.com since it also points to the same IP address as foobar.com
and if the IP address changes we can only record changes in the DNS A record of foobar.com .

What is the role of the web server
-
- The main job of a web server is to display website content through storing, processing and delivering webpages to users.

What is the role of the application server
-
- The function of the application server is to act as host (or container) for the user's business logic while facilitating
access to and performance of the business application.

What is the role of the database
-
- Database software makes data management simpler by enabling users to store data in a structured form and then access it.

What is the server using to communicate with the computer of the user requesting the website
-
- HyperText Transfer Protocol (HTTP)


You must be able to explain what the issues are with this infrastructure:
-

SPOF
-
- A single point of failure (SPOF) is essentially a flaw in the design, configuration, or implementation of a system, circuit
- Without a load balancer in place, the server runs the risk of becoming overwhelmed, ultimately leading to its eventual collapse and subsequent loss of connections to the server.
Downtime when maintenance needed (like deploying new code web server needs to be restarted)

Cannot scale if too much incoming traffic
-
- In the absence of a load balancer, the server faces the imminent risk of being overwhelmed, resulting in its eventual breakdown and the subsequent loss of connections to it.
