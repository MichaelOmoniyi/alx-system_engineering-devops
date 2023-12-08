# automate the task of creating a custom HTTP header response

exec {'header':
    provider => shell,
    command  => 'sudo apt-get update ; sudo apt-get -y install nginx ; sudo ufw allow 'Nginx Http' ; sudo mkdir -p /var/www/html ; sudo chmod -R 755 /var/www ; echo 'Hello World' | sudo tee /var/www/html/index.html ; echo "Ceci n'est pas une page" | sudo tee /var/www/html/404.html ; sudo sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By \$hostname;\n\trewrite ^\/redirect_me https:\/\/www.github.com/MichaelOmoniyi permanent;/" /etc/nginx/sites-enabled/default' ; sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\n\terror_page 404 \/404.html;\n\tlocation = \/404.html {\n\t\troot \/var\/www\/html;\n\t\tinternal;\n\t}" /etc/nginx/sites-enabled/default ; sudo service restart nginx',
            }
