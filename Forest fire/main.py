{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3e9db130",
   "metadata": {},
   "source": [
    "# Forest fire area predictor"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "64a90953",
   "metadata": {},
   "source": [
    "## Reading data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b454ab22",
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
      " 2   month   517 non-null    object \n",
      " 3   day     517 non-null    object \n",
      " 4   FFMC    517 non-null    float64\n",
      " 5   DMC     517 non-null    float64\n",
      " 6   DC      517 non-null    float64\n",
      " 7   ISI     517 non-null    float64\n",
      " 8   temp    517 non-null    float64\n",
      " 9   RH      517 non-null    int64  \n",
      " 10  wind    517 non-null    float64\n",
      " 11  rain    517 non-null    float64\n",
      " 12  area    517 non-null    float64\n",
      "dtypes: float64(8), int64(3), object(2)\n",
      "memory usage: 52.6+ KB\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "forest_fire=pd.read_csv(\"forestfires.csv\")   #Reading data\n",
    "forest_fire.info()              #Some information about data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "de10f0d0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['X', 'Y', 'month', 'day', 'FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH',\n",
       "       'wind', 'rain', 'area'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "col=forest_fire.columns\n",
    "col#Viewing sample of data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "944fee7e",
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
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>4.669246</td>\n",
       "      <td>4.299807</td>\n",
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
       "                X           Y        FFMC         DMC          DC         ISI  \\\n",
       "count  517.000000  517.000000  517.000000  517.000000  517.000000  517.000000   \n",
       "mean     4.669246    4.299807   90.644681  110.872340  547.940039    9.021663   \n",
       "std      2.313778    1.229900    5.520111   64.046482  248.066192    4.559477   \n",
       "min      1.000000    2.000000   18.700000    1.100000    7.900000    0.000000   \n",
       "25%      3.000000    4.000000   90.200000   68.600000  437.700000    6.500000   \n",
       "50%      4.000000    4.000000   91.600000  108.300000  664.200000    8.400000   \n",
       "75%      7.000000    5.000000   92.900000  142.400000  713.900000   10.800000   \n",
       "max      9.000000    9.000000   96.200000  291.300000  860.600000   56.100000   \n",
       "\n",
       "             temp          RH        wind        rain         area  \n",
       "count  517.000000  517.000000  517.000000  517.000000   517.000000  \n",
       "mean    18.889168   44.288201    4.017602    0.021663    12.847292  \n",
       "std      5.806625   16.317469    1.791653    0.295959    63.655818  \n",
       "min      2.200000   15.000000    0.400000    0.000000     0.000000  \n",
       "25%     15.500000   33.000000    2.700000    0.000000     0.000000  \n",
       "50%     19.300000   42.000000    4.000000    0.000000     0.520000  \n",
       "75%     22.800000   53.000000    4.900000    0.000000     6.570000  \n",
       "max     33.300000  100.000000    9.400000    6.400000  1090.840000  "
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
   "cell_type": "code",
   "execution_count": 4,
   "id": "dd1b4790",
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
       "   X  Y  FFMC   DMC     DC  ISI  temp  RH  wind  rain  area\n",
       "0  7  5  86.2  26.2   94.3  5.1   8.2  51   6.7   0.0   0.0\n",
       "1  7  4  90.6  35.4  669.1  6.7  18.0  33   0.9   0.0   0.0\n",
       "2  7  4  90.6  43.7  686.9  6.7  14.6  33   1.3   0.0   0.0\n",
       "3  8  6  91.7  33.3   77.5  9.0   8.3  97   4.0   0.2   0.0\n",
       "4  8  6  89.3  51.3  102.2  9.6  11.4  99   1.8   0.0   0.0"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "forest_fire_mod=forest_fire.drop([\"month\",\"day\"],axis=1)\n",
    "forest_fire_mod.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "825f611a",
   "metadata": {},
   "source": [
    "## One hot encoding"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3dded234",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import OneHotEncoder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3dd5972b",
   "metadata": {},
   "outputs": [],
   "source": [
    "ohe=OneHotEncoder(drop=\"first\",sparse=False,dtype=np.int64)\n",
    "forest_fire_new=ohe.fit_transform(forest_fire[['month','day']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "75e04a08",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(517, 17)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "forest_fire_new.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "36654f19",
   "metadata": {},
   "outputs": [],
   "source": [
    "forest_fire=pd.DataFrame(np.hstack((forest_fire_mod,forest_fire_new)))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5ad0c6a9",
   "metadata": {},
   "source": [
    "## Train-Test split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4fa79944",
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
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "      <th>4</th>\n",
       "      <th>5</th>\n",
       "      <th>6</th>\n",
       "      <th>7</th>\n",
       "      <th>8</th>\n",
       "      <th>9</th>\n",
       "      <th>...</th>\n",
       "      <th>18</th>\n",
       "      <th>19</th>\n",
       "      <th>20</th>\n",
       "      <th>21</th>\n",
       "      <th>22</th>\n",
       "      <th>23</th>\n",
       "      <th>24</th>\n",
       "      <th>25</th>\n",
       "      <th>26</th>\n",
       "      <th>27</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>329</th>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>92.2</td>\n",
       "      <td>102.3</td>\n",
       "      <td>751.5</td>\n",
       "      <td>8.4</td>\n",
       "      <td>23.5</td>\n",
       "      <td>27.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>173</th>\n",
       "      <td>4.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>90.9</td>\n",
       "      <td>126.5</td>\n",
       "      <td>686.5</td>\n",
       "      <td>7.0</td>\n",
       "      <td>17.7</td>\n",
       "      <td>39.0</td>\n",
       "      <td>2.2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>272</th>\n",
       "      <td>2.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>92.1</td>\n",
       "      <td>152.6</td>\n",
       "      <td>658.2</td>\n",
       "      <td>14.3</td>\n",
       "      <td>20.2</td>\n",
       "      <td>47.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>497</th>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>96.1</td>\n",
       "      <td>181.1</td>\n",
       "      <td>671.2</td>\n",
       "      <td>14.3</td>\n",
       "      <td>32.3</td>\n",
       "      <td>27.0</td>\n",
       "      <td>2.2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>182</th>\n",
       "      <td>5.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>86.8</td>\n",
       "      <td>15.6</td>\n",
       "      <td>48.3</td>\n",
       "      <td>3.9</td>\n",
       "      <td>12.4</td>\n",
       "      <td>53.0</td>\n",
       "      <td>2.2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows ?? 28 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      0    1     2      3      4     5     6     7    8    9   ...   18   19  \\\n",
       "329  4.0  3.0  92.2  102.3  751.5   8.4  23.5  27.0  4.0  0.0  ...  0.0  0.0   \n",
       "173  4.0  4.0  90.9  126.5  686.5   7.0  17.7  39.0  2.2  0.0  ...  0.0  0.0   \n",
       "272  2.0  5.0  92.1  152.6  658.2  14.3  20.2  47.0  4.0  0.0  ...  0.0  0.0   \n",
       "497  3.0  4.0  96.1  181.1  671.2  14.3  32.3  27.0  2.2  0.0  ...  0.0  0.0   \n",
       "182  5.0  4.0  86.8   15.6   48.3   3.9  12.4  53.0  2.2  0.0  ...  0.0  0.0   \n",
       "\n",
       "      20   21   22   23   24   25   26   27  \n",
       "329  0.0  1.0  0.0  1.0  0.0  0.0  0.0  0.0  \n",
       "173  0.0  1.0  1.0  0.0  0.0  0.0  0.0  0.0  \n",
       "272  0.0  0.0  0.0  0.0  0.0  0.0  1.0  0.0  \n",
       "497  0.0  0.0  0.0  0.0  0.0  0.0  1.0  0.0  \n",
       "182  0.0  0.0  0.0  0.0  1.0  0.0  0.0  0.0  \n",
       "\n",
       "[5 rows x 28 columns]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "train_set,test_set=train_test_split(forest_fire,test_size=0.2,random_state=42)\n",
    "train_set.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "4b36b096",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(104, 28)"
      ]
     },
     "execution_count": 10,
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
   "id": "0b142913",
   "metadata": {},
   "source": [
    "## Feature and labels"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "56c8301c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(413, 27)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_features=train_set.drop(27,axis=1)\n",
    "train_labels=train_set[27].copy()\n",
    "train_features.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "36cf0deb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(413,)"
      ]
     },
     "execution_count": 12,
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
   "id": "223f8205",
   "metadata": {},
   "source": [
    "## Creating a pipeline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "7ca44ad1",
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
   "execution_count": 14,
   "id": "312b13fc",
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
   "execution_count": 15,
   "id": "d2f5ab1b",
   "metadata": {},
   "outputs": [],
   "source": [
    "pd_train_set=my_pipeline.fit_transform(train_features)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c5a642f7",
   "metadata": {},
   "source": [
    "## Selecting a model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "276f4d1d",
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
   "execution_count": 17,
   "id": "5831bae4",
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
   "execution_count": 18,
   "id": "d094a8e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 18,
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
   "execution_count": 19,
   "id": "0b613b4a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.02143157, 0.049782  , 0.18520062, 0.22886821, 0.01108564])"
      ]
     },
     "execution_count": 19,
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
   "execution_count": 20,
   "id": "56460fa4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "329    0.0\n",
       "173    0.0\n",
       "272    0.0\n",
       "497    0.0\n",
       "182    0.0\n",
       "Name: 27, dtype: float64"
      ]
     },
     "execution_count": 20,
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
   "execution_count": 21,
   "id": "eeabd453",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.05817562981247947"
      ]
     },
     "execution_count": 21,
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
   "id": "e8211e4c",
   "metadata": {},
   "source": [
    "## Cross validation evaluation "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "364a5de2",
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
   "execution_count": 23,
   "id": "329eec45",
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
   "execution_count": 24,
   "id": "43a86102",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.23967347 0.29828028 0.25506327 0.26844426 0.21272587]\n",
      "mean :  0.25483743062235586\n",
      "Standard deviation :  0.028551030652163238\n"
     ]
    }
   ],
   "source": [
    "print_score(rmse_score)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a570b1b0",
   "metadata": {},
   "source": [
    "## Storing data and Dumping model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "df55f198",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['forest_fire.joblib']"
      ]
     },
     "execution_count": 25,
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
   "execution_count": 26,
   "id": "a3a8ad0f",
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
   "execution_count": 27,
   "id": "111c3964",
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
   "execution_count": 28,
   "id": "61eb2d38",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0.39223227, -1.58113883,  0.19466156, -0.23579877,  0.72610598,\n",
       "       -0.28641452,  0.34435902, -1.10884271,  1.22474487,  0.        ,\n",
       "       -0.62284825, -0.81649658,  0.        , -0.5       ,  0.        ,\n",
       "        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,\n",
       "        0.        ,  1.22474487, -0.5       ,  2.        , -0.5       ,\n",
       "        0.        , -0.81649658])"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "prd_data[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e685ab4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5e17f84",
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
