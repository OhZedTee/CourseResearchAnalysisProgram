# Project

For all Documentation regarding this project, please see the [Wiki](<doc/Full Documentation.md>)

How to recreate our results:

Necessary Dependencies for Webscraping functionality
requires:
- sudo pip3 install requests
- sudo pip3 install beautifulsoup4

Example Graph:
- Search by Department - CIS
- Combine Search
- Search by Department - Marketing
- Export with filename ex "CIS_Marketing"


Gephi Dependencies 
- Java 8 

Typical Gephi Settings Used:

**Layout**
- Layout: Force Atlas 2
- Layout Settings: No Overlap


**Appearance**
- Nodes - Partition 
- Attribute - Department / Status
- Font: Arial 5 Plain


**Preview Settings**
- Show Labels: ON
- Shorten Label: ON




# CI/CD Pipeline Configuration
\
Locally:
## 1. Generate SSH Certificates
========================= \
ssh-keygen -t rsa -b 4096 \

rename file to cis4250, leave password blank and click enter

### Rename Private Key
mv cis4250 cis4250.pem

### Change permissions on private key
chmod 700 cis4250.pem

## 2. Copy Public key to server
========================= \
scp cis4250.pub sysadmin@cis4250-02.socs.uoguelph.ca:/home/sysadmin/.ssh/uploaded_key.pub
\
\
\
\
On the server:
## 3. Append authorized_keys file
========================= \
cat ~/.ssh/uploaded_key.pub >> ~/.ssh/authorized_keys

## 4. Update server file permissions (if necessary, check /var/log/auth.log for permission errors)
========================= \
sudo chmod 700 ~ \
sudo chmod 700 ~/.ssh \
sudo chmod 600 ~/.ssh/*


## 5. Test auth locally
========================= \
ssh -i cis4250.pem sysadmin@cis4250-02.socs.uoguelph.ca

It should not prompt you for a password, if it does, check ssh logs located at /var/log/auth.log


## 6. Copy SSH Private Key to Gitlab settings
========================= \
define the variable SSH_PRIVATE_KEY within Settings > CI/CD > Variables with the content of your private key (cis4250.pem)


## 7. Create Deploy Token
========================= \
Create Deploy token within Settings > Repository > Deploy tokens, make note of the username and password (you won't be able to see the password again)


## 8. Copy Deploy Token Values to Gitlab settings
========================= \
define the variable CI_DEPLOY_USER within Settings > CI/CD > Variables with the content of your Deploy Token username \
define the variable CI_DEPLOY_PASSWORD within Settings > CI/CD > Variables with the content of your Deploy Token password

## 9. Remove Password Restriction For Sudo Command from SSH User
========================= \
sudo visudo

Add the following line to the **end** of the file:
```
sysadmin ALL=(ALL) NOPASSWD: ALL
```