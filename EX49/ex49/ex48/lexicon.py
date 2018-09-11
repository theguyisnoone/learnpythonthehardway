lexicon={
'north':('direction', 'north'),
'south':('direction', 'south'),
'east':('direction', 'east'),
'go':('verb', 'go'),
'kill':('verb', 'kill'),
'eat':('verb', 'eat'),
'the':('stop', 'the'),
'in':('stop', 'in'),
'of':('stop', 'of'),
'bear':('noun', 'bear'),
'princess':('noun', 'princess'),
}
def convert_numbers(s):
	try:
		return int(s)
	except ValueError:
		return None

def scan(sentence):
	words=sentence.split()#word is a list
	result=[]
	for word in words:
		wordd=word.lower()
		print(wordd)
		if wordd in lexicon:

			result.append(lexicon[wordd])

		elif convert_numbers(word):#if number
			word=int(word)
			result.append(('number',word))

		else:
			result.append(('error',word))

	return result



#https://blog.csdn.net/oukohou/article/details/51199561
