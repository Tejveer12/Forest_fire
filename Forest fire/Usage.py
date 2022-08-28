{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e5ed1275",
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
   "id": "425cdbfd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3ea70289",
   "metadata": {},
   "outputs": [],
   "source": [
    "input=np.array([[ 0.39223227, -1.58113883,  0.68228824,  1.79284291,  0.19466156,\n",
    "       -0.23579877,  0.72610598, -0.28641452,  0.34435902, -1.10884271,\n",
    "        1.22474487,  0.        ]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "fa982296",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([15.87603447])"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.predict(input)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fde1b990",
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
