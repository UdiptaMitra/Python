{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "244cfda6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Player A turn\n",
      "Player B turn\n",
      "Player A turn\n",
      "Player B turn\n",
      "Player A turn\n",
      "Player B turn\n"
     ]
    }
   ],
   "source": [
    "def playerA(n):\n",
    "    if n == 0:\n",
    "        return\n",
    "    print(\"Player A turn\")\n",
    "    playerB(n - 1)\n",
    "\n",
    "def playerB(n):\n",
    "    if n == 0:\n",
    "        return\n",
    "    print(\"Player B turn\")\n",
    "    playerA(n - 1)\n",
    "\n",
    "playerA(6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "08f9a4bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Player A:\n",
      "1 2 3 4 5 \n",
      "\n",
      "Player B:\n",
      "3 1\n",
      "\n",
      "Player A:\n",
      "2 3 4 5 6 \n",
      "\n",
      "Player B:\n",
      "4 2\n",
      "\n",
      "Player A:\n",
      "3 4 5 6 7 \n",
      "\n",
      "Player B:\n",
      "5 3\n",
      "\n",
      "Player A:\n",
      "4 5 6 7 8 \n",
      "\n",
      "Player B:\n",
      "6 4\n",
      "\n",
      "Player A:\n",
      "5 6 7 8 9 \n",
      "\n",
      "Player B:\n",
      "7 5\n",
      "\n"
     ]
    }
   ],
   "source": [
    "def playerA(n,x=1):\n",
    "    if n == 0:      # stopping condition\n",
    "        return\n",
    "    \n",
    "    print(\"Player A:\")\n",
    "    last = x\n",
    "    for i in range(5):\n",
    "        print(last, end=\" \")\n",
    "        last += 1\n",
    "    \n",
    "    print(\"\\n\")\n",
    "    playerB(n - 1 , last - 1 )   # pass the last printed value\n",
    "\n",
    "\n",
    "def playerB(n, y=1 ):\n",
    "    if n == 0:      # stopping condition\n",
    "        return\n",
    "    \n",
    "    print(\"Player B:\")\n",
    "    print(y-2, y-4)\n",
    "    print()\n",
    "    \n",
    "    playerA(n-1, y-3)  # continue from decreased value\n",
    "\n",
    "\n",
    "playerA(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ba3a3752",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
