from Crypto.PublicKey import ECC

class Wallet():

    def __init__(self):
        self.generateKeyPair()
    
    def generateKeyPair(self):
        try:
            key = ECC.generate(curve='P-256')
            pr_key_pem = key.export_key(format= 'PEM')
            pb_key_pem = key.public_key().export_key(format= 'PEM')
            self.private_key = pr_key_pem
            self.public_key = pb_key_pem
        except Exception as e:
            print(e)
        else:
            print('Wallet generate KeyPair Succeed\nPublic Key: ' + self.public_key \
            + '\nPrivate Key: ' + self.private_key + '\n')