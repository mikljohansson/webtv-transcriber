#!/usr/bin/env python
import sys, io, re, codecs, json

def ngrams(stream, gramsize):
	utfstream = codecs.getreader('utf-8')(stream)
	remainder = ''
	replacer = re.compile(u'([^\w]|[\d_])+', re.UNICODE)

	while True:
		buf = utfstream.read(65536)
		if buf == '':
			break
		
		buf = remainder + buf.lower()
		buf = replacer.sub(' ', buf)

		last = len(buf) - len(buf) % gramsize
		
		for i in xrange(0, last, gramsize):
			yield buf[i:(i + gramsize)]
		
		remainder = buf[last:]

def counts(stream, gramsize):
	counters = {}
	for gram in ngrams(stream, gramsize):
		counters[gram] = counters.get(gram, 0) + 1
	return counters

def mostfrequent(counters):
	return dict(item for item in counters.iteritems() if item[1] >= 5)

if __name__ == '__main__':
	counters = mostfrequent(counts(sys.stdin, int(sys.argv[1])))
	json.dump(counters, sys.stdout, indent=2)
