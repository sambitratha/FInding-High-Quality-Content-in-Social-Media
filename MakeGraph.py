
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





CHUNK_SIZE = 100	 

COLOR_TOP_N = 10
separator = '\t' # '\t' for tsc and ','' for csv
users = set()
data = [None] * CHUNK_SIZE
graph = nx.MultiDiGraph()
count = 0

with open('modified_data.csv', 'r') as file:
	reader = csv.reader(file)
	for line in reader:
		if(line[31] == 'True'):
			# add users to set
			users.add(line[3])
			users.add(line[27])
			# pprint(line)
			# print(line[3])
			# print(line[27])
			weight = 1
			data[count] = (line[3], line[27], weight)
			count += 1
			if count == CHUNK_SIZE:
				graph.add_weighted_edges_from(data)
				count = 0
	graph.add_weighted_edges_from(data[:count])

	ranks = nx.pagerank_numpy(graph)
	sorted_users = sorted(ranks.items(), key = lambda x: x[1], reverse = True)
	print '\nTop Users: '
	for i in range(0,COLOR_TOP_N):
	    print sorted_users[i][0]
	  


