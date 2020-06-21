import time
import hashlib

class Block():

    def __init__(self, msg, previous_hash):
        self.previous_hash = previous_hash
        self.msg = msg
        self.time_stamp = time.asctime(time.localtime(time.time()))
        self.nonce = 1
        self.hash = self.get_hash()

    def get_hash(self):
        data = self.time_stamp + self.msg + str(self.nonce) + self.previous_hash
        hash256 = hashlib.sha256()
        hash256.update(data.encode('gb2312'))
        return hash256.hexdigest()
        
    def mine(self, diffculty, target):
        while (int(self.hash[0:diffculty] != target)):
            self.nonce = self.nonce + 1
            self.hash = self.get_hash()
        print('Mined a new block')