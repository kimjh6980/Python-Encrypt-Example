import hashlib

storepw = hashlib.md5()
storepw.update('abcde123'.encode())

inputpw = input('Input Passwor : ')

Encryptpw = hashlib.md5()
Encryptpw.update(inputpw.encode())

if storepw.hexdigest() == Encryptpw.hexdigest():
    print('Password Matching Success')
    print(storepw.hexdigest())
else:
    print('Password Matching Fail')
    print(' storepw = ', storepw.hexdigest())
    print(' inputpw = ', Encryptpw.hexdigest())

''' hexdigest()는 우리가 일반적으로 알고 있는 hashed된 16진수값'''
''' hashed 된 값을 그냥 digest로 출력하면 그건 Decrypt된게 아니기 때문에 글자가 다 깨짐'''
''' MD5 값을 Decrypt하고 싶으면 http://www.md5online.org/ 에서 확인할것'''
''' MD5 뿐만 아니라 SHA1도 같은 방식 (hashlib.sha1)로 하면됨'''