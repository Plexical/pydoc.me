from routes import app

if __name__ == "__main__":
    import os
    from werkzeug import SharedDataMiddleware

    static_base = os.path.join(os.getcwd(), 'static')
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {'/static': static_base})
    app.debug = True
    app.run(host='0.0.0.0')
