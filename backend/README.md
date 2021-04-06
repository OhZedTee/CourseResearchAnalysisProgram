# Running the Backend

1. On terminal in root directory run `pip install -r requirements.txt
2. On terminal cd to the backend folder
3. run `scripts/run_app.sh`
4. See the ![Wiki - API Documenation](https://git.socs.uoguelph.ca/team2-design5/project/-/wikis/API-Documenation) for requests that can be made against the backend server



# Installing and Configuring the Backend on a Production Server

## 0. Install Python, Pip, and Git
========================= \
sudo apt-get update \
sudo apt-get -y upgrade   

### Python should be installed natively, verify this
python3 --version

### Install Pip
sudo apt-get install -y python3-pip

### Install Git
sudo apt-get install -y git


## 1. Install apache and mode_wsgi
========================= \
sudo apt-get install apache2 \
sudo apt-get install libapache2-mod-wsgi-py3 \
sudo a2enmod headers
sudo systemctl restart apache2

## 2. Clone the project
================== \
cd ~/ \
git clone https://${CI_DEPLOY_USER}:${CI_DEPLOY_PASSWORD}@git.socs.uoguelph.ca/team2-design5/project.git W21CIS4250Team2 \
cd W21CIS4250Team2

For information about the CI_DEPLOY_USER and CI_DEPLOY_PASSWORD please see the root README
regarding CI CD setup (the server requires that the remote be the same user that will pull
on the server in the automated process)

## 2a. Change directory permissions
========================= \
sudo chown -R sysadmin:www-data * \
sudo chmod -R 775 backend/data
sudo chmod -R 775 /home
sudo chmod -R 775 /home/sysadmin


## 3. Install Dependencies
================== \
sudo pip3 install -r requirements.txt

## 4. Create Symlink
========================= \
cd ~/ \
sudo ln -sT ~/W21CIS4250Team2/backend/ /var/www/html/W21CIS4250Team2-backend
sudo chown -R sysadmin:www-data /var/www/html/W21CIS4250Team2-backend

## 4. Apache Settings
================= \
sudo vim /etc/apache2/sites-enabled/000-default.conf

```
<VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        #ServerName www.example.com

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html

        WSGIDaemonProcess W21CIS4250Team2-backend threads=5 home=/home/sysadmin/W21CIS4250Team2/backend/ user=sysadmin
        WSGIScriptAlias / /var/www/html/W21CIS4250Team2-backend/flask.wsgi process-group=W21CIS4250Team2-backend application-group=%{GLOBAL}
        <Directory W21CIS4250Team2-backend>
             Order deny,allow
             Allow from all
        </Directory>

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
         Header set Access-Control-Allow-Origin "*"
</VirtualHost>

```

## 4a.
========================= \
vim /etc/apache2/apache2.conf \

```
IncludeOptional sites-enabled/*.conf
```

## 5. Restart apache
=============== \
sudo service apache2 restart \

## Debugging?
=============== \
sudo tail -f /var/log/apache2/error.log \
sudo tail -f /var/log/apache2/access.log


# Setup Scrape CronJob

## 1. Install cURL
========================= \
sudo apt-get update \
sudo apt-get -y upgrade \
sudo apt -y install curl

## 2. Make script executable
========================= \
cd ~/W21CIS4250Team2/backend \
chmod +x scripts/*.sh

## 3. Add Crontab entry
========================= \
crontab -e

```
0 4 * * * ~/W21CIS4250/backend/scripts/run_scrape.sh >> ~/log/scrape.log 2>&1
```
mkdir ~/log/ \
touch ~/log/scrape.log

