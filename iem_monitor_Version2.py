from flask import Flask, render_template_string, request

app = Flask(__name__)

MESSAGES = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form.get("message")
        if message:
            MESSAGES.append(message)
    return render_template_string("""
    <h1>VTEC/IEMBot Monitor</h1>
    <form method="post">
        <input type="text" name="message" placeholder="Paste alert/test here" size="60">
        <input type="submit" value="Submit">
    </form>
    <h2>Received Messages:</h2>
    <ul>
    {% for msg in messages %}
        <li>{{ msg }}</li>
    {% endfor %}
    </ul>
    """, messages=MESSAGES)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)