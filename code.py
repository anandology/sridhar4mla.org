import web

from settings import db, render, production_mode
import forms

if not production_mode:
    web.config.debug = True
    db.printing = True

urls = (
  r'/', 'index',
  r'/(.*)', 'pages',
)

app = web.application(urls, globals())

def get_delete_msg():
    msg = web.cookies().get('sp_msg', None)
    web.setcookie('sp_msg', '', expires=-1)
    return msg or ''

def set_msg(msg):
    web.setcookie('sp_msg', msg)

def save_user(i):
    phone = web.numify(i.phone)
    pin = web.numify(i.pin)
    volunteer = 'volunteer' in i
    if 'donate' in i:
        donate_amt = int(i.donate_amt or '0')
    else:
        donate_amt = 0
    donate = 'donate' in i and int(i.donate_amt, 0)
    db.insert('users', name=i.name, email=i.email, phone=phone, pin=pin, want2volunteer=volunteer, want2donate=donate_amt)

class pages(object):
    def GET(self, page):
        page = page.strip().replace('-', '_')
        if render._lookup(page)[0]:
            return render.base(render.__getattr__(page)())
        raise web.notfound()

class index(object):
    def GET(self, form=None):
        form = form or forms.stay_connected_form()
        msg = get_delete_msg()
        return render.base(render.index(form, msg=msg))
    
    def POST(self):
        i = web.input()
        form = forms.stay_connected_form()
        if not form.validates(i):
            form.fill(i)
            return self.GET(form)
        save_user(i)
        set_msg('Thank You!')
        return web.seeother('/')