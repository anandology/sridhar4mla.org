import web

from settings import db, render, production_mode
import forms

if not production_mode:
    web.config.debug = True
    db.printing = True

urls = (
  r'/', 'index',
)

app = web.application(urls, globals())

def save_user(i):
    print i

class index(object):
    def GET(self, form=None):
        form = form or forms.stay_connected_form()
        return render.index(form)
    
    def POST(self):
        i = web.input()
        form = forms.stay_connected_form()
        if not form.validates(i):
            form.fill(i)
            return self.GET(form)
        save_user(i)
        return web.seeother('/')