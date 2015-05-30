import os
import sys
class easyfile:
	def __init__(self,filename):
		self.filename = filename
		self.idxname= filename+".idx"
		self.idx = None
		self.length = None
		self.fh = None
	def makeIndex(self):
		self.fh = open(self.filename,'r')
		fh = self.fh
		out_h = open(self.idxname,'w')
		out_h.write("0\n");
		while(fh.readline()):
			out_h.write(str(fh.tell()))
			out_h.write("\n")
	def loadIndex(self):
		try:
		  fh = open(self.idxname,'r')
		except:
		  sys.stderr.write("ERROR: loadIndex() must be executed after makeIndex \n")
		  sys.exit(1)
		self.idx = []
		for line in fh:
		   self.idx.append( int(line.strip()) )
		self.length = len(self.idx)
		fh.close()
	def getline(self,i):
		if self.idx is None or self.length is None:
			self.makeIndex()
			self.loadIndex()
		if i > len(self.idx):
			sys.stderr.write("ERROR: %d line doesn't exist \n" % (i) )
		fh = self.fh
		fh.seek(self.idx[i-1],0)
		return fh.readline()
	def seekline(self,i):
		if self.idx is None or self.length is None or self.fh is None:
			self.makeIndex()
			self.loadIndex()
		if i > len(self.idx):
			sys.stderr.write("ERROR: %d line doesn't exist \n" % (i) )
		fh = self.fh
		fh.seek(self.idx[i-1],0)
		return fh
if __name__ == "__main__":
	fh = easyfile("test.txt")
	sys.stdout.write(fh.getline(3))
	sys.stdout.write(fh.getline(11))
	fp = fh.seekline(8)
	sys.stdout.write(fp.readline())