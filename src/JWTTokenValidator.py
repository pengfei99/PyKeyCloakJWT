from cryptography.hazmat.primitives import serialization


class JWTTokenValidator:
    def __init__(self, pub_key_path=None):
        self.pub_key = pub_key_path

    @staticmethod
    def get_pub_key(pub_key_path):
        if pub_key_path:
            public_key = open(pub_key_path, 'r').read()
            return serialization.load_ssh_public_key(public_key.encode())
        else:
            return None

    def get_token_payload(self,token):
        pass


