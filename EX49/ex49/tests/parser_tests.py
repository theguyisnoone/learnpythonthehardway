from nose.tools import *
from ex48 import lexicon,parser

def test_sentence():
	s1=parser.Sentence(('noun',"l"),('verb',"wanna"),('noun',"bed"))

def test_peek():
	word_list=[]
	assert None==parser.peek(word_list)
	assert_equal(parser.peek([('direction', 'north')]), 'direction')

def test_match():
	assert_equal(parser.match([('obj','apple')],'obj'),('obj','apple'))

def test_verb():
	assert_equal(parser.parse_verb([('verb','run')]),('verb','run'))
	# assert_equal(parser.parse_verb([('stop', 'of'), ('verb', 'go'), ('direction', 'north')]), ('verb', 'go'))

def test_object():
	assert_equal(parser.parse_object([('direction','north')]),('direction','north'))
	assert_equal(parser.parse_object([('noun','bear')]),('noun','bear'))
	assert_raises(parser.ParserError, parser.parse_object, [('verb', 'kill'), ('stop', 'of'), ('verb', 'go')])


def test_subject():
	assert_equal(parser.parse_subject([('noun','me')]),('noun','me'))
