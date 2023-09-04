#  Here we automate the task of creating a custom HTTP header response using Puppet
#  Requirements:
#   - The name of the custom HTTP header must be X-Served-By
#   - The value of the custom HTTP header must be the hostname of the server Nginx is running on

# Make sure nginx is Installed
exec { 'install nginx':
  command  => 'sudo apt-get update -y;
	sudo apt-get install nginx -y;',
  provider => shell,
}

# creating a custom HTTP header response
exec { 'custom http header':
  command  => 'sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default
	sudo service nginx restart',
  provider => shell,
}
