import pandas as pd
import numpy as np
from sklearn import metrics, model_selection
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
from sklearn import tree

df = pd.read_csv('VirusSample.csv')

print(df['class'].value_counts())

for i in range(len(df)):
    if df['class'][i] == 'Downloader' or df['class'][i] == 'Spyware' or df['class'][i] == 'Ransomware' or df['class'][i] == 'Riskware' or df['class'][i] == 'Dropper' or df['class'][i] == 'Crypt' or df['class'][i] == 'Keylogger' or df['class'][i] == 'Adware' or df['class'][i] == 'Agent':
        df['class'][i] = 'Other'

print(df['class'].value_counts())

tNames = df['class'].unique().tolist()



def generate_N_grams(text,ngram=1):
    words=[word for word in text.split(",")]  
    #print("Sentence after removing stopwords:",words)
    temp=zip(*[words[i:] for i in range(ngram)])
    ans=[' '.join(ngram) for ngram in temp]
    return ans


#Minusculas
df['api'] = df['api'].str.lower()
print(len(df))

#Creando n-gramas

cv = CountVectorizer(ngram_range=(3,3))

ngrams = cv.fit_transform(df['api'])

#print(ngrams.shape)
#print(cv.get_feature_names())

ngrams_df = pd.DataFrame(ngrams.toarray(), columns=cv.get_feature_names_out())

print(ngrams_df)

#División de datos de entrenamientos y prueba
feature_matrix_train, feature_matrix_test, target_train, target_test = model_selection.train_test_split(ngrams_df, df['class'], test_size=0.30, random_state=32)

#Aplicación de modelo
clf = tree.DecisionTreeClassifier()
clf = clf.fit(feature_matrix_train, target_train)

#Guardando modelo
clf_pkl_model = open('model_desiciontree.pkl', 'wb')
pickle.dump(clf, clf_pkl_model)
clf_pkl_model.close()

'''print(feature_matrix_train.count())

print(feature_matrix_test.count())'''

target_pred = clf.predict(feature_matrix_test)

print(target_test.unique())


#Métricas
print(metrics.accuracy_score(target_test, target_pred))
#print('Matriz de confusion /n',metrics.confusion_matrix(target_test, target_pred))
print(metrics.classification_report(target_test, target_pred, target_names=tNames))