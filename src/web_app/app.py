from flask import request, Flask, jsonify

app = Flask("PiMoneyBox")

@app.route('/')
def index():
    return "404 Page Not Found"

@app.route('/paid', methods=["POST"])
def paid():
    if not request.json:
        abort(400)
    return jsonify({'state':'open'}), 201

if __name__ == '__main__':
    app.run(debug=True)