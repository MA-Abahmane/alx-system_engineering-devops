#!/usr/bin/env bash
# Let’s practice using Puppet to make changes to our configuration file.
# Just as in the previous configuration file task, we’d like you to set up
# your client SSH configuration file so that you can connect to a server without
# typing a password.
# 
# Requirements:
#   Your SSH client configuration must be configured to use the private key ~/.ssh/school
#   Your SSH client configuration must be configured to refuse to authenticate using a password

# Make sure the file is present, if so; write contents.
file { 'etc/ssh_config':
ensure => present,
content => 
"
host*
PasswordAuthentication no
IdentityFile ~/.ssh/school
"
}
