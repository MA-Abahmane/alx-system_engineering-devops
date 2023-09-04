#!/usr/bin/env bash
#  Here we automate the task of creating a custom HTTP header response using Puppet
#  Requirements:
#   - The name of the custom HTTP header must be X-Served-By
#   - The value of the custom HTTP header must be the hostname of the server Nginx is running on

# Make sure nginx is Installed
package { 'nginx':
ensure => installed,
}

# creating a custom HTTP header response
exec { 'http header response':
command  =>
'sudo apt-get update;
sudo apt-get install -y nginx;

sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default;

sudo service nginx restart;',
provider => shell,
}

# Make sure nginx service is on
server { 'nginx':
ensure => running,
enable => true,
}