import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):": "Make a class named %%% that is-a %%%.",
	
	"class %%%(object):\n\t def__init__(self,***)":  "class %%% has-a __init__ that takes self and *** parameters.",
	  "class %%%(object):\n\tdef ***(self, @@@)": "class %%% has-a function named *** that takes self and @@@ parameters.",

	"*** = %%%(): ": "Set *** to a instance of class %%%.",
	
	"***.***(@@@)": "From *** get the *** function, and call it with parameters self,@@@.",
		
	"***.*** = '***'": "From *** get the *** attribute and set it to '***'."
}

if len(sys.argv) == 2 and sys.argv[1] == 'english':
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())

	
def convert(snippet, phrase):
	print snippet.count("%%%"), '============='
	print snippet.count("***"), '000000000000'
	class_names = [w.capitalize() for w in 
				   random.sample(WORDS, snippet.count("%%%"))]
	print class_names, '------------------------'			   
	other_names = random.sample(WORDS, snippet.count("***"))
	print other_names, '~~~~~~~~~~~~~~~~~~~~~~~~'
	results = []
	param_names = []
	print "snippet.count:", snippet.count("@@@")
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		print "param_count: ", param_count
		param_names.append(', '.join(random.sample(WORDS, param_count)))
		print param_names
	for sentence in snippet, phrase:
		result = sentence[:]
		print "result:", result
		
	
		
		for word in class_names:
			result = result.replace("%%%", word, 1)
		for word in other_names:
			result = result.replace("***", word, 1)
		for word in param_names:
			result = result.replace("@@@", word, 1)
			
		results.append(result)
			
	return results
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)
		
		for snippet in snippets:
			phrase = PHRASES[snippet]
			print "snippet: %s\n phrase: %s" % (snippet, phrase)
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question

			print "question: %s" % question
			
			raw_input('> ')
			print "answer: %s\n\n" % answer
except EOFError:
	print "\nBye"
	