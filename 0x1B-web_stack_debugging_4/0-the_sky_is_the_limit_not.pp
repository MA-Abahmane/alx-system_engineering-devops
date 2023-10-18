# Create a Puppet script that modifies the open file limit for Nginx in the /etc/default/nginx file,

# Remove the line setting ULimit
# Restart Nginx service
exec { 'remove_Nginx_ulimit':
  command => 'sed -i "/^ULIMIT/d" /etc/default/nginx && sudo service nginx restart',
  path    => ['/bin', '/usr/bin'],
}
