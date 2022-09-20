* [0-transfer_file](0-transfer_file) - bash script that transfers a file from our client to the server
* [1-install_nginx_web_server](1-install_nginx_web_server) - bash script that configures a new Ubuntu machine to respect the conditions given
* [2-setup_a_domain_name](2-setup_a_domain_name) - my domain name from .TECH Domains
* [3-redirection](3-redirection) - bash script containing command to automatically configure a Ubuntu machine to respect given requirements
* [4-not_found_page_404](4-not_found_page_404) - updated [3-redirection](3-redirection) to the requirements for 404
* [7-puppet_install_ngix_web_server.pp](7-puppet_install_ngix_web_server.pp) - install and configure ngix using puppet insteadd of bash, also include resources in the manifest to perfom a 301 redirect when querying/redirect_me