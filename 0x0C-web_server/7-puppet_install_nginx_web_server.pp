# #!/usr/bin/env bash
# Time to practice configuring your server with Puppet! Just as you did before,
# we’d like you to install and configure an Nginx server using Puppet instead of
# Bash. To save time and effort, you should also include resources in your
# manifest to perform a 301 redirect when querying /redirect_me.
# Requirements:
#  - Nginx should be listening on port 80
#  - When querying Nginx at its root / with a GET request (requesting a page) using curl,
#   it must return a page that contains the string Hello World!
#  - The redirection must be a “301 Moved Permanently”
#  - Your answer file should be a Puppet manifest containing commands to automatically
#   configure an Ubuntu machine to respect the above requirements    


# Make sure Nginx is installed
package { 'nginx':
ensure => installed,
}

# The redirection is Moved Permanently to my GitHub page and Nginx is listening on port 80
$redirectPage = "https://www.github.com/MA-Abahmane"
file_line { 'install':
ensure => 'present',
path   => '/etc/nginx/sites-available/default',
after  => 'listen 80 default_server;',
line   => 'rewrite ^/redirect_me $redirectPage permanent;',
}

# Create a web index page containing the string 'Hello World!'
$pageMessage = "Hello World!"
file { '/var/www/html/index.html':
content => "$pageMessage"
}

# Rerun nginx service
service { 'nginx':
ensure  => running,
require => Package['nginx'],
}
