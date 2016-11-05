from flask import request, Flask, jsonify
import servo as servo

SECURITY_ID = "bruno05"

app = Flask("PiMoneyBox")

@app.route('/')
def index():
    return "404 Page Not Found"

@app.route('/paid', methods=["POST"])
def paid():
    if not request.json:
        abort(400)

    content = request.json

    servo = servo.Servo()
    servo.open()
    if content['security_id'] == SECURITY_ID : 
        return jsonify({'state':'open'}), 201
    else:
        abort(400)


if __name__ == '__main__':
    app.run(debug=True)