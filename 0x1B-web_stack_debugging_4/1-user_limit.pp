# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.

# Removes all hard and soft limits from the holberton user
exec { 'RemoveLimitsDel':
    command  => "sed -i "/^holberton/d" /etc/security/limits.conf",
    provider => shell,
}
