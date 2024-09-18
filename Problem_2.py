{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNwXx6FYFq/WymDh6EW+To9",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/budhilsai-19/HandsOn-4/blob/main/Problem_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Wk-Lftcy7c8i",
        "outputId": "b0804a4e-3e8e-44a8-e889-2940221823e5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[2]\n",
            "[1, 2, 3, 4, 5]\n"
          ]
        }
      ],
      "source": [
        "def remove_duplicate(arr):\n",
        "    a=[]\n",
        "    for i in arr:\n",
        "        if i not in a:\n",
        "            a.append(i)\n",
        "    return a\n",
        "\n",
        "\n",
        "array = [2, 2, 2, 2, 2]\n",
        "print(remove_duplicate(array))\n",
        "array = [1, 2, 2, 3, 4, 4, 4, 5, 5]\n",
        "print(remove_duplicate(array))"
      ]
    }
  ]
}