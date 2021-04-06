import sys 
import os

##Replace the standard out
sys.stdout = sys.stderr

sys.path.insert(0, '/var/www/html/W21CIS4250Team2-backend')
from Main import app as application
