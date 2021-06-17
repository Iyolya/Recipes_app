from flask import Flask, render_template

from controllers.recipe_controller import recipes_blueprint



app = Flask(__name__)

app.register_blueprint(recipes_blueprint)

@app.route('/')
def main():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)

