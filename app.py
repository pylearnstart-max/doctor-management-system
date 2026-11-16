
from flask import Flask

from patient_api import patient_bp

app = Flask(__name__)

# Register Patient API
app.register_blueprint(patient_bp)


if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)
