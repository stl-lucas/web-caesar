from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <form method='POST'>
        <label>Rotate by:
            <input name="rot" type="text" value='0' />
		</label>
        <input type="textarea" name="text" value=''/>
		<input type="submit" value="Submit Query" />
    </form>
"""

@app.route("/")
def index():
    return form
	
@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    encrypted_text = rotate_string(text, rot)
    return '<h1>' + encrypted_text + '</h1>'

app.run()