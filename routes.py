from flask import render_template, request, redirect

def init_routes(app):
    @app.route('/')
    def get_base():
        return render_template('base.html')
