import copy
import sys
import json
import csv
import itertools
import networkx as nx
import pandas as pd
from matplotlib import pyplot
from pprint import pprint
from random import randint
from textstat.textstat import textstat
import nltk
from nltk import ngrams



data = json.load(open('data.json'))
# pprint(data)
# print(data)
# print(data.viewkeys())
# print data["questions"][0]


file = open('modified_data.csv', 'w')
writer = csv.writer(file)
count = 0


for x in data["questions"]:
	# print x.viewkeys()
	if(x.has_key('body')):
		question = x['body']
	else:
		question = ''
	if(x.has_key('title')):
		title = x['title']
	else:
		title = ''
	if(x.has_key('question_id')):
		question_id =  x['question_id']
	else:
		question_id = ''
	if(x.has_key('answers')):
		answers = x['answers']
	else:
		answers = ''
	if(x.has_key('question_timestamp')):
		question_timestamp = x['question_timestamp']
	else:
		question_timestamp = ''
	
	question_userid = randint(1,30)
	if(question != ""):	
		question_automated_readability_index = textstat.automated_readability_index(question)
		question_avg_letter_per_word = textstat.avg_letter_per_word(question)
		question_avg_sentence_length = textstat.avg_sentence_length(question)
		question_avg_sentence_per_word = textstat.avg_sentence_per_word(question)
		question_avg_syllables_per_word = textstat.avg_syllables_per_word(question)
		question_char_count = textstat.char_count(question)
		question_coleman_liau_index = textstat.coleman_liau_index(question)
		question_dale_chall_readability_score = textstat.dale_chall_readability_score(question)
		question_difficult_words = textstat.difficult_words(question)
		question_flesch_kincaid_grade = textstat.flesch_kincaid_grade(question)
		question_flesch_reading_ease = textstat.flesch_reading_ease(question)
		question_gunning_fog = textstat.gunning_fog(question)
		question_lexicon_count = textstat.lexicon_count(question)
		question_linsear_write_formula = textstat.linsear_write_formula(question)
		question_lix = textstat.lix(question)
		question_polysyllabcount = textstat.polysyllabcount(question)
		question_sentence_count = textstat.sentence_count(question)
		question_smog_index = textstat.smog_index(question)
		question_syllable_count = textstat.syllable_count(question)
		question_text_standard = textstat.text_standard(question)
		question_ngrams = ngrams(question.split(), 5)
	else:
		question_automated_readability_index = ''
		question_avg_letter_per_word = ''
		question_avg_sentence_length = ''
		question_avg_sentence_per_word = ''
		question_avg_syllables_per_word = ''
		question_char_count = ''
		question_coleman_liau_index = ''
		question_dale_chall_readability_score = ''
		question_difficult_words = ''
		question_flesch_kincaid_grade = ''
		question_flesch_reading_ease = ''
		question_gunning_fog = ''
		question_lexicon_count = ''
		question_linsear_write_formula = ''
		question_lix = ''
		question_polysyllabcount = ''
		question_sentence_count = ''
		question_smog_index = ''
		question_syllable_count = ''
		question_text_standard = ''
		question_ngrams = ''

	y = [str(question.encode('utf-8')), str(title.encode('utf-8')), str(question_id), str(question_timestamp), str(question_userid), str(len(answers)), 
	question_automated_readability_index, question_avg_letter_per_word, question_avg_sentence_length, question_avg_sentence_per_word, question_avg_syllables_per_word, question_char_count, question_coleman_liau_index, question_dale_chall_readability_score, question_difficult_words, question_flesch_kincaid_grade, question_flesch_reading_ease, question_gunning_fog, question_lexicon_count, question_linsear_write_formula, question_lix, question_polysyllabcount, question_sentence_count,  question_smog_index, question_syllable_count, question_text_standard]
	# print(len(y))
	# exit(1)
	# print question_userid
	# print question_id
	# print question_timestamp
	# print title
	# print question
	for answer in answers:
		count += 1
		# print answer
		# print answer.viewkeys()
		if(answer.has_key('thumbs_up')):
			thumbs_up = answer['thumbs_up']
		else:
			thumbs_up = 0
		# To write list of thumbs_up size for who gave thumbs_up
		if(answer.has_key('thumbs_down')):
			thumbs_down = answer['thumbs_down']
		else:
			thumbs_down = 0
		# To write list of thumbs_up size for who gave thumbs_down
		if(answer.has_key('answer_text')):
			answer_text = answer['answer_text']
		else:
			answer_text = ""
		if(answer.has_key('answer_sources')):
			answer_sources = answer['answer_sources']
		else:
			answer_sources = ""
		if(answer.has_key('is_best_answer')):
			is_best_answer = answer['is_best_answer']
		else:
			is_best_answer = ""
		if(answer.has_key('answer_timestamp')):
			answer_timestamp = answer['answer_timestamp']
		else:
			answer_timestamp = ""
		answer_userid = randint(1,30)
		if(answer_text != ""):
			answer_automated_readability_index = textstat.automated_readability_index(answer_text)
			answer_avg_letter_per_word = textstat.avg_letter_per_word(answer_text)
			answer_avg_sentence_length = textstat.avg_sentence_length(answer_text)
			answer_avg_sentence_per_word = textstat.avg_sentence_per_word(answer_text)
			answer_avg_syllables_per_word = textstat.avg_syllables_per_word(answer_text)
			answer_char_count = textstat.char_count(answer_text)
			answer_coleman_liau_index = textstat.coleman_liau_index(answer_text)
			answer_dale_chall_readability_score = textstat.dale_chall_readability_score(answer_text)
			answer_difficult_words = textstat.difficult_words(answer_text)
			answer_flesch_kincaid_grade = textstat.flesch_kincaid_grade(answer_text)
			answer_flesch_reading_ease = textstat.flesch_reading_ease(answer_text)
			answer_gunning_fog = textstat.gunning_fog(answer_text)
			answer_lexicon_count = textstat.lexicon_count(answer_text)
			answer_linsear_write_formula = textstat.linsear_write_formula(answer_text)
			answer_lix = textstat.lix(answer_text)
			answer_polysyllabcount = textstat.polysyllabcount(answer_text)
			answer_sentence_count = textstat.sentence_count(answer_text)
			answer_smog_index = textstat.smog_index(answer_text)
			answer_syllable_count = textstat.syllable_count(answer_text)
			answer_text_standard = textstat.text_standard(answer_text)
			answer_ngrams = ngrams(answer_text.split(), 5)
		else:
			answer_automated_readability_index = ''
			answer_avg_letter_per_word = ''
			answer_avg_sentence_length = ''
			answer_avg_sentence_per_word = ''
			answer_avg_syllables_per_word = ''
			answer_char_count = ''
			answer_coleman_liau_index = ''
			answer_dale_chall_readability_score = ''
			answer_difficult_words = ''
			answer_flesch_kincaid_grade = ''
			answer_flesch_reading_ease = ''
			answer_gunning_fog = ''
			answer_lexicon_count = ''
			answer_linsear_write_formula = ''
			answer_lix = ''
			answer_polysyllabcount = ''
			answer_sentence_count = ''
			answer_smog_index = ''
			answer_syllable_count = ''
			answer_text_standard = ''
			answer_ngrams = ''

		z = [str(answer_userid), str(answer_timestamp), str(answer_text.encode('utf-8')), str(thumbs_up), str(thumbs_down), str(is_best_answer), str(answer_sources.encode('utf-8')),
		answer_automated_readability_index, answer_avg_letter_per_word, answer_avg_sentence_length, answer_avg_sentence_per_word, answer_avg_syllables_per_word, answer_char_count, answer_coleman_liau_index, answer_dale_chall_readability_score, answer_difficult_words, answer_flesch_kincaid_grade, answer_flesch_reading_ease, answer_gunning_fog, answer_lexicon_count, answer_linsear_write_formula, answer_lix, answer_polysyllabcount, answer_sentence_count, answer_smog_index, answer_syllable_count, answer_text_standard]
		writer.writerow(y+z)
		# print (z+y)
		# print (z)
		# print answer_userid
		# print answer_timestamp
		# print answer_text
		# print thumbs_up
		# print thumbs_down
		# print is_best_answer
		# print answer_sources
print count


print("-"*100)


file.close()





