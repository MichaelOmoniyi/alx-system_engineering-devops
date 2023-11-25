# 0x0A. Configuration management
This project is focused on the usage of Puppet for Configuration Management.

## Tasks
* [ 0-create_a_file.pp ](./0-create_a_file.pp): Creates file in /tmp.
    * Requirements:
        * File path is /tmp/school
        * File permission is 0744
        * File owner is www-data
        * File group is www-data
        * File contains I love Puppet

* [ 1-install_a_package.pp ](./1-install_a_package.pp): Installs flask from  pip3.
    * Requirements:
        * Install flask
        * Version must be 2.1.0

* [ 2-execute_a_command.pp ](./2-execute_a_command.pp): Creates a manifest that kills a process named killmenow.
    * Requirements:
        * Must use the exec Puppet resource
        * Must use pkill
