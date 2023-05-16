"""

Python Flask, Python programlama dilinde web uygulamaları geliştirmek için kullanılan bir web framework'üdür.
Flask, hafif bir yapıya sahiptir.

django ve tornado, güçlü web çatılarıdır.

Flask kurulum

#python
pip install flask

#aktif ortamda
conda install flask

"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    a = data['a']
    b = data['b']
    result = a + b
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)