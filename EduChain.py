import json
from Block import Block
from Wallet import Wallet
from Transaction import Transaction


class EduChain():

    def __init__(self, diffculty):
        self.list = []
        self.diffculty = diffculty
        self.target_hash = self.get_target_hash()

    def block_dict(self, Block):
        return Block.__dict__

    def add_block(self, block):
        block.mine(self.diffculty, self.target_hash)
        self.list.append(block)

    def show(self):
        json_res = json.dumps(self.list, default=self.block_dict)
        print(json_res)

    def is_chain_valid(self):
        for i in range(1, len(self.list)):
            current_block = self.list[i]
            previous_block = self.list[i - 1]
            if(current_block.hash != current_block.get_hash()):
                print('Current hash is not equal')
                return False
            if(current_block.previous_hash != previous_block.hash):
                print('Previous hash is not eaqual')
                return False
            if(current_block.hash[0:self.diffculty] != self.target_hash):
                print(('The block is not mined'))
                return False

            print('All the blocks are correct')
            return True

    def get_target_hash(self):
        target = ''
        for i in range(0,self.diffculty):
            target = target + '0'
        return target

if __name__ == '__main__':
    print('EduChain CLT Oct 2019 by fxt0706')
    wallet_a = Wallet()
    wallet_b = Wallet()
    transaction = Transaction(wallet_a.public_key, wallet_b.public_key, 20)
    signature = transaction.generateSignature(wallet_a.private_key)
    transaction.verifySignature(signature)
