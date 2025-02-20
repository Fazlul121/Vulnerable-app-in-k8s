from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def hello():
    cmd = request.args.get('cmd')
    if cmd:
        try:
            output = subprocess.check_output(cmd, shell=True)
            return output.decode('utf-8')
        except Exception as e:
            return str(e)
    return 'Vulnerable Flask App - Try ?cmd=id'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)