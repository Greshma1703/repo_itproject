from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="docs/Architecture/templates",
    static_folder="docs/Architecture/static",
    static_url_path="/static",
)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
