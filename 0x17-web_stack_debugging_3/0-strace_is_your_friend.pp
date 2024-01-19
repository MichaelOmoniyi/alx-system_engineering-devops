# Fixes 500 error

exec { 'replace_line':
    provider => shell,
    command  => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"
}
