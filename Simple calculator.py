{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO9XQgZZZ6l9Al/mFfO3d5j",
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
        "<a href=\"https://colab.research.google.com/github/sendora123/Roadmap.py/blob/main/Simple%20calculator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def calculator(num1, num2):\n",
        "    operator = input(\"Enter operator (+, -, /, *): \")\n",
        "\n",
        "    if operator == \"+\":\n",
        "        Result = num1 + num2\n",
        "    elif operator == \"-\":\n",
        "        Result = num1 - num2\n",
        "    elif operator == \"*\":\n",
        "        Result = num1 * num2\n",
        "    elif operator == \"/\":\n",
        "        if num2 == 0:\n",
        "            return \"Error: Cannot divide by zero.\"\n",
        "        Result = num1 / num2\n",
        "    else:\n",
        "        return f\"Error: '{operator}' is not a valid operator. Use +, -, *, or /\"\n",
        "\n",
        "    return Result\n",
        "\n",
        "\n",
        "# MAIN PROGRAM\n",
        "while True:\n",
        "    try:\n",
        "        num1 = float(input(\"\\nEnter the first number:  \"))\n",
        "        num2 = float(input(\"Enter the second number: \"))\n",
        "        Result = calculator(num1, num2)\n",
        "        print(f\"\\nThe Result is: {Result}\")\n",
        "    except ValueError:\n",
        "        print(\"Error: Please enter valid numbers.\")\n",
        "\n",
        "    again = input(\"\\nDo you want to calculate again? (yes/no): \").strip().lower()\n",
        "    if again != \"yes\":\n",
        "        print(\"\\nThank you for using the calculator. Goodbye!\")\n",
        "        break"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8nVQJ5CMYYHY",
        "outputId": "7fcf2407-1cf3-4a43-b631-f6b3c74522f0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Enter the first number:  3\n",
            "Enter the second number: 4\n",
            "Enter operator (+, -, /, *): *\n",
            "\n",
            "The Result is: 12.0\n",
            "\n",
            "Do you want to calculate again? (yes/no): no\n",
            "\n",
            "Thank you for using the calculator. Goodbye!\n"
          ]
        }
      ]
    }
  ]
}