import networkx as nx 
import numpy as np 
import csv
import sys

allusers = {}

GraphA = None

class Question:
	def __init__(self, contents, title, id, timestamp, userid):
		self.contents = contents
		self.title = title
		self.id = id
		self.timestamp = timestamp
		self.userid = userid
		self.answers = []

	def add_answers(self, answer_data):
		self.answers.append(answer_data)
		 

class Answer:
	def __init__(self, contents, userid, timestamp, thumbsup, thumbsdown, is_best_answer, source, questionid):

		self.contents = contents
		self.userid = userid
		self.timestamp = timestamp
		self.thumbsup = int(thumbsup)
		self.thumbsdown = int(thumbsdown)
		self.is_best_answer = int(is_best_answer)
		self.source = source
		self.questionid = questionid


class User:
	def __init__(self, id, quesions_asked, answers_given):
		self.quesions_asked = quesions_asked
		self.answers_given = answers_given
		self.id = id


	def hasAnswered(self, userid):
		targetuser = allusers[userid]
		for question in targetuser.quesions_asked:
			for answer in question.answers:
				if answer.userid == self.id:
					return True

		return False

	def hasAnsweredBest(self, userid):
		targetuser = allusers[userid]
		for question in targetuser.quesions_asked:
			for answer in question.answers:
				if answer.userid == self.id and answer.is_best_answer:
					return True

		return False



def process_data(data):
	for line in data:
		[question, title, id, timestamp, userid] = line[:5]
		newq = Question(question, title, id, timestamp, userid)
		if userid not in allusers:
			newuser = User(userid, [newq], [])
			allusers[userid] = newuser
		else:
			allusers[userid].quesions_asked.append(newq)

		no_of_answers = line[5]
		cur = 6
		for i in range(no_of_answers):
			[userid, timestamp, ans, thumbsup, thumbsdown, is_best_answer, source] = line[cur:cur + 7]
			cur += 7

			newA = Answer(ans, userid, timestamp, thumbsup, thumbsdown, is_best_answer, source, id)
			if userid not in allusers:
				newuser = User(userid, [], [newA])
				allusers[userid] = newuser
			else:
				allusers[userid].answers_given.append(newA)


			

			newq.add_answers(newA)


def createNormalGraph():
	global GraphA
	GraphA = nx.Graph()
	print "graph created"
	print GraphA
	for u in allusers:
		GraphA.add_node(allusers[u])

	for u in allusers:
		for v in allusers:
			if u != v:
				if allusers[u].hasAnswered(v):
					GraphA.add_edge(u, v, weight = 1)



toydata = []


process_data(toydata)
createNormalGraph()

print list(GraphA.edges)





