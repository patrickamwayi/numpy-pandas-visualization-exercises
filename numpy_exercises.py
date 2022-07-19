{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "013311b6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "\n",
    "import numpy as np\n",
    "# Use the following code for the questions below:\n",
    "\n",
    "\n",
    "a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])\n",
    "# 1.\n",
    "# How many negative numbers are there?\n",
    "\n",
    "print(len(a[a < 0 ]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d1794b23",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "# 2.\n",
    "# How many positive numbers are there?\n",
    "print(len(a[a > 0 ]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a73269e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "# 3.\n",
    "# How many even positive numbers are there?\n",
    "print(len(a[(a > 0) & (a % 2 == 0)]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0a4ddb90",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n"
     ]
    }
   ],
   "source": [
    "#4.\n",
    "# If you were to add 3 to each data point, how many positive numbers would there be?\n",
    "b = a + 3\n",
    "print(len(b[b > 0]))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "e0d7f016",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "74.0 144.0243035046516\n"
     ]
    }
   ],
   "source": [
    "#5.\n",
    "# If you squared each number, what would the new mean and standard deviation be?\n",
    "b = a ** 2\n",
    "print(b.mean(), b.std())\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5d977377",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[  1.   7.   9.  20.  -5.  -4.  -3.  -3.  -3.  -9.   0. -10.]\n"
     ]
    }
   ],
   "source": [
    "#6.\n",
    "# A common statistical operation on a dataset is centering. \n",
    "#This means to adjust the data such that the mean of the data is 0. \n",
    "#This is done by subtracting the mean from each data point. \n",
    "#Center the data set. See this link for more on centering.\n",
    "\n",
    "a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])\n",
    "print(a - a.mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "4ba15599",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 0.12403473  0.86824314  1.11631261  2.48069469 -0.62017367 -0.49613894\n",
      " -0.3721042  -0.3721042  -0.3721042  -1.11631261  0.         -1.24034735]\n"
     ]
    }
   ],
   "source": [
    "#7.\n",
    "# Calculate the z-score for each data point. Recall that the z-score is given by:\n",
    "\n",
    "\n",
    "\n",
    "print((a - a.mean()) / a.std())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "330fa5ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "# \n",
    "#8.   Life w/o numpy to life with numpy\n",
    "\n",
    "## Setup 1\n",
    "a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "\n",
    "# Use python's built in functionality/operators to determine the following:\n",
    "\n",
    "# Exercise 1\n",
    "# - Make a variable called sum_of_a to hold the sum of all the numbers in above list\n",
    "sum_of_a = sum(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "ef942923",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 2 \n",
    "# - Make a variable named min_of_a to hold the minimum of all the numbers in the above list\n",
    "min_of_a = min(a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "d44e32a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 3\n",
    "# - Make a variable named max_of_a to hold the max number of all the numbers in the above list\n",
    "max_of_a = max(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "4385c012",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 4 \n",
    "# - Make a variable named mean_of_a to hold the average of all the numbers in the above list\n",
    "mean_of_a = sum_of_a/len(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "0b7d3d5d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 5\n",
    "# - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together\n",
    "product_a = sum(a)\n",
    "product_of_a = 1\n",
    "for num in a:\n",
    "    product_a *=num "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "525cf3f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 6\n",
    "# - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]\n",
    "squares_of_a = [num * num for num in a]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "5741feab",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 7\n",
    "# - Make a variable named odds_in_a. It should hold only the odd numbers\n",
    "odds_in_a = [num for num in a if num % 2 == 1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "3816063d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 8 \n",
    "# - Make a variable named evens_in_a. It should hold only the evens.\n",
    "evens_in_a = [num for num in a if num % 2 == 1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af3ca04f",
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
