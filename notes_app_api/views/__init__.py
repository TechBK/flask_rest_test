from notes_app_api import app
# from .resource_test import


@app.route('/')
def hello_world():
    return 'Hello World!'

# import test