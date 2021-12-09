class CaesarCipherArabic():
	"""Class for doing encryption and decryption using a Caesar cipher."""

	def __init__(self, shift):
		"""Construct Caesar cipher using given integer shift for rotation."""

		encoder = [None] * 36
		decoder = [None] * 36

		for k in range(36):
			encoder[k] = chr((k + shift) % 36 + ord('ا'))
			decoder[k] = chr((k - shift) % 36 + ord('ا'))
		self._forward = ''.join(encoder)
		self._backward = ''.join(decoder)


	def encrypt(self, message):
		"""Return string representing encripted message."""

		return self._transform(message, self._forward)


	def decrypt(self, secret):
		"""Return decrypted message given encrypted secret."""

		return self._transform(secret, self._backward)


	def _transform(self, original, code):
		"""Utility to perform transformation based on given code string"""
		msg = list(original)
		for k in range(len(msg)):
			if ord(msg[k]) >= 1575:
				j = ord(msg[k]) - ord('ا')
				msg[k] = code[j]
				result = ''.join(msg)
		return result


cipher = CaesarCipherArabic(3)
message = "السلام عليكم"
codeed = cipher.encrypt(message)
print(f"Secret: {codeed}")
answer = cipher.decrypt(codeed)
print(f"Message: {answer}")

