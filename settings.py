import os
import web
from web.db import dburl2dict

production_mode = os.environ.get('PRODUCTION_MODE', False)
render = web.template.render('templates/', cache=production_mode)

db = web.database(dbn='postgres', name='sridhar4mla', pw='')


