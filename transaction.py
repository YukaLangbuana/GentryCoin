from flask import Flask
from flask import request
node = Flask(__name__)

#Store every transaction to a list
this_nodes_transaction = []


#Say hi to JSON ;)
@node.route('/transaction', methods=['POST'])

def transaction():
    if request.method == 'POST':
        #On each POST request, exctract the data
        new_transaction = request.get_json()

        #Add the transaction to our list
        this_nodes_transaction.append(new_transaction)

        #Print the damn thing out so we know what's what
        print "Transaction:"
        print "FROM  : ", new_transaction['from']
        print "TO    : ", new_transaction['to']
        print "AMOUNT: ", new_transaction['amount']
        print "Transaction submission successful"

        return "Transaction submission successful"

node.run()
    
