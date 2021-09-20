from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import matplotlib.pyplot as plt 
import csv



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local.db'
db = SQLAlchemy(app)


''' reflecting the table in the given db
it is like read only mode so I can not add any new items to the 
database tables but I do not need to anyways'''
transactions = db.Table('transactions', db.metadata, autoload=True, autoload_with=db.engine)
results = db.session.query(transactions).all()
# for result in results:
# 	print(result.price)


# home route
@app.route('/', methods=['GET'])
def index():

	return render_template('base.html')


'''generate values for the chart 
then pass them to the template to create the chart'''
@app.route('/report_view', methods=['GET'])
def chart_generator():
	''' generate the chart here then return it to
	the view where we're gonna plot it'''
	x = []
	y = []

	with open('static/report_data.txt', 'r') as csvfile:
		report = csv.reader(csvfile, delimiter = ',')

		for row in report:
			x.append(row[0])
			y.append(row[1])

	x_and_y_in_pairs = []
	for x_item, y_item in zip(x, y):
		x_and_y_in_pairs.append({x_item, y_item})

	return render_template('report_view.html', xdata = x, ydata = y, total_data = x_and_y_in_pairs)


@app.route('/return_highest', methods=['GET'])
def return_highest():
	drivers_names = []
	total_cash_amount_for_deriver = []
	for result in results:
		drivers_names.append(result.driverName)
		total_cash_amount_for_deriver.append(result.collectionAmount)

	return render_template('report_view.html', drivers_names = drivers_names, total_cash = total_cash_amount_for_deriver)

if __name__ == '__main__':
	app.run(debug=True)