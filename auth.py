# Creating security token and validating it

from itsdangerous import URLSafeTimedSerializer, BadSignature

# Generate veryfication token
def generate_token(password, email):
    serializer = URLSafeTimedSerializer(password)
    token = serializer.dumps(email)
    
    return token

# Validating token
def confirm_token(token, expiration, password):
    serializer = URLSafeTimedSerializer(password)

    try:
        email = serializer.loads(token, expiration)
        print("Token confirmed")
        return (True, email)

    except BadSignature:
        print('Token expired')
        return (False, '')
