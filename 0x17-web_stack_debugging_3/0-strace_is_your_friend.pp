# Replaces a line in a file in server

$file = '/var/www/html/wp-setting.php'

exec { 'replace_line':
    command => "sed -i 's/phpp/php/g' ${file}",
    path    => ['/bin','/usr/bin']
}
