# coding=utf-8
import click
from flask import Flask, request, abort, redirect, url_for, make_response, render_template, jsonify
from flask.views import View

app = Flask(__name__)
app.config.from_object('config')


@app.route('/people/')
def people():
    name = request.args.get('name')
    if not name:
        return redirect(url_for('login'))  # only get method
    print(type(request))
    user_agent = request.header.get('User-Agent')
    return 'Name:{0};UA:{1}'.format(name, user_agent)


@app.route('/')
def index():
    return "<span style='color:red'>I am app 3</span>"


@app.route('/fileList/', methods=['POST'])
def get_file_list():
    return ""


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        return 'User:{} login'.format(user_id)
    else:
        return 'Open Login Page1111'


@app.route('/secret/')
def secret():
    abort(401)
    print('This is never executed')


@app.route('/')
def default_route():
    """Default route"""
    app.logger.debug('this is a     DEBUG    message')
    app.logger.info('this is an    INFO    message')
    app.logger.warning('this is a    WARNING    message')
    app.logger.error('this is an    ERROR    message')
    app.logger.critical('this is a    CRITICAL    message')
    return jsonify('hello    world')


@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    return resp


@app.cli.command()
def init_db():
    click.echo('Init the db')


@app.errorhandler(500)  # not work
def server_error(error):
    resp = make_response(render_template('error500.html'), 500)
    return resp


class BaseView(View):
    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        if request.method != 'GET':
            return 'UNSUPPORTED!'
        context = {'users': self.get_users()}
        return self.render_template(context)

    @staticmethod
    def get_user():
        return "none"


class UserView(BaseView):
    def get_template_name(self):
        return 'users.html'

    def get_users(self):
        return [{'username': 'fake', 'avatar': 'http://lorempixel.com/100/100/nature/'}]


app.add_url_rule('/users', view_func=UserView.as_view('userview'))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=app.debug)
