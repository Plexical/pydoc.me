import os
import sys
from pymod.routes import app

if __name__ == "__main__" and '--serve' in sys.argv:
    from werkzeug import SharedDataMiddleware

    static_base = os.path.join(os.getcwd(), 'static')
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {'/static': static_base})
    app.debug = True
    app.run(host='0.0.0.0')
elif __name__ == '__main__':
    import os
    import sys
    import pprint
    from pymod.index import modules

    mods = modules()
    if '--pprint' in sys.argv:
        pprint.pprint(mods)
