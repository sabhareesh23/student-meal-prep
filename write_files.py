open('app/__init__.py','w').write("""from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    from app.routes import main
    app.register_blueprint(main)

    return app
""")

open('app/routes.py','w').write("""from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index() -> str:
    return render_template('index.html')
""")

open('run.py','w').write("""from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
""")

open('templates/index.html','w').write('<html><body><h1>Student Meal Prep App</h1></body></html>')

print('All files written successfully')
