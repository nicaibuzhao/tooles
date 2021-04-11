#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: untitled
# @Time : 2020/9/29 14:59

# 使用
import hashlib
import random

"""
加盐：
    其含义是对于字符串"alex123"，可以根据自定义逻辑任意分割，并在其前、中、后可加入自定义字符
"""

# 方式一：在被加密字符串前后添加随机字符，然后update

def get_salt_md5(md5_str):
    obj_md5 = hashlib.md5()
    obj_md5.update("天王".encode('utf-8'))
    obj_md5.update(md5_str.encode('utf-8'))
    obj_md5.update("盖地虎".encode('utf-8'))
    res = obj_md5.hexdigest()
    return res


print(get_salt_md5("alex123"))



# 方式二：在实例化hashlib对象的时候，直接加入随机数或字符
def get_salt_md52(md5_str):

    salt = str(random.randint(1,100))
    obj_md5 = hashlib.md5(salt.encode('utf-8'))
    obj_md5.update(md5_str.encode('utf-8'))
    res = obj_md5.hexdigest()
    return res

print(get_salt_md52("alex123"))





