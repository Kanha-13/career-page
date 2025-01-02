from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': "Data Analysts",
    'location': "Chennai, India",
    'salary': "Rs. 10,00,000"
}, {
    'id': 2,
    'title': "Data Scientists",
    'location': "Pune, India",
    'salary': "Rs. 15,00,000"
}, {
    'id': 3,
    'title': "Full Stack Developer",
    'location': "Mangalore, India",
    'salary': "Rs. 8,00,000"
}, {
    'id': 4,
    'title': "Blockchain Developer",
    'location': "Mumbai, India",
    'salary': "Rs. 10,50,000"
}, {
    'id': 5,
    'title': "Business Analysts",
    'location': "Bangaluru, India",
    'salary': ""
}]


@app.route('/', methods=['GET'])
def home():
  return render_template("index.html", jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
