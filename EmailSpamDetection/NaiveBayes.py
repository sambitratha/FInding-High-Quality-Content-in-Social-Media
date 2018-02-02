# Implementing naive bayes with sklearn

from sklearn.naive_bayes import GaussianNB
from sklearn.feature_extraction.text import TfidfVectorizer
import string
import os
from scipy.sparse.csr import csr_matrix #need this if you want to save tfidf_matrix
import scipy.stats
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.feature_selection import SelectKBest, mutual_info_classif
import nltk
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, roc_auc_score
from sklearn import metrics

token_dict = {}
stemmer = PorterStemmer()

# Tokenizing the words 
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

# Storing data from files into array
spamtrain=[]
path1 = 'EmailsData/spam-train'
for subdir, dirs, files in os.walk(path1):
    for file in files:
        file_path = subdir + os.path.sep + file
        inputfile = open(file_path, 'r')
        text = inputfile.read()
        lowers = text.lower()
        spamtrain.append(lowers)

nonspamtrain=[]
path2 = 'EmailsData/nonspam-train'
for subdir, dirs, files in os.walk(path2):
    for file in files:
        file_path = subdir + os.path.sep + file
        inputfile = open(file_path, 'r')
        text = inputfile.read()
        lowers = text.lower()
        nonspamtrain.append(lowers)

spamtest=[]
path3 = 'EmailsData/spam-test'
for subdir, dirs, files in os.walk(path3):
    for file in files:
        file_path = subdir + os.path.sep + file
        inputfile = open(file_path, 'r')
        text = inputfile.read()
        lowers = text.lower()
        spamtest.append(lowers) 

nonspamtest=[]
path4 = 'EmailsData/nonspam-test'
for subdir, dirs, files in os.walk(path4):
    for file in files:
        file_path = subdir + os.path.sep + file
        inputfile = open(file_path, 'r')
        text = inputfile.read()
        lowers = text.lower()
        nonspamtest.append(lowers) 
       	
# using tfidf to calculate score
tfidf = TfidfVectorizer(tokenizer=tokenize,stop_words='english')
mails = spamtrain + nonspamtrain
testmails = spamtest + nonspamtest
tfs_mails = tfidf.fit_transform(mails)
tfs_test = tfidf.transform(testmails)
fs_mail = SelectKBest(mutual_info_classif, k=50)

# array of expected test labels
Y=[1]*350
Y.extend([-1]*350)
new_mail = fs_mail.fit_transform(tfs_mails,Y)
new_test = fs_mail.transform(tfs_test)

new_test = new_test.toarray()


X = new_mail.toarray()

# Test dataset
X_test = new_test
clf = GaussianNB()
clf.fit(X, Y) # Training naive bayes
predicted = clf.predict(X_test) # predicting the output of naive bayes


# Array of actual test labels
actual = [1]*130
actual.extend([-1]*130)

accuracy = accuracy_score(actual,predicted)

# Calculating accuracy, confusion matrix,roc area and f1 score
print 'Accuracy:', accuracy*100 # Accuracy = 93.0769230769 
# Spam is True Positive & Non Spam is True Negative 
# [[TN FP] [FN TP]]
print 'Confussion matrix: [[True Non Spam | False Spam] [False Non Spam | True Spam]]\n',confusion_matrix(actual,predicted) # Confusion Matrix = [[122   8],[ 10 120]]
print 'F1 score:', f1_score(actual,predicted) # F1 score = 0.93023255814
print 'ROC score:',roc_auc_score(actual,predicted) # ROC score = 0.930769230769

