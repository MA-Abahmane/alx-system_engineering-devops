# Using Puppet, create a manifest that kills a process named killmenow.# 
# Requirements:
#   Must use the exec Puppet resource
#   Must use pkill

exec { 'Kill_Process':
command             => 'pkill -f killmenow',
onlyif              => 'pgrep -f killmenow',
path                => ['/bin/bash', '/user/bin', '/bin'],
}
