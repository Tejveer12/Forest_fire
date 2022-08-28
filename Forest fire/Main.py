{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c8e87c4b",
   "metadata": {},
   "source": [
    "# Forest fire area predictor"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a59a755f",
   "metadata": {},
   "source": [
    "## Reading data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "810b3a48",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 517 entries, 0 to 516\n",
      "Data columns (total 13 columns):\n",
      " #   Column  Non-Null Count  Dtype  \n",
      "---  ------  --------------  -----  \n",
      " 0   X       517 non-null    int64  \n",
      " 1   Y       517 non-null    int64  \n",
      " 2   month   517 non-null    int64  \n",
      " 3   day     517 non-null    int64  \n",
      " 4   FFMC    517 non-null    float64\n",
      " 5   DMC     517 non-null    float64\n",
      " 6   DC      517 non-null    float64\n",
      " 7   ISI     517 non-null    float64\n",
      " 8   temp    517 non-null    float64\n",
      " 9   RH      517 non-null    int64  \n",
      " 10  wind    517 non-null    float64\n",
      " 11  rain    517 non-null    float64\n",
      " 12  area    517 non-null    float64\n",
      "dtypes: float64(8), int64(5)\n",
      "memory usage: 52.6 KB\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "forest_fire=pd.read_csv(\"forestfires.csv\")   #Reading data\n",
    "forest_fire.info()              #Some information about data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3423560e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>X</th>\n",
       "      <th>Y</th>\n",
       "      <th>month</th>\n",
       "      <th>day</th>\n",
       "      <th>FFMC</th>\n",
       "      <th>DMC</th>\n",
       "      <th>DC</th>\n",
       "      <th>ISI</th>\n",
       "      <th>temp</th>\n",
       "      <th>RH</th>\n",
       "      <th>wind</th>\n",
       "      <th>rain</th>\n",
       "      <th>area</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>7</td>\n",
       "      <td>5</td>\n",
       "      <td>3</td>\n",
       "      <td>5</td>\n",
       "      <td>86.2</td>\n",
       "      <td>26.2</td>\n",
       "      <td>94.3</td>\n",
       "      <td>5.1</td>\n",
       "      <td>8.2</td>\n",
       "      <td>51</td>\n",
       "      <td>6.7</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>7</td>\n",
       "      <td>4</td>\n",
       "      <td>10</td>\n",
       "      <td>3</td>\n",
       "      <td>90.6</td>\n",
       "      <td>35.4</td>\n",
       "      <td>669.1</td>\n",
       "      <td>6.7</td>\n",
       "      <td>18.0</td>\n",
       "      <td>33</td>\n",
       "      <td>0.9</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>7</td>\n",
       "      <td>4</td>\n",
       "      <td>10</td>\n",
       "      <td>6</td>\n",
       "      <td>90.6</td>\n",
       "      <td>43.7</td>\n",
       "      <td>686.9</td>\n",
       "      <td>6.7</td>\n",
       "      <td>14.6</td>\n",
       "      <td>33</td>\n",
       "      <td>1.3</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>8</td>\n",
       "      <td>6</td>\n",
       "      <td>3</td>\n",
       "      <td>5</td>\n",
       "      <td>91.7</td>\n",
       "      <td>33.3</td>\n",
       "      <td>77.5</td>\n",
       "      <td>9.0</td>\n",
       "      <td>8.3</td>\n",
       "      <td>97</td>\n",
       "      <td>4.0</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>8</td>\n",
       "      <td>6</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>89.3</td>\n",
       "      <td>51.3</td>\n",
       "      <td>102.2</td>\n",
       "      <td>9.6</td>\n",
       "      <td>11.4</td>\n",
       "      <td>99</td>\n",
       "      <td>1.8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   X  Y  month  day  FFMC   DMC     DC  ISI  temp  RH  wind  rain  area\n",
       "0  7  5      3    5  86.2  26.2   94.3  5.1   8.2  51   6.7   0.0   0.0\n",
       "1  7  4     10    3  90.6  35.4  669.1  6.7  18.0  33   0.9   0.0   0.0\n",
       "2  7  4     10    6  90.6  43.7  686.9  6.7  14.6  33   1.3   0.0   0.0\n",
       "3  8  6      3    5  91.7  33.3   77.5  9.0   8.3  97   4.0   0.2   0.0\n",
       "4  8  6      3    1  89.3  51.3  102.2  9.6  11.4  99   1.8   0.0   0.0"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "forest_fire.head()  #Viewing sample of data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d7c6fa64",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>X</th>\n",
       "      <th>Y</th>\n",
       "      <th>month</th>\n",
       "      <th>day</th>\n",
       "      <th>FFMC</th>\n",
       "      <th>DMC</th>\n",
       "      <th>DC</th>\n",
       "      <th>ISI</th>\n",
       "      <th>temp</th>\n",
       "      <th>RH</th>\n",
       "      <th>wind</th>\n",
       "      <th>rain</th>\n",
       "      <th>area</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>517.000000</td>\n",
       "      <td>517.000000</td>\n",
       "      <td>517.000000</td>\n",
       "      <td>517.000000</td>\n",
       "      <td>517.000000</td>\n",
       "      <td>517.000000</td>\n",
       "      <td>517.000000</td>\n",
       "      <td>517.000000</td>\n",
       "      <td>517.000000</td>\n",
       "      <td>517.000000</td>\n",
       "      <td>517.000000</td>\n",
       "      <td>517.000000</td>\n",
       "      <td>517.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>4.669246</td>\n",
       "      <td>4.299807</td>\n",
       "      <td>7.475822</td>\n",
       "      <td>3.423598</td>\n",
       "      <td>90.644681</td>\n",
       "      <td>110.872340</td>\n",
       "      <td>547.940039</td>\n",
       "      <td>9.021663</td>\n",
       "      <td>18.889168</td>\n",
       "      <td>44.288201</td>\n",
       "      <td>4.017602</td>\n",
       "      <td>0.021663</td>\n",
       "      <td>12.847292</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>2.313778</td>\n",
       "      <td>1.229900</td>\n",
       "      <td>2.275990</td>\n",
       "      <td>1.715316</td>\n",
       "      <td>5.520111</td>\n",
       "      <td>64.046482</td>\n",
       "      <td>248.066192</td>\n",
       "      <td>4.559477</td>\n",
       "      <td>5.806625</td>\n",
       "      <td>16.317469</td>\n",
       "      <td>1.791653</td>\n",
       "      <td>0.295959</td>\n",
       "      <td>63.655818</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>18.700000</td>\n",
       "      <td>1.100000</td>\n",
       "      <td>7.900000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.200000</td>\n",
       "      <td>15.000000</td>\n",
       "      <td>0.400000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>90.200000</td>\n",
       "      <td>68.600000</td>\n",
       "      <td>437.700000</td>\n",
       "      <td>6.500000</td>\n",
       "      <td>15.500000</td>\n",
       "      <td>33.000000</td>\n",
       "      <td>2.700000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>4.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>91.600000</td>\n",
       "      <td>108.300000</td>\n",
       "      <td>664.200000</td>\n",
       "      <td>8.400000</td>\n",
       "      <td>19.300000</td>\n",
       "      <td>42.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.520000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>7.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>92.900000</td>\n",
       "      <td>142.400000</td>\n",
       "      <td>713.900000</td>\n",
       "      <td>10.800000</td>\n",
       "      <td>22.800000</td>\n",
       "      <td>53.000000</td>\n",
       "      <td>4.900000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>6.570000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>9.000000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>12.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>96.200000</td>\n",
       "      <td>291.300000</td>\n",
       "      <td>860.600000</td>\n",
       "      <td>56.100000</td>\n",
       "      <td>33.300000</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>9.400000</td>\n",
       "      <td>6.400000</td>\n",
       "      <td>1090.840000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                X           Y       month         day        FFMC         DMC  \\\n",
       "count  517.000000  517.000000  517.000000  517.000000  517.000000  517.000000   \n",
       "mean     4.669246    4.299807    7.475822    3.423598   90.644681  110.872340   \n",
       "std      2.313778    1.229900    2.275990    1.715316    5.520111   64.046482   \n",
       "min      1.000000    2.000000    1.000000    1.000000   18.700000    1.100000   \n",
       "25%      3.000000    4.000000    7.000000    2.000000   90.200000   68.600000   \n",
       "50%      4.000000    4.000000    8.000000    3.000000   91.600000  108.300000   \n",
       "75%      7.000000    5.000000    9.000000    5.000000   92.900000  142.400000   \n",
       "max      9.000000    9.000000   12.000000    6.000000   96.200000  291.300000   \n",
       "\n",
       "               DC         ISI        temp          RH        wind        rain  \\\n",
       "count  517.000000  517.000000  517.000000  517.000000  517.000000  517.000000   \n",
       "mean   547.940039    9.021663   18.889168   44.288201    4.017602    0.021663   \n",
       "std    248.066192    4.559477    5.806625   16.317469    1.791653    0.295959   \n",
       "min      7.900000    0.000000    2.200000   15.000000    0.400000    0.000000   \n",
       "25%    437.700000    6.500000   15.500000   33.000000    2.700000    0.000000   \n",
       "50%    664.200000    8.400000   19.300000   42.000000    4.000000    0.000000   \n",
       "75%    713.900000   10.800000   22.800000   53.000000    4.900000    0.000000   \n",
       "max    860.600000   56.100000   33.300000  100.000000    9.400000    6.400000   \n",
       "\n",
       "              area  \n",
       "count   517.000000  \n",
       "mean     12.847292  \n",
       "std      63.655818  \n",
       "min       0.000000  \n",
       "25%       0.000000  \n",
       "50%       0.520000  \n",
       "75%       6.570000  \n",
       "max    1090.840000  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "forest_fire.describe()    #Description about data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0f215bf5",
   "metadata": {},
   "source": [
    "## Train-Test split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b40ea71d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>X</th>\n",
       "      <th>Y</th>\n",
       "      <th>month</th>\n",
       "      <th>day</th>\n",
       "      <th>FFMC</th>\n",
       "      <th>DMC</th>\n",
       "      <th>DC</th>\n",
       "      <th>ISI</th>\n",
       "      <th>temp</th>\n",
       "      <th>RH</th>\n",
       "      <th>wind</th>\n",
       "      <th>rain</th>\n",
       "      <th>area</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>329</th>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>9</td>\n",
       "      <td>6</td>\n",
       "      <td>92.2</td>\n",
       "      <td>102.3</td>\n",
       "      <td>751.5</td>\n",
       "      <td>8.4</td>\n",
       "      <td>23.5</td>\n",
       "      <td>27</td>\n",
       "      <td>4.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>3.33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>173</th>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>9</td>\n",
       "      <td>2</td>\n",
       "      <td>90.9</td>\n",
       "      <td>126.5</td>\n",
       "      <td>686.5</td>\n",
       "      <td>7.0</td>\n",
       "      <td>17.7</td>\n",
       "      <td>39</td>\n",
       "      <td>2.2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>3.07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>272</th>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>8</td>\n",
       "      <td>3</td>\n",
       "      <td>92.1</td>\n",
       "      <td>152.6</td>\n",
       "      <td>658.2</td>\n",
       "      <td>14.3</td>\n",
       "      <td>20.2</td>\n",
       "      <td>47</td>\n",
       "      <td>4.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>3.09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>497</th>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>8</td>\n",
       "      <td>3</td>\n",
       "      <td>96.1</td>\n",
       "      <td>181.1</td>\n",
       "      <td>671.2</td>\n",
       "      <td>14.3</td>\n",
       "      <td>32.3</td>\n",
       "      <td>27</td>\n",
       "      <td>2.2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>14.68</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>182</th>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>86.8</td>\n",
       "      <td>15.6</td>\n",
       "      <td>48.3</td>\n",
       "      <td>3.9</td>\n",
       "      <td>12.4</td>\n",
       "      <td>53</td>\n",
       "      <td>2.2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>6.38</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     X  Y  month  day  FFMC    DMC     DC   ISI  temp  RH  wind  rain   area\n",
       "329  4  3      9    6  92.2  102.3  751.5   8.4  23.5  27   4.0   0.0   3.33\n",
       "173  4  4      9    2  90.9  126.5  686.5   7.0  17.7  39   2.2   0.0   3.07\n",
       "272  2  5      8    3  92.1  152.6  658.2  14.3  20.2  47   4.0   0.0   3.09\n",
       "497  3  4      8    3  96.1  181.1  671.2  14.3  32.3  27   2.2   0.0  14.68\n",
       "182  5  4      2    1  86.8   15.6   48.3   3.9  12.4  53   2.2   0.0   6.38"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "from sklearn.model_selection import train_test_split\n",
    "train_set,test_set=train_test_split(forest_fire,test_size=0.2,random_state=42)\n",
    "train_set.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ff62ad7d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(104, 13)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test_set.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d3fc3fd5",
   "metadata": {},
   "source": [
    "## Feature and labels"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "6dea0928",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(413, 12)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_features=train_set.drop(\"area\",axis=1)\n",
    "train_labels=train_set['area'].copy()\n",
    "train_features.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "03383f4d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(413,)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_labels.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b1bb9ac4",
   "metadata": {},
   "source": [
    "## Creating a pipeline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "beaaa5d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler \n",
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.impute import SimpleImputer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "0bad6739",
   "metadata": {},
   "outputs": [],
   "source": [
    "my_pipeline=Pipeline([\n",
    "    (\"imputer\",SimpleImputer(strategy=\"median\")),\n",
    "    (\"scalar\",StandardScaler())\n",
    "]\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "31dfef01",
   "metadata": {},
   "outputs": [],
   "source": [
    "pd_train_set=my_pipeline.fit_transform(train_features)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d6be9d07",
   "metadata": {},
   "source": [
    "## Selecting a model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "59705cf8",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.tree import DecisionTreeRegressor\n",
    "from sklearn.ensemble import RandomForestRegressor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "582837cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "model=LinearRegression()\n",
    "#model=DecisionTreeRegressor()\n",
    "#model=RandomForestRegressor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "682f81b8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.fit(pd_train_set,train_labels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e7711e52",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([15.87603452, 12.31341182,  4.47678242, 20.18237419,  2.81205081])"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "some_data=train_features.iloc[:5]\n",
    "prd_data=my_pipeline.fit_transform(some_data)\n",
    "some_labels=train_labels.iloc[:5]\n",
    "model.predict(prd_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "780ff2c6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "329     3.33\n",
       "173     3.07\n",
       "272     3.09\n",
       "497    14.68\n",
       "182     6.38\n",
       "Name: area, dtype: float64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "some_labels"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "0d56c18c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2004.0296690814466"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import mean_squared_error\n",
    "pdt=model.predict(pd_train_set)\n",
    "err=mean_squared_error(train_labels,pdt)\n",
    "err"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b218e730",
   "metadata": {},
   "source": [
    "## Cross validation evaluation "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "12bc3c3b",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import cross_val_score\n",
    "score=cross_val_score(model,pd_train_set,train_labels,scoring=\"neg_mean_squared_error\")\n",
    "rmse_score=np.sqrt(-score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "31094a63",
   "metadata": {},
   "outputs": [],
   "source": [
    "def print_score(a):\n",
    "    print(a)\n",
    "    print(\"mean : \",a.mean())\n",
    "    print(\"Standard deviation : \",a.std())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "c4fac684",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[39.8957861  18.03546782 33.21892645 84.53767632 24.48542125]\n",
      "mean :  40.03465558810302\n",
      "Standard deviation :  23.46373905979108\n"
     ]
    }
   ],
   "source": [
    "print_score(rmse_score)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9a354175",
   "metadata": {},
   "source": [
    "## Storing data and Dumping model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "96c8b35e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['forest_fire.joblib']"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from joblib import dump, load\n",
    "dump(model,\"forest_fire.joblib\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "1493079b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Stored 'test_set' (DataFrame)\n"
     ]
    }
   ],
   "source": [
    "%store test_set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "10c04a18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Stored 'my_pipeline' (Pipeline)\n"
     ]
    }
   ],
   "source": [
    "%store my_pipeline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b32981af",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3fb087ea",
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
