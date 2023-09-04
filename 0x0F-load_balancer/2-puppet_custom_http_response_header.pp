# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Create a custom Nginx config file
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('your_module/custom_headers.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => running,
  enable => true,
}
