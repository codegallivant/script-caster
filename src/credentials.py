import os
from cryptography.fernet import Fernet


class Credential:

	def __init__(self, credsfilepath, filecontent=None):
		self.credsfilepath = credsfilepath
		self.keyfilepath = os.path.join(os.path.dirname(credsfilepath), "keys", os.path.splitext(os.path.basename(credsfilepath))[0] + "_KEY" + ".key")
		if filecontent != None and ((not os.path.exists(credsfilepath)) or (os.path.getsize(credsfilepath) == 0)):
			key = Fernet.generate_key()
			f = Fernet(key)
			encrypted_content = f.encrypt(filecontent.encode())
			with open(self.credsfilepath, 'wb') as credsfile:
				credsfile.write(encrypted_content)
			with open(self.keyfilepath, 'wb') as keyfile:
				keyfile.write(key)


	def get_key(self):
		if os.path.exists(self.keyfilepath) and os.path.getsize(self.keyfilepath)>0:
			with open(self.keyfilepath, 'r') as keyfile:
				key = keyfile.read()
		else:
			key = False
		return key

	def reset_key(self):
		key = Fernet.generate_key()
		f = Fernet(key)
		with open(self.keyfilepath, 'wb') as keyfile:
			keyfile.seek(0)
			keyfile.write(key)
			keyfile.truncate()

	def encrypt(self, text=None):
		key = self.get_key()
		if key is False:
			self.reset_key()
			key = self.get_key()
			self.encrypt()
		else:
			f = Fernet(key)
			if text == None:
				with open(self.credsfilepath, 'r')  as credsfile:
					encrypted_content = f.encrypt(credsfile.read().encode())
			else:
				encrypted_content = f.encrypt(text.encode())
			
			with open(self.credsfilepath, 'wb') as credsfile:
				credsfile.seek(0)
				credsfile.write(encrypted_content)
				credsfile.truncate()



	def get_decrypted_content(self):
		key = self.get_key()
		with open(self.credsfilepath, 'r') as credsfile:
			credsfilecontent = credsfile.read()
		if key is False:
			decrypted_content = credsfilecontent
		else:
			f = Fernet(key)
			decrypted_content = f.decrypt(credsfilecontent).decode()
		return decrypted_content

	def decrypt(self):
		key = self.get_key()
		if key is not False:
			decrypted_content = self.get_decrypted_content()
			with open(self.credsfilepath, 'w') as credsfile:
				credsfile.seek(0)
				credsfile.write(decrypted_content)
				credsfile.truncate()
			os.remove(self.keyfilepath)

	def reset_and_encrypt(self, text=None):
		if text == None:
			decrypted_content = self.get_decrypted_content()
		else:
			decrypted_content = text
		self.reset_key()
		key = self.get_key()
		f = Fernet(key)
		encrypted_content = f.encrypt(decrypted_content.encode())
		with open(self.credsfilepath, 'wb') as credsfile:
			credsfile.seek(0)
			credsfile.write(encrypted_content)
			credsfile.truncate()