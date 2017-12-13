
import librosa
import numpy as np
import keras
from keras.models import load_model



class ac_classifier():
    
    def __init__(self):
        self.mfcc = None
        self.model = load_model('model1_f0.17_acc0.241.hd5')
        
    def make_librosa_nor_mfcc(self,filename):
        y_, sr_ = librosa.load(filename,offset=0.05, duration= 21)
        y_ = librosa.util.fix_length(y_,463050)
        mfccs = librosa.feature.mfcc(y_, sr_, n_mfcc=13)
        mfccs = librosa.util.normalize(mfccs, axis= 1)
        self.mfcc = mfccs
        
    def _data_reshaping(self,X):
        dim,win_len = X.shape
        X_ = np.reshape(X,(1,dim,win_len,1))
        return X_
    
    def predict(self,filename):
        self.make_librosa_nor_mfcc(filename)
        x = self._data_reshaping(self.mfcc)
        prediction = self.model.predict(x)
        prediction = np.argmax(prediction)
        x_ = self.mfcc
        return prediction, x_

