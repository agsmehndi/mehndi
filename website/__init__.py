from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hashtaganugotsmeeten'

    from .views import views
    from .polaroid import polaroid
    from .ghibli import ghibli
    from .vfb import vfb
    from .film import film

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(polaroid, url_prefix='/')
    app.register_blueprint(ghibli, url_prefix='/')
    app.register_blueprint(vfb, url_prefix='/')
    app.register_blueprint(film, url_prefix='/')

    return app