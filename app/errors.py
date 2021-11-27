from flask import render_template
from app import app


@app.errorhandler(404)
def not_found_error(error):
    return render_template(
        'error/404.html',
        title='404 - страница не найдена',
        ), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template(
        'error/500.html',
        title='500 - ошибка сервера',
        ), 500

