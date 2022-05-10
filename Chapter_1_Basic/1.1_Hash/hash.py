import hashlib

def get_text_hash256_value(data: str):
    hash256 = hashlib.sha256()
    hash256.update(data.encode('utf-8'))
    return hash256.hexdigest()

def get_text_hash1_value(data: str):
    hash1 = hashlib.sha1()
    hash1.update(data.encode('utf-8'))
    return hash1.hexdigest()

if __name__ == '__main__':
    hash256_result = get_text_hash256_value('test')
    hash1_result = get_text_hash1_value('test')
    print(hash256_result)
    print(hash1_result)
    
    