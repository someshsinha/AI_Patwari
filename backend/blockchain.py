import hashlib  
import json  

class Blockchain:  
    def __init__(self):  
        self.chain = []  
        self.current_transactions = []  
        self.new_block(previous_hash='1', proof=100)  

    def new_block(self, proof, previous_hash):  
        block = {  
            'index': len(self.chain) + 1,  
            'transactions': self.current_transactions,  
            'proof': proof,  
            'previous_hash': previous_hash  
        }  
        self.current_transactions = []  
        self.chain.append(block)  
        return block  

    def new_transaction(self, deed):  
        self.current_transactions.append(deed)  
        return self.last_block['index'] + 1  

    @property  
    def last_block(self):  
        return self.chain[-1]  