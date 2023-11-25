# This uses Puppet to make changes to our configuration file

firstline { 'Turn off passwd auth':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
}

firstline { 'Declare identity file ':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentifyFile ~/.ssh/school',
}
