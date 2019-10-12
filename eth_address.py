import codecs

import ecdsa as ecdsa
import sha3


def gen(key):
    # test key 0x0000000000000000000000000000000000000000000000000000000000000001
    private_key = key
    private_key_bytes = codecs.decode(private_key, 'hex')
    key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
    key_bytes = key.to_string()
    # key_hex = codecs.encode(key_bytes, 'hex')
    # print(key_hex)
    public_key_bytes = key_bytes
    keccak_hash = sha3.keccak_256()
    keccak_hash.update(public_key_bytes)
    keccak_digest = keccak_hash.hexdigest()
    wallet_len = 40
    wallet = '0x' + keccak_digest[-wallet_len:]
    return wallet
