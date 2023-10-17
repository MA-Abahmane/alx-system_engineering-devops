-- Create a Puppet script that modifies the open file limit for Nginx in the /etc/default/nginx file,
-- you can use the file and exec resources. Here's an example Puppet manifest:

class nginx_disable_ulimit {
  package { 'augeas-tools':
    ensure => installed,
  }

  augeas { 'comment_ulimit_line':
    context => '/files/etc/default/nginx',
    changes => [
      'set ULIMIT "# ULIMIT line commented by Puppet"',
    ],
  }
}