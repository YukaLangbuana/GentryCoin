from Block import *
import datetime as date

def genesis_block():
    return Block(0, date.datetime.now(), { "proof-of-work": 9, "transactions": None}, "0")

# Function to generate new block
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Gentry Coin block: " + str(this_index)
    this_hash = last_block.hash

    return Block(this_index, this_timestamp, this_data, this_hash)

#=======================FOR TESTING PURPOSES==========================================

# Create the blockchain and add the genesis block
blockchain = [genesis_block()]
previous_block = blockchain[0]

# How many blocks should we add to the chain after the genesis block
# We shall modify the structure of this code later to automate the process.
num_of_blocks_to_add = 20

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    # Tell everyone about it!
    print "Gentry Coin block", i, "has been added to the blockchain.".format(block_to_add.index)
    print "Hash: {}\n".format(block_to_add.hash)
