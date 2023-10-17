# Create a Puppet script that modifies the open file limit for Nginx in the /etc/default/nginx file,
# you can use the file and exec resources. Here's an example Puppet manifest:

# Remove the line setting ULimit 
exec { 'remove_Nginx_ulimit':
  command => 'sed -i "/^ULIMIT/d" /etc/default/nginx',
  path    => ['/bin', '/usr/bin'],
}

# Restart Nginx service
exec { 'restart-nginx':
  command => 'service nginx restart',
  path    => ['/bin', '/usr/bin'],
}
