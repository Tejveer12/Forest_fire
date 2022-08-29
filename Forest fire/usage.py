{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6f2f3766",
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
   "id": "83311117",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9a5d6b6b",
   "metadata": {},
   "outputs": [],
   "source": [
    "input=np.array([ 0.39223227, -1.58113883,  0.19466156, -0.23579877,  0.72610598,\n",
    "       -0.28641452,  0.34435902, -1.10884271,  1.22474487,  0.        ,\n",
    "       -0.62284825, -0.81649658,  0.        , -0.5       ,  0.        ,\n",
    "        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,\n",
    "        0.        ,  1.22474487, -0.5       ,  2.        , -0.5       ,\n",
    "        0.        , -0.81649658])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "edb4339b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.02143156])"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.predict([[ 0.39223227, -1.58113883,  0.19466156, -0.23579877,  0.72610598,\n",
    "       -0.28641452,  0.34435902, -1.10884271,  1.22474487,  0.        ,\n",
    "       -0.62284825, -0.81649658,  0.        , -0.5       ,  0.        ,\n",
    "        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,\n",
    "        0.        ,  1.22474487, -0.5       ,  2.        , -0.5       ,\n",
    "        0.        , -0.81649658]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45ec594c",
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
