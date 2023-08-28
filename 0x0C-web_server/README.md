# Web Server Cheat Sheet

## 1. Web Server Basics

- A web server is a software application or hardware device that serves web content to users' browsers upon request.
- Common web server software includes Apache, Nginx, Microsoft IIS, and LiteSpeed.

## 2. Important Concepts

- **HTTP:** Hypertext Transfer Protocol, the foundation of data communication on the web.
- **HTTPS:** HTTP Secure, an encrypted version of HTTP using SSL/TLS for secure data transfer.
- **IP Address:** A unique numerical label assigned to each device connected to a computer network.
- **Domain Name:** Human-readable name representing an IP address (e.g., www.example.com).

## 3. Common Commands

**Apache:**
- Start Apache: `sudo service apache2 start`
- Stop Apache: `sudo service apache2 stop`
- Restart Apache: `sudo service apache2 restart`
- Configuration File: `/etc/apache2/apache2.conf`

**Nginx:**
- Start Nginx: `sudo service nginx start`
- Stop Nginx: `sudo service nginx stop`
- Restart Nginx: `sudo service nginx restart`
- Configuration File: `/etc/nginx/nginx.conf`

## 4. Configuration Files

- Apache: `/etc/apache2/apache2.conf`, `/etc/apache2/sites-available/`
- Nginx: `/etc/nginx/nginx.conf`, `/etc/nginx/sites-available/`

## 5. Virtual Hosts

- Apache: Defined in separate configuration files under `/etc/apache2/sites-available/`.
- Nginx: Defined in server blocks within the main configuration file.

## 6. Security

- Keep software updated to patch security vulnerabilities.
- Use HTTPS to encrypt data transmission.
- Configure firewalls to allow only necessary traffic.
- Regularly monitor logs for suspicious activities.

## 7. Server-Side Scripting

- **PHP:** Hypertext Preprocessor; widely used for dynamic web content.
- **Python:** Can be used with web frameworks like Django or Flask.
- **Node.js:** Allows server-side JavaScript execution.

## 8. Reverse Proxy

- A server that sits between clients and web servers, forwarding client requests to the appropriate server.
- Commonly used for load balancing and caching.
- Nginx and Apache can act as reverse proxies.

## 9. Load Balancing

- Distributing incoming web traffic across multiple servers to ensure high availability and performance.
- Nginx and HAProxy are commonly used for load balancing.

## 10. Caching

- Storing copies of frequently accessed data to reduce server load and improve performance.
- Popular caching tools: Varnish, Memcached, Redis.

## 11. SSL/TLS Certificates

- Enable HTTPS by obtaining an SSL/TLS certificate from a certificate authority (CA) like Let's Encrypt.
- Certbot is a common tool for automating the SSL/TLS certificate setup process.

## 12. Monitoring and Logging

- Use monitoring tools like Nagios, Zabbix, or Prometheus to track server health.
- Analyze server logs (access logs, error logs) to identify issues and trends.

Remember that this is just a basic overview. Web server administration can be quite extensive, and there's a lot more to learn depending on your specific use case and requirements.
