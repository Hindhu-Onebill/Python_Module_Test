#Banking application using Rest API in Flask
#all the CRUD operations are being performed
#banking operation like withdrawal and deposit is also added


#importing Flask and jsonify
from flask import Flask, jsonify, render_template
app = Flask(__name__)


#storing the customers details in a dictionary
details = [{'Customer_id': "001",
           'Customer_name': "Oliver",
           'Account_No': "86661",
            'Account_Type': "Customer account",
            'Balance': "70000"},
          {'Customer_id': "002",
           'Customer_name': "Elio",
           'Account_No': "86662",
           'Account_Type': "Customer account",
           'Balance': "45000"
           },
          {'Customer_id': "003",
           'Customer_name': "Tessa",
           'Account_No': "86663",
           'Account_Type': "Customer Account",
           'Balance': "120000"
           },
          {'Customer_id': "004",
           'Customer_name': "Hardin",
           'Account_No': "86664",
           'Account_Type': "Customer account",
           'Balance': "10000"
           },
          {'Customer_id': "005",
           'Customer_name': "Lincoln",
           'Account_No': "86665",
           'Account_Type': "Customer account",
           'Balance': "40000"
           }
          ]


#this method is just like a homepage
@app.route('/')
def index():
    return "XYZ Bank Welcomes you for Online Banking"


#this method displays the details of all the customers
@app.route('/AllCustomers', methods=['GET'])
def get():
    return jsonify({'details': details})


#this method displays the details of a particular customer based on customer_id
@app.route('/AllCustomers/<int:Customer_id>', methods=['GET'])
def get_customer(Customer_id):
    return jsonify({'details': details[Customer_id]})


#It adds the given values to a already existing datas
@app.route('/Add', methods=['POST'])
def create():
    new_details = {'Customer_id': "006",
               'Customer_name': "Octavia",
               'Account_No': "86666",
               'Account_Type': "Savings account",
               'Balance': "200000"}
    details.append(new_details)
    return jsonify({'Created': new_details})


#this method is used to update a particular value in specific id
@app.route('/Update/<int:Customer_id>', methods=['PUT'])
def details_update(Customer_id):
    details[Customer_id]['Account_Type'] = "Savings"
    return jsonify({'details': details[Customer_id]})


#based on the given id it delets that particular one
@app.route('/Delete/<int:Customer_id>', methods=['DELETE'])
def delete(Customer_id):
    details.remove(details[Customer_id])
    return jsonify({'result': True})


@app.route('/Transfer')
def hello_name():
	return render_template('Transfer.html')



if __name__ == '__main__':
    app.run(debug=True)


