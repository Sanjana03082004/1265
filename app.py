from flask import Flask,render_template,redirect,request,url_for

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])

def home():
	if request.method=="POST":
		print("Form submitted")
		print("Form data:",request.form)
		return "registration Succesful!"
	return render_template('register.html')
if ('__main__')==(__name__):
	app.run(debug=True)