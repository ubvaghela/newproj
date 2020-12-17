import re
#mystr = " Your choice of which function to use depends on from whence you are loading the pickled data:pickle.loads is used to load pickled data from a bytes string. The 's' in loads refers to the fact that in Python 2, the data was loaded from a string. "
mystr = '2223-546'
#patt = re.compile(r'Y')
patt = re.compile(r"\d{4}-\d{3}")
matches = patt.finditer(mystr)
for match in matches:
	print(match)