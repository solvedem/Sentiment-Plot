# Sentiment-Plot
Plots the polarity of the contents of multiple text files in a directory

The program takes advantage of the TextBlob API, a simple API for natural language processing. It is said to "stand on the shoulders of NLTK and pattern." The documentation can be found here: https://textblob.readthedocs.io/en/latest/

Instructions:

Ensure proper installation of required libraries

matplotlib - https://matplotlib.org/faq/installing_faq.html

natsort - https://pypi.python.org/pypi/natsort

TextBlob - http://textblob.readthedocs.io/en/dev/install.html

Place the plot_sentiment.py file in a directory with multiple text files.

[![input.jpg](https://s14.postimg.org/y1reu6iz5/input.jpg)](https://postimg.org/image/oh7s7atn1/)

Run plot_sentiment.py.

[![sent1.png](https://s17.postimg.org/o3f53zvsv/sent1.png)](https://postimg.org/image/dglbyknnf/)

Blue dots illustrate the polarity of individual lines from a given file. Black dots illustrate the polarity of the entire file. The polarity of an individual line is a float within the range [-1.0, 1.0]. 

The helper file clean_files.py creates copies of all files in a directory without characters that the TextBlob libary finds invalid. Useful for automating the cleaning data before running the plot_sentiment.py file.

The test_txt folder has example text to test the program. The text files are handled in a naturally sorted order.
