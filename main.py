import os, sys
sys.path.insert(0, os.path.abspath(os.path.curdir) + '/webpy/')

import web
from code import app

if __name__ == '__main__':
    app.run()
