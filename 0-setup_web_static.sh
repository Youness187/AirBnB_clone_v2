#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static.
apt-get update -y
apt-get install nginx -y
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/
echo "YE 187" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/^server {/a \ \n\tlocation \/hbnb_static {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
service nginx restart
