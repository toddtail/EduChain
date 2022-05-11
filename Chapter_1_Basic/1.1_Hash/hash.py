import hashlib

def get_text_hash256_value(data: str):
    hash256 = hashlib.sha256()
    hash256.update(data.encode('utf-8'))
    return hash256.hexdigest()

def get_text_hash1_value(data: str):
    hash1 = hashlib.sha1()
    hash1.update(data.encode('utf-8'))
    return hash1.hexdigest()

def get_file_hash256_value(data: str):
    hash256 = hashlib.sha256()
    with open(data, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            hash256.update(chunk)
    return hash256.hexdigest()

if __name__ == '__main__':
    hash256_text_result = get_text_hash256_value('test')
    hash1_result = get_text_hash1_value('test')
    hash256_file_result = get_file_hash256_value('test.docx')
    print(hash256_text_result)
    print(hash1_result)
    print(hash256_file_result)
    