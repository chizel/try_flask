#!flask/bin/python

from my_site import app

if __name__ == '__main__':
    if app.debug:
        app.run(debug=True)
    else:
        app.run(host='0.0.0.0')
