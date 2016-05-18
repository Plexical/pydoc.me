import os
import site

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
site.addsitedir(os.path.join(base_path, 'lib', 'python3.5', 'site-packages'))

from pymod.routes import app as application
