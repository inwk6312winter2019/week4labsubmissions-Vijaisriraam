""" Task 1 start """

import string

fp=open('emma.txt')
name=fp.read()
for line in name.split():
	word=line.strip(string.punctuation)
	print(word.lower())
""" Task 1 end """

""" Task 2 start """

import string

fp=open('mybook.txt')
name=fp.read()

def print_book():
	count=0
	mydict=dict()
	for line in name.split():
		word=line.strip(string.punctuation)
		myword=word.lower()
		print(myword)	
		count=count+1
		if myword not in mydict:
			mydict[myword]=1
		else:
			mydict[myword]+=1

	print('The total no of words in the book is:',count)
	print(mydict)
	print('The different no of words in the book is:',len(mydict))

print_book()

""" Task 2 end """


""" Task 3 start """

import string

fp=open('mybook.txt')
name=fp.read()

def print_book():
	count=0
	mydict=dict()
	for line in name.split():
		word=line.strip(string.punctuation)
		myword=word.lower()
		print(myword)	
		count=count+1
		if myword not in mydict:
			mydict[myword]=1
		else:
			mydict[myword]+=1

	print('The total no of words in the book is:',count)
	print(mydict)
	print('The different no of words in the book is:',len(mydict))
	mylist=[]
	for key,value in mydict.items():
		mylist.append((value,key))
	mylist.sort(reverse=True)
	print(mylist)
	for freq,word in mylist[:20]:
		print(word,freq,sep='\t')


print_book()

""" Task 3 end """


""" Task 4 start """

import string

fp=open('emma.txt')
name=fp.read()
fp1=open('words.txt')
name1=fp1.read()

def print_book(book):
	mydict=dict()
	for line in book.split():
		word=line.strip(string.punctuation)
		if word not in mydict:
			mydict[word]=1
		else:
			mydict[word]+=1
	return mydict


def subtract(d1,d2):
        res=dict()
        for key in d1:
                if key not in d2:
                        res[key]=None
        return res

hist=print_book(name)
words=print_book(name1)
diff=subtract(hist,words)

print('The words in book that is not in words file are:')
for word in diff:
	print(word,sep='\n')

""" Task 4 end """

""" Task 5 start """

import sys
import string
import matplotlib.pyplot as plt

from lab4_task4 import print_book


def rank_freq(hist):
    # sort the list of frequencies in decreasing order
    freqs = list(hist.values())
    freqs.sort(reverse=True)

    # enumerate the ranks and frequencies
    rf = [(r+1, f) for r, f in enumerate(freqs)]
    return rf


def print_ranks(hist):
    for r, f in rank_freq(hist):
        print(r, f)



def plot_ranks(hist, scale='log'):
    t = rank_freq(hist)
    rs, fs = zip(*t)

    plt.clf()
    plt.xscale(scale)
    plt.yscale(scale)
    plt.title('Zipf plot')
    plt.xlabel('rank')
    plt.ylabel('frequency')
    plt.plot(rs, fs, 'r-', linewidth=3)
    plt.show()


def main(script, filename='emma.txt', flag='plot'):
    hist = print_book(filename)

    # either print the results or plot them
    if flag == 'print':
        print_ranks(hist)
    elif flag == 'plot':
        plot_ranks(hist)
    else:
        print('Usage: zipf.py filename [print|plot]')


if __name__ == '__main__':
    main(*sys.argv)


""" Task 5 end """


""" Task 6 start """

import os

def print_file(dir):
        for path in os.listdir():
                if os.path.isfile(path):
                        print(path)
print_file('.')



def print_dir(dirname):
        for name in os.listdir(dirname):
                path = os.path.join(dirname,name)
                if os.path.isfile(path):
                        print(path)
                else:
                        walk(path)
print_dir('.')

""" Task 6 end """


""" Task 7 start """

def sed(pattern,replace,filein,fileout):
        try:
                fin=open(filein,'r')
                fout=open(fileout,'w')
        except:
                print('sorry something went wrong!')

        for line in fin:
                line=line.replace(pattern,replace)
                fout.write(line)
        fin.close()
        fout.close()

pattern='pattern'
replace='replace'

filein='testfile.txt'
fileout=filein+'.replaced'

sed(pattern,replace,filein,fileout)

""" Task 7 end """


""" Task 8 start """

import os


def walk(dirname):
    names = []
    if '__pycache__' in dirname:
        return names

    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(walk(path))
    return names


def compute_checksum(filename):
    cmd = 'md5sum ' + filename
    return pipe(cmd)


def check_diff(name1, name2):
    cmd = 'diff %s %s' % (name1, name2)
    return pipe(cmd)

def pipe(cmd):
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    assert stat is None
    return res, stat


def compute_checksums(dirname, suffix):
    d = {}
    for name in dirname:
        if name.endswith(suffix):
            res, stat = compute_checksum(name)
            checksum, _ = res.split()

            if checksum in d:
                d[checksum].append(name)
            else:
                d[checksum] = [name]

    return d


def check_pairs(names):
    for name1 in names:
        for name2 in names:
            if name1 < name2:
                res, stat = check_diff(name1, name2)
                if res:
                    return False
    return True


def print_duplicates(d):
    for key, names in d.items():
        if len(names) > 1:
            print('The following files have the same checksum:')
            for name in names:
                print(name)

            if check_pairs(names):
                print('And they are identical.')


if __name__ == '__main__':
    d = compute_checksums(dirname='.', suffix='.py')
    print_duplicates(d)


""" Task 8 end """
