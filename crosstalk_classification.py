import pandas as pd
from sklearn import svm
from sklearn.model_selection import GridSearchCV
import os
import matplotlib.pyplot as plt
from skimage.transform import resize
from skimage.io import imread
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix
import pickle

Categories=[ 'D_122_H_117', 'D_122_H_165', 'D_127_H_109', 'D_152_H_74', 'D_183_H_127', 'D_213_H_114',
	     'D_213_H_127', 'D_213_H_165', 'D_244_H_127', 'D_274_H_114', 'D_274_H_165', 'D_335_H_71',
	     'D_335_H_99', 'D_366_H_127', 'D_366_H_165', 'D_396_H_127', 'D_488_H_71', 'D_518_H_114' ]

#TODO
IMAGE_PATH = "/home/jemish/practice/svr/svm_model/black_white/0001.jpeg"
flat_data_arr=[]
target_arr=[]
#please use datadir='/content' if the files are upload on to google collab
#else mount the drive and give path of the parent-folder containing all category images folders.
#datadir='/home/jemish/practice/svr/svm_model/debug_model'
for reading in Categories:
	print( 'loading... category : %s' % reading )
	midheight =  int( reading.split( '_' )[ 3 ] )
	distance = int( reading.split( '_' )[ 1 ] )
	midheight_range = (( midheight - 3 ), ( midheight + 3 ) )
	for height in range( midheight_range[ 0 ], midheight_range[ 1 ] + 1 ):
		#flat_data_arr.append( [ imread( IMAGE_PATH), distance, height ] )
		flat_data_arr.append( [ distance, height ] )
		target_arr.append( reading  )
	print( 'loaded category:%s successfully' % reading )

flat_data=np.array(flat_data_arr, dtype = object)
target=np.array(target_arr)
df=pd.DataFrame(flat_data)
df['Target']=target
print( df['Target'] )

x=df.iloc[:,:-1]
y=df.iloc[:,-1]
print(y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=77,stratify=y)
print('Splitted Successfully')


param_grid={'C':[0.1,1,10,100],'gamma':[0.0001,0.001,0.1,1],'kernel':['rbf','poly']}
svc=svm.SVC(probability=True)
print("The training of the model is started, please wait for while as it may take few minutes to complete")
model=GridSearchCV(svc,param_grid)
model.fit(x_train,y_train)
print('The Model is trained well with the given images')
print( model.best_params_ )

y_pred=model.predict(x_test)
print("The predicted Data is :")
print ( y_pred )

print("The actual data is:")
print ( np.array(y_test) )

#print("The model is %f accurate" % accuracy_score(y_pred,y_test)*100 )

pickle.dump(model,open('img_model.p','wb'))
print("Pickle is dumped successfully")
