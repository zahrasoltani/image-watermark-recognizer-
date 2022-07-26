# image-watermark-recognizer
training a model using neural network (tf.Keras) to recognize watermark in images on DigiKala dataset

how to run:
- give the model train and test file directory (directories include images) in watermark.py .
- the model will automatically saved.
- in predict.py you can load the saved model, and give the test images directory.
- it will return an excel file. the first column will be include name of all images which are in test directory. the second column will ne 0 or 1.
- 0 means no watermark on photo. 1 means watermark on photo.
