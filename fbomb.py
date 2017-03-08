import fire
import os
class FBomb(object):
	
	def forkbomb(self):
		while(0xFABB):
			os.fork()
	
	def fstar(self, n=1):
		for i in range(0, n):
			print "f**k"
	
	def dfstar(self, n=1, d="me"):
		for i in range(0, n):
			print "f**k " + d

	def f(self):
		print "f**k"

	def df(self, d="me"):
		print "f**k " + d


def main():
	fire.Fire(FBomb)

if __name__ == '__main__':
	main()
