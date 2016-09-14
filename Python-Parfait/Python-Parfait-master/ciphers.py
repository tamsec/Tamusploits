#Viginere, substitution, and Caesar ciphers.
#All below take case into consideration; a simpler code would just convert 
#everything to lowercase.

import sys
global alflist 
alflist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alf = 'abcdefghijklmnopqrstuvwxyz.\"_/\\'	 #manually escaped character set
subKey = 'qazw\"sxedcrf\\vtgbyhn.ujm/i_kolp' #manually escaped key
key = "mithrandil" 

#substitution------------------------------------------------------------------
def checkKey(key):
	if len(key) != len(alf):
		sys.exit('Key is wrong length.')

def Sub(text, key, mode): #'e' or 'd' for encrypt or decrypt
	checkKey(key)
	mydict = dict(zip(alf, key))
	flipped = {v: k for k, v in mydict.items()} #or: flipped = dict(zip(key, alf))
	new = ''
	if mode == 'e':
		for l in text:
			if l.lower() in alf:
				if l.islower():
					new += new.join(mydict[l])
				elif l.isupper(): 
					new += new.join(mydict[l.lower()].upper())
				else:	#it's a character, but it's in alf
					new += new.join(mydict[l])
			else: #it's a chr and it's not in alf (i.e. spaces)
				new += new.join(l)
	elif mode == 'd':
		for l in text:
			if l.lower() in alf:
				if l.islower():
					new += new.join(flipped[l])
				elif l.isupper():
					new += new.join(flipped[l.lower()].upper())
				else:
					new += new.join(flipped[l])
			else: 
				new += new.join(l)
	else:
		print("sry u fail")
	return new

#caesar-----------------------------------------------------------------------------
def toCaesar(plaintext, value):
	caesared = ''
	for x in plaintext:
		if x.isalpha():
			num = ord(x) + value
			if x.islower():
				if num > ord('z'):  
					num -=26
			elif x.isupper():
				if num > ord('Z'):
					num -= 26
			caesared += chr(num)
		else:
			caesared += x
	return caesared

#viginere-----------------------------------------------------------------------
#repeat key until same length as plaintext 
def extendKey(key, plain):
	while len(key) < len(plain):
		x = len(plain) - len(key)
		if len(key + key) <= len(plain):
			key += key
		elif len(key+key) > len(plain):
			key += key[:x]
		else:
			break
	if len(key) > len(plain):
		x = len(plain)
		key = key[:x]
	return key

#*****There's probably a much nicer way to do this with ord().****
#i is index in plaintext, keyIndex is index in key
def eVig(plaintext, key):
	encrypted = ''
	keyIndex = 0
	for i in range(0, len(plaintext)):
		if plaintext[i].isalpha():
			if plaintext[i].isupper():
				encrypted += alflist[(alflist.index(plaintext[i].lower()) + alflist.index(key[keyIndex]))%26].upper()
			else:
				encrypted += alflist[(alflist.index(plaintext[i]) + alflist.index(key[keyIndex]))%26]
			if keyIndex + 1 < len(key):
				keyIndex += 1
			else: 
				keyIndex = 0
		else:
			encrypted += plaintext[i]
	return encrypted

def eVig(plaintext, key): #i is index in plaintext, keyIndex is index in key
	encrypted = ''
	keyIndex = 0
	for i in range(0, len(plaintext)):
		if plaintext[i].isalpha():
			if plaintext[i].isupper():
				encrypted += chr(ord(plaintext[i].lower()) + ord(key[keyIndex])%26).upper()
			else:
				encrypted += chr(ord(plaintext[i]) + ord(key[keyIndex])%26)
			if keyIndex + 1 < len(key):
				keyIndex += 1
			else: 
				keyIndex = 0
		else:
			encrypted += plaintext[i]
	return encrypted

def dVig(ciphered, key): 
	plain = ""
	keyIndex = 0
	for i in range(0, len(ciphered)):
		if ciphered[i].isalpha():
			if ciphered[i].isupper():
				plain += alflist[(alflist.index(ciphered[i].lower()) - alflist.index(key[keyIndex]))%26].upper()
			else:
				plain += alflist[(alflist.index(ciphered[i]) - alflist.index(key[keyIndex]))%26]
			if keyIndex + 1 < len(key):
				keyIndex += 1
			else: 
				keyIndex = 0
		else:
			plain += ciphered[i]
	return plain

