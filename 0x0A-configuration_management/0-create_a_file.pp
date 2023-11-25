# Creates a file in /tmp

file { 'school':
    path    => '/tmp/school',
    group   => 'www-data',
    mode    => '0744',
    owner   => 'www-data',
    content => 'I love Puppet',
}
