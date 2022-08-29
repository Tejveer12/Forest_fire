{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "544f7532",
   "metadata": {},
   "outputs": [],
   "source": [
    "from joblib import load\n",
    "model=load(\"forest_fire.joblib\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "fa2aaef1",
   "metadata": {},
   "outputs": [],
   "source": [
    "%store -r test_set\n",
    "%store -r my_pipeline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bb510c32",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_features=test_set.drop(27,axis=1)\n",
    "test_labels=test_set[27].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "afe1a5bb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(104, 27)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test_features.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "031dedf9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(104,)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test_labels.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a72e4761",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_features_tr=my_pipeline.fit_transform(test_features)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c5f10530",
   "metadata": {},
   "outputs": [],
   "source": [
    "pdt_labels=model.predict(test_features_tr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "d8ca48c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import mean_squared_error\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "80f6b005",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.27219808709958515"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "err=mean_squared_error(test_labels,pdt_labels)\n",
    "rt_err=np.sqrt(err)\n",
    "rt_err"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d2593bd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50917392",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
