from flask import Flask, render_template
from flask_migrate import Migrate
from models.alarm import db
from routes.alarms_blueprint import alarms_blueprint


app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)
migrate.init_app(app, db)

app.register_blueprint(alarms_blueprint, url_prefix='/alarms')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
