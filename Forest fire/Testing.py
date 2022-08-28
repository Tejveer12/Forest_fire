{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2c036193",
   "metadata": {},
   "outputs": [],
   "source": [
    "from joblib import load\n",
    "model=load(\"forest_fire.joblib\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "e6fd1402",
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
   "id": "860fa01e",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_features=test_set.drop(\"area\",axis=1)\n",
    "test_labels=test_set[\"area\"].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "99f69817",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(104, 12)"
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
   "id": "07cc6de7",
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
   "execution_count": 8,
   "id": "5d9ed2df",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_features_tr=my_pipeline.fit_transform(test_features)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4ba73882",
   "metadata": {},
   "outputs": [],
   "source": [
    "pdt_labels=model.predict(test_features_tr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "7564e6b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import mean_squared_error\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f3b3a590",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "108.27664293339325"
      ]
     },
     "execution_count": 15,
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
   "id": "92878cbe",
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
