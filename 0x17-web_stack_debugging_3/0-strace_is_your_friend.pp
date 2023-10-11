# I found the bug! In the wordpress file there was a file called 'wp-settings.php' with the extension 'phpp'.

exec {'Fix File Extension':
    command => 'sed -i "s/\b.phpp\b/.php/g" /var/www/html/wp-settings.php'
}
