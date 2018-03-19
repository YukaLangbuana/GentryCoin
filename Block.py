import hashlib as hasher

class Block:

    #This is our initiator function
    #   We can add any data we want to the block
    def __init__(self, index, timestamp, data, previous_hash):
        self.index          = index
        self.timestamp      = timestamp
        self.data           = data
        self.previous_hash  = previous_hash           #This is where our immutability came from
        
        self.hash           = self.hash_block()       #To ensure the integrity of our blockchain,
                                                      #each block shall have a self-identifying hash.
                                                      #Think of it as some sort of ID number.

    #This function create our block's "ID Number"
    #   made out of the block's index, timestamp, data, and previous block's hash
    def hash_block(self):
        sha = hasher.sha256()               
        sha.update(str(self.index)     +
                   str(self.timestamp) +
                   str(self.data)      +
                   str(self.previous_hash))
        return sha.hexdigest()


#This is our block class
    
