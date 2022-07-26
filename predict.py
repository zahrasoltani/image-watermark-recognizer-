import pandas as pd
from keras.models import load_model
from keras.preprocessing.image import load_img
import numpy as np
import os


file_list=os.listdir(r'dataset/test/testt')

df = pd.DataFrame(file_list)
df["predict"] = ""
#print(df)

df.to_csv("watermark.csv" , index=False) 

model = load_model('model_savedd.h5')


for i in range(len(df)):
    image = load_img('dataset/test/testt/{}'.format(df.iloc[i,0]), target_size=(224, 224))
    img = np.array(image)
    img = img / 255.0
    img = img.reshape(1,224,224,3)
    label = model.predict(img)
    final = round(label[0][0])
    df.iloc[i,1] = final
    print(i)
    

#print(df)
df.to_csv("watermark.csv" , index=False)