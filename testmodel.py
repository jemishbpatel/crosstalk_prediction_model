from skimage.io import imread
import matplotlib.pyplot as plt
import pickle
from skimage.transform import resize
import sys

Categories=[ 'D_122_H_117', 'D_122_H_165', 'D_127_H_109', 'D_152_H_74', 'D_183_H_127', 'D_213_H_114',
             'D_213_H_127', 'D_213_H_165', 'D_244_H_127', 'D_274_H_114', 'D_274_H_165', 'D_335_H_71',
             'D_335_H_99', 'D_366_H_127', 'D_366_H_165', 'D_396_H_127', 'D_488_H_71', 'D_518_H_114' ]


model=pickle.load(open('img_model.p','rb'))
input_elements = []
input_elements.append( int( sys.argv[ 1 ] ) )
input_elements.append( int( sys.argv[ 2 ] ) )
input_distance_height = [ input_elements ]
#url=input('Enter URL of Image')
#img=imread(url)
#plt.imshow(img)
#plt.show()
#img_resize=resize(img,(150,150,3))
#l=[img_resize.flatten()]
probability=model.predict_proba( input_distance_height )
for ind,val in enumerate(Categories):
        #print('{val} = {probability[0][ind]*100}%')
        print("val = %d" % (probability[0][ind]*100))
print( "Prdicted cross talk type is : %s" % model.predict(input_distance_height)[0] )

