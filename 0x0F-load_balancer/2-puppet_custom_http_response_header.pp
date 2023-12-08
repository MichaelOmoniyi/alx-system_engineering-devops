# automate the task of creating a custom HTTP header response

exec {'header':
    provider => shell,
    command  => 'sed -i "s/server_name _;\n\tserver_name _;\n\tadd_header X-Served-By \$hostname;" /etc/nginx/sites-enabled/default',
            }
