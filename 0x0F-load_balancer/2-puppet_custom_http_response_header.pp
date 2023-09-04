# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Manage the custom HTTP header in the Nginx configuration
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "server {\n  listen 80 default_server;\n  server_name _;\n\n  location / {\n    add_header X-Served-By $hostname;\n  }\n}\n",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => running,
  enable => true,
}