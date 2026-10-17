from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


#Now we'll have the functions to hash the password
def hash_password(plain_password: str) -> str:
    #hash the password using bcrypt (hashed + salt) and returns it
    return password_context.hash(plain_password) 

#Just a trial
# password = "mysecretpassword"
# print("Plain password:", password) 
# hashed_password = hash_password(password)
# print("Hashed password:", hashed_password) #$2b$12$xsv5B5O6voICl9Zmh3Q.FOp0BGGskRLSkez0YDOW2USQSjQwsKe/i

#Now that we have the hashed value we can't unhash it, but we can verify it using the verify function
def verify_password(plain_password: str, hashed_password: str) -> bool:
    #verify the password using bcrypt and returns True or False
    return password_context.verify(plain_password, hashed_password)

# print("Verifying password...", verify_password("mysecretpassword", "$2b$12$xsv5B5O6voICl9Zmh3Q.FOp0BGGskRLSkez0YDOW2USQSjQwsKe/i")) #True   