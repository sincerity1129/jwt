import jwt
import bcrypt

name = 'test'
password = '1234'

user_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())  # 비밀번호 저장
user_token = jwt.encode({'name': name}, password, algorithm="HS256")  # str으로 반환하여 return
user_check = bcrypt.checkpw(password.encode('utf-8'), user_password)  # 비밀번호 일치 확인
