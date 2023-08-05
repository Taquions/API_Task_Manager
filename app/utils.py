from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") #Cria o objeto que vai ser responsável por criptografar a senha

def hash(password: str):
    return pwd_context.hash(password) #Criptografa a senha

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password) #Verifica se a senha criptografada é igual a senha criptografada no banco de dados