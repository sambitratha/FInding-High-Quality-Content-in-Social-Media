import networkx as nx


graph = nx.MultiDiGraph()
questions = open("QuesGraph.txt","r")

for line in questions:
    line = line.strip()
    s1, s2 = line.split()
    v1=int(s1)
    v2=int(s2)
    graph.add_node(v1)
    graph.add_node(v2)
    graph.add_weighted_edges_from([(v1,v2,1)])
    # print v1
ranks = nx.pagerank_numpy(graph)
sorted_users = sorted(ranks.items(), key = lambda x: x[1], reverse = True)
print '\nTop Questions: '
for i in range(0,3):
    print sorted_users[i][0]
questions.close()