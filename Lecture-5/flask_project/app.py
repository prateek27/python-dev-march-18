from flask import Flask, render_template, request

app = Flask("my flask app!")

@app.route('/home')
def home():
	return render_template("index.html")

@app.route('/blog/<id>/')
def blog(id):
	return "Showing blog no. " + id

@app.route('/bio')
def mybio():
	name = request.args.get('name')
	age = request.args.get('age')
	names = ['a', 'b', 'c']
	return render_template("bio.html", 
		name=name, age=age, names=names)

@app.route('/upload', methods=['GET', 'POST'])
def upload_data():
	if request.method == 'GET':
		return render_template('upload.html')
	else:
		print(request.form)
		image = request.files.get('image')
		image.save('pic.jpg')
		return render_template('index.html')

if __name__ == "__main__":
	app.run(use_reloader=True)