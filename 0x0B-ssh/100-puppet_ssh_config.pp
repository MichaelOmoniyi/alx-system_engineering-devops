# This uses Puppet to make changes to our configuration file
exec { 'echo':
    path    => 'usr/bin:/bin',
    command => 'echo "      Identityfile ~/.ssh/school      PasswordAuthentication no" >> /etc/ssh/ssh_config',
    returns  => [0,1],
}
