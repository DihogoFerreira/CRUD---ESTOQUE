{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNzxE3NuyeVvY8ggtnbNUd1",
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
        "<a href=\"https://colab.research.google.com/github/DihogoFerreira/CRUD---ESTOQUE/blob/main/tradutor.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Instala a biblioteca do Google Translate\n",
        "!pip install googletrans==4.0.0-rc1\n",
        "\n",
        "# Importa a classe Translator da biblioteca googletrans\n",
        "from googletrans import Translator\n",
        "\n",
        "# Cria um objeto Translator\n",
        "translator = Translator()\n",
        "\n",
        "# Define o texto que queremos traduzir\n",
        "texto_original = \"Olá, como você está?\"\n",
        "\n",
        "# Traduz o texto para o inglês\n",
        "texto_traduzido = translator.translate(texto_original, dest='en')\n",
        "\n",
        "# Imprime o texto traduzido\n",
        "print(\"Texto Original:\", texto_original)\n",
        "print(\"Texto Traduzido para Inglês:\", texto_traduzido.text)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hFRTr02D6c68",
        "outputId": "88af1cf7-1aee-43e4-ab3c-d5b003e89ddf"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting googletrans==4.0.0-rc1\n",
            "  Downloading googletrans-4.0.0rc1.tar.gz (20 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Collecting httpx==0.13.3 (from googletrans==4.0.0-rc1)\n",
            "  Downloading httpx-0.13.3-py3-none-any.whl.metadata (25 kB)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx==0.13.3->googletrans==4.0.0-rc1) (2024.8.30)\n",
            "Collecting hstspreload (from httpx==0.13.3->googletrans==4.0.0-rc1)\n",
            "  Downloading hstspreload-2024.11.1-py3-none-any.whl.metadata (2.1 kB)\n",
            "Requirement already satisfied: sniffio in /usr/local/lib/python3.10/dist-packages (from httpx==0.13.3->googletrans==4.0.0-rc1) (1.3.1)\n",
            "Collecting chardet==3.* (from httpx==0.13.3->googletrans==4.0.0-rc1)\n",
            "  Downloading chardet-3.0.4-py2.py3-none-any.whl.metadata (3.2 kB)\n",
            "Collecting idna==2.* (from httpx==0.13.3->googletrans==4.0.0-rc1)\n",
            "  Downloading idna-2.10-py2.py3-none-any.whl.metadata (9.1 kB)\n",
            "Collecting rfc3986<2,>=1.3 (from httpx==0.13.3->googletrans==4.0.0-rc1)\n",
            "  Downloading rfc3986-1.5.0-py2.py3-none-any.whl.metadata (6.5 kB)\n",
            "Collecting httpcore==0.9.* (from httpx==0.13.3->googletrans==4.0.0-rc1)\n",
            "  Downloading httpcore-0.9.1-py3-none-any.whl.metadata (4.6 kB)\n",
            "Collecting h11<0.10,>=0.8 (from httpcore==0.9.*->httpx==0.13.3->googletrans==4.0.0-rc1)\n",
            "  Downloading h11-0.9.0-py2.py3-none-any.whl.metadata (8.1 kB)\n",
            "Collecting h2==3.* (from httpcore==0.9.*->httpx==0.13.3->googletrans==4.0.0-rc1)\n",
            "  Downloading h2-3.2.0-py2.py3-none-any.whl.metadata (32 kB)\n",
            "Collecting hyperframe<6,>=5.2.0 (from h2==3.*->httpcore==0.9.*->httpx==0.13.3->googletrans==4.0.0-rc1)\n",
            "  Downloading hyperframe-5.2.0-py2.py3-none-any.whl.metadata (7.2 kB)\n",
            "Collecting hpack<4,>=3.0 (from h2==3.*->httpcore==0.9.*->httpx==0.13.3->googletrans==4.0.0-rc1)\n",
            "  Downloading hpack-3.0.0-py2.py3-none-any.whl.metadata (7.0 kB)\n",
            "Downloading httpx-0.13.3-py3-none-any.whl (55 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m55.1/55.1 kB\u001b[0m \u001b[31m5.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading chardet-3.0.4-py2.py3-none-any.whl (133 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m133.4/133.4 kB\u001b[0m \u001b[31m4.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading httpcore-0.9.1-py3-none-any.whl (42 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m42.6/42.6 kB\u001b[0m \u001b[31m2.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading idna-2.10-py2.py3-none-any.whl (58 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m58.8/58.8 kB\u001b[0m \u001b[31m5.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading h2-3.2.0-py2.py3-none-any.whl (65 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m65.0/65.0 kB\u001b[0m \u001b[31m6.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading rfc3986-1.5.0-py2.py3-none-any.whl (31 kB)\n",
            "Downloading hstspreload-2024.11.1-py3-none-any.whl (1.2 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.2/1.2 MB\u001b[0m \u001b[31m24.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading h11-0.9.0-py2.py3-none-any.whl (53 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m53.6/53.6 kB\u001b[0m \u001b[31m5.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading hpack-3.0.0-py2.py3-none-any.whl (38 kB)\n",
            "Downloading hyperframe-5.2.0-py2.py3-none-any.whl (12 kB)\n",
            "Building wheels for collected packages: googletrans\n",
            "  Building wheel for googletrans (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for googletrans: filename=googletrans-4.0.0rc1-py3-none-any.whl size=17397 sha256=9d5f84a1033868962a3d7071fa75d71c7af68178dd4d15528ae3c1cc90f59dc5\n",
            "  Stored in directory: /root/.cache/pip/wheels/c0/59/9f/7372f0cf70160fe61b528532e1a7c8498c4becd6bcffb022de\n",
            "Successfully built googletrans\n",
            "Installing collected packages: rfc3986, hyperframe, hpack, h11, chardet, idna, hstspreload, h2, httpcore, httpx, googletrans\n",
            "  Attempting uninstall: h11\n",
            "    Found existing installation: h11 0.14.0\n",
            "    Uninstalling h11-0.14.0:\n",
            "      Successfully uninstalled h11-0.14.0\n",
            "  Attempting uninstall: chardet\n",
            "    Found existing installation: chardet 5.2.0\n",
            "    Uninstalling chardet-5.2.0:\n",
            "      Successfully uninstalled chardet-5.2.0\n",
            "  Attempting uninstall: idna\n",
            "    Found existing installation: idna 3.10\n",
            "    Uninstalling idna-3.10:\n",
            "      Successfully uninstalled idna-3.10\n",
            "  Attempting uninstall: httpcore\n",
            "    Found existing installation: httpcore 1.0.6\n",
            "    Uninstalling httpcore-1.0.6:\n",
            "      Successfully uninstalled httpcore-1.0.6\n",
            "  Attempting uninstall: httpx\n",
            "    Found existing installation: httpx 0.27.2\n",
            "    Uninstalling httpx-0.27.2:\n",
            "      Successfully uninstalled httpx-0.27.2\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "langsmith 0.1.143 requires httpx<1,>=0.23.0, but you have httpx 0.13.3 which is incompatible.\n",
            "openai 1.54.4 requires httpx<1,>=0.23.0, but you have httpx 0.13.3 which is incompatible.\u001b[0m\u001b[31m\n",
            "\u001b[0mSuccessfully installed chardet-3.0.4 googletrans-4.0.0rc1 h11-0.9.0 h2-3.2.0 hpack-3.0.0 hstspreload-2024.11.1 httpcore-0.9.1 httpx-0.13.3 hyperframe-5.2.0 idna-2.10 rfc3986-1.5.0\n",
            "Texto Original: Olá, como você está?\n",
            "Texto Traduzido para Inglês: Hello, how are you?\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Define o texto que queremos traduzir\n",
        "texto_original = \"O livro está sobre a mesa!\"\n",
        "\n",
        "# Traduz o texto para o inglês\n",
        "texto_traduzido = translator.translate(texto_original, dest='en')\n",
        "\n",
        "# Imprime o texto traduzido\n",
        "print(\"Texto Original:\", texto_original)\n",
        "print(\"Texto Traduzido para Inglês:\", texto_traduzido.text)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PI9pXe0R6ju1",
        "outputId": "0d8c7465-9d34-4725-bd9a-ea7d400308c0"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Texto Original: O livro está sobre a mesa!\n",
            "Texto Traduzido para Inglês: The book is on the table!\n"
          ]
        }
      ]
    }
  ]
}