from flask import Flask, render_template, request

app = Flask(__name__, template_folder='assets/html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process the form data here
        name = request.form['name']
        age = request.form['age']
        return f"Name: {name}, Age: {age}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run()