import hashlib


def get_sha256(str_256):
    obj_256 = hashlib.sha256()
    obj_256.update(str.encode('utf-8'))
    return obj_256.hexdigest()


print(get_sha256("alex"))
print(len(get_sha256("alex")))
