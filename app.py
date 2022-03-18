from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import load_blueprint


app = Flask(__name__)

app.register_blueprint(main_blueprint)

app.register_blueprint(load_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
