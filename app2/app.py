from flask import Flask, request
import subprocess
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    cmd = request.args.get('cmd')
    if cmd:
        try:
            output = subprocess.check_output(cmd, shell=True)
            return output.decode('utf-8')
        except Exception as e:
            return str(e)
    return 'Redis App - Try ?cmd=id'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)