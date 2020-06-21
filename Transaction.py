from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Signature import DSS

class Transaction():

    def __init__(self, key_from, key_to, domain):
        self.sender = key_from
        self.reciepient = key_to
        self.domain = str(domain)

    def generateSignature(self, private_key):
        data = self.sender + self.reciepient + self.domain
        hash_msg = SHA256.new(data.encode('utf8'))
        pr_key_for_signer = ECC.import_key(private_key)
        signer = DSS.new(pr_key_for_signer, 'fips-186-3')
        signature = signer.sign(hash_msg)
        return signature
    
    def verifySignature(self, signature):
        data = self.sender + self.reciepient + self.domain
        hash_msg = SHA256.new(data.encode('utf8'))
        pub_key_for_vetifier = ECC.import_key(self.sender)
        verifier = DSS.new(pub_key_for_vetifier, 'fips-186-3')
        try:
            verifier.verify(hash_msg, signature)
        except ValueError:
            print('Signature verified error')
        else:
            print('Signature verified succeed')