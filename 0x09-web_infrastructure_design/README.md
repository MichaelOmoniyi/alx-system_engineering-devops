#0x09. Web infrastructure design

This project is based on whiteboarding various web infrastructures.

##Tasks
* **[ 0-simple_web_stack ](./0-simple_web_stack)**  This file contains the link to the whiteboarding on a web infrastructure based on:
    * 1 server
    * 1 web server (Nginx)
    * 1 application server
    * 1 application files (your code base)
    * 1 database (MySQL)
    * 1 domain name foobar.com configured with a www record that points to the server IP 8.8.8.8

* **[ 1-distributed_web_infrastructure ](./1-distributed_web_infrastructure)**  This file contains the link to the whiteboarding on a web infrastructure in continuation of [ 0-simple_web_stack ](./0-simple_web_stack), the following would be added:
    * 2 servers
    * 1 web server (Nginx)
    * 1 application server
    * 1 load-balancer (HAproxy)
    * 1 set of application files (your code base)
    * 1 database (MySQL)

* **[ 2-secured_and_monitored_web_infrastructure ](./2-secured_and_monitored_web_infrastructure)**  This file contains the link to the whiteboarding on a web infrastructure in continuation of [ 1-distributed_web_infrastructure ](./1-distributed_web_infrastructure), the following would be added:
    * 3 firewalls
    * 1 SSL certificate to serve www.foobar.com over HTTPS
    * 3 monitoring clients (data collector for Sumologic or other monitoring services)

* **[ 3-scale_up ](./3-scale_up)**  This file contains the link to the whiteboarding on a web infrastructure in continuation of [ 2-secured_and_monitored_web_infrastructure ](./2-secured_and_monitored_web_infrastructure), the following would be added:
    * 1 server
    * 1 load-balancer (HAproxy) configured as cluster with the other one
    * Split components (web server, application server, database) with their own server
