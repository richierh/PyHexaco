# /usr/bin/env python

import os

# Mengunakan plugin schemacrawler untuk membuat design
cmd = "/home/cireng/schemacrawler/_schemacrawler/schemacrawler.sh \
-server sqlite \
-database /home/cireng/Projects/pyhexaco/coreapps/models/hexacodb \
-command schema \
-outputformat png \
-outputfile /home/cireng/Projects/pyhexaco/coreapps/models/hexacodb.png"

os.system(cmd)
