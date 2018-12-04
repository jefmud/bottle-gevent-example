from bottle import Bottle, run, route, request
import sys

app = Bottle()

@app.route('/')
def index():
    return """
    <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
    <html>
        <head>
            <title>Hello</title>
            <style type="text/css">
              html {background-color: #eee; font-family: sans-serif;}
              body {background-color: #fff; border: 1px solid #ddd;
                    padding: 15px; margin: 15px;}
              pre {background-color: #eee; border: 1px solid #ddd; padding: 5px;}
            </style>
        </head>
        <body>
            <h1>Hello</h1>
            <p>Lorem ipsum dolor set amet...</p>
            <pre>These are not the droids you are looking for.</pre>
        </body>
    </html>
    """

@app.route('/form', method='GET')
def form_get():
    return """
     <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
    <html>
        <head>
            <title>Form</title>
            <style type="text/css">
              html {background-color: #eee; font-family: sans-serif;}
              body {background-color: #fff; border: 1px solid #ddd;
                    padding: 15px; margin: 15px;}
              pre {background-color: #eee; border: 1px solid #ddd; padding: 5px;}
            </style>
        </head>
        <body>
            <h1>Form Example</h1>
            <p>Lorem ipsum dolor set amet...</p>
            <pre>These are not the droids you are looking for.</pre>
            <form method="POST">
                Name:<br>
                <input type="text" name="name"><br><br>

                Email:<br>
                <input type="text" name="email"><br><br>

                <input type="submit">
            </form>
        </body>
    </html>
    
    """

@app.route('/form', method='POST')
def form_post():
    name = request.forms.get('name')
    email = request.forms.get('email')
    return """
    <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
    <html>
        <head>
            <title>Form POST</title>
            <style type="text/css">
              html {background-color: #eee; font-family: sans-serif;}
              body {background-color: #fff; border: 1px solid #ddd;
                    padding: 15px; margin: 15px;}
              pre {background-color: #eee; border: 1px solid #ddd; padding: 5px;}
            </style>
        </head>
        <body>
            <h1>Form POST data</h1>
            <p>Lorem ipsum dolor set amet...</p>
            <pre>received data name=%s email=%s</pre>
        </body>
    </html>
    """ % (name, email)

if __name__ == '__main__':
    PORT=54321
    HOST='0.0.0.0'
    if '--port' in sys.argv:
        idx = sys.argv.index('--port')
        PORT = int(sys.argv[idx+1])

    app.run(debug=True, host=HOST, port=PORT)