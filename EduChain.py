import time
import hashlib
import json

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

    def mine(self, diffculty):
        target = ''
        for each_num in range(0,diffculty):
            target = target + '0'
        while (int(self.hash[0:diffculty] != target)):
            self.nonce = self.nonce + 1
            self.hash = self.get_hash()
        print('Mined a new block')


class EduChain():

    def __init__(self, diffculty):
        self.list = []
        self.diffculty = diffculty

    def block_dict(self, Block):
        return Block.__dict__

    def add_block(self, block):
        block.mine(self.diffculty)
        self.list.append(block)

    def show(self):
        json_res = json.dumps(self.list, default=self.block_dict)
        print(json_res)

    def isChainValid(self):
        for i in range(1, len(self.list)):
            current_block = self.list[i]
            previous_block = self.list[i - 1]
            if (current_block.hash != current_block.get_hash()):
                print('Current hash is not equal')
                return False
            if (current_block.previous_hash != previous_block.hash):
                print('Previous hash is not eaqual')
                return False
            print('All the blocks are correct')
            return True




print('EduChain CLT Apr 2018 by fxt0706')
c = EduChain(1)
c.add_block(Block('first','0'))
c.add_block(Block('second', c.list[len(c.list)-1].hash))
c.show()
c.isChainValid()
