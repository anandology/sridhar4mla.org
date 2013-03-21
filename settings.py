import os
import web
from web.db import dburl2dict

production_mode = os.environ.get('PRODUCTION_MODE', False)
render = web.template.render('templates/', cache=production_mode)

if 'DATABASE_URL' in os.environ:
    db_url = os.environ.get('DATABASE_URL')
else:
    db_url = "postgres://%s:''@localhost/sridhar4mla" % os.environ.get('USER')
db = web.database(db_url)


