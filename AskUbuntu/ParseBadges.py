import sys
import gzip
from multiprocessing.queues import SimpleQueue
from multiprocessing import Process
from threading import Thread, Lock
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords

NUM_PROCS = 8
MAX_LEN = -1
graph = open("BadgesFeature.txt","w")
mutex = Lock()
REMOVE_STOP = False


def say(s, stream=sys.stderr):
    stream.write("{}".format(s))
    stream.flush()

def parse(post):
    soup = BeautifulSoup(post,"html.parser")

    if not soup.row:
        say("[WARNING]\n{}\n>>{}<<\n".format(post, soup))


    id = int(soup.row["id"])
    userID = int(soup.row["userid"])
    name = soup.row["name"]
    date = soup.row["date"]
    cls = soup.row["class"]
    tag = soup.row["tagbased"]
    
    return id, userID, name, date, cls,tag

def worker(queue_in, queue_out):
    while True:
        post = queue_in.get()
        if post == None: break
        id, userID, name, date, cls,tag = parse(post)
        if id is not None:
            queue_out.put((id, userID, name, date, cls,tag))
    queue_out.put(None)

def collector(queue_out):
    data = [ ]
    cnt = 0
    processed = 0
    while cnt < NUM_PROCS:
        item = queue_out.get()
        if item == None:
            cnt += 1
        else:
            data.append(item)
            processed += 1
            if processed % 1000 == 0:
                say("\r{}".format(processed))
    data = sorted(data, key=lambda x: x[0])
    N = len(data)
    for i in xrange(N):
        assert i == 0 or data[i][0] > data[i-1][0]
        say("{}\t{}\t{}\t{}\t{}\t{}\n".format(*data[i]), stream=sys.stdout)

if len(sys.argv) != 2:
    say("Usage:\n")
    say("\tpython preprocess.py posts.xml > output_file\n")
    say("\tpython preprocess.py posts.xml.gz > output_file\n")
    sys.exit(0)

queue_in = SimpleQueue()
queue_out = SimpleQueue()
procs = [ ]
for i in xrange(NUM_PROCS):
    p = Process(target=worker, args=(queue_in, queue_out))
    p.start()
    procs.append(p)

collector_proc = Process(target=collector, args=(queue_out,))
collector_proc.start()

say("\n") 
say("Reading raw xml file: {}\n".format(sys.argv[1]))
cnt = 0
fopen = lambda x: gzip.open(x) if x.endswith(".gz") else open(x)
with fopen(sys.argv[1]) as fin:
    for line in fin:
        line = line.strip()
        if line.startswith("<row Id=\""):
            queue_in.put(line)
        cnt += 1
        if cnt % 1000 == 0:
            say("\r{} lines processed".format(cnt))
say("\nDone.\n")

for i in xrange(NUM_PROCS):
    queue_in.put(None)

for p in procs:
    p.join()
collector_proc.join()
graph.close()