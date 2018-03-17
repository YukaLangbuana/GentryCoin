from blockchain import *
import json
from flask import Flask
from flask import request
node = Flask(__name__)

# Create the blockchain and add the genesis block
blockchain = [genesis_block()]
previous_block = blockchain[0]

#Store every transaction to a list
this_nodes_transactions = []

#Let us setup an arbitrary miner address
miner_address = "wqfe67vewuviwe7362rbhcg78swgvw7t23fvhsv832gbjesd77tb"

#Define the proof-of-work algorithm
def proof_of_work(last_proof):
    
    #Variable to store our incrementor
    incrementor = last_proof + 1

    #Keep incrementing until it's divisible by 13
    #   and divisible by the proof-of-work's result of the previous block

    while not(incrementor % 13 == 0 and incrementor % last_proof == 0):
        incrementor += 1

    return incrementor


@node.route('/mine', methods = ['GET'])
#Define our mining protocol
def mine():
    #Get the last proof-of-work
    last_block = blockchain[len(blockchain) - 1]
    last_proof = last_block.data['proof-of-work']

    #Find the proof-of-work for the current block
    proof = proof_of_work(last_proof)

    #Once found, reward the miner
    this_nodes_transactions.append( { "From": "Network", "To"  : miner_address, "Amount": 1 } )

    #Prepare new block's information
    new_block_data      = {"proof-of-work": proof, "transactions": list(this_nodes_transactions)}
    new_block_index     = last_block.index + 1
    new_block_timestamp = date.datetime.now()
    last_block_hash     = last_block.hash

    #Empty transaction list
    this_nodes_transactions[:] = []

    #Create the new block!
    mined_block = Block(new_block_index, new_block_timestamp, new_block_data, last_block_hash)

    #Append the newblock to the blockchain
    blockchain.append(mined_block)

    #Print to console
    print "Successfully mined a block"
    print "index     :", new_block_index
    print "timestamp :", str(new_block_timestamp)
    print "data      :", new_block_data
    print "hash      :", last_block_hash
    
    
    return "Successfully mined a block"
    

node.run()




