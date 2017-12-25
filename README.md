# Sentiment-Plot
Plots the polarity of the contents of multiple text files in a directory

The program takes advantage of the TextBlob API, a simple API for natural language processing. It is said to "stand on the shoulders of NLTK and pattern." The documentation can be found here: https://textblob.readthedocs.io/en/latest/

Instructions:

Ensure proper installation of required libraries

matplotlib - https://matplotlib.org/faq/installing_faq.html

natsort - https://pypi.python.org/pypi/natsort

TextBlob - http://textblob.readthedocs.io/en/dev/install.html

Users then place the plot_sentiment.py file in a directory with multiple text files.

[![input.jpg](https://s14.postimg.org/y1reu6iz5/input.jpg)](https://postimg.org/image/oh7s7atn1/)

After running plot_sentiment.py, the resulting plot will show the polarity of the words of each file.

[![figure_2.png](https://s14.postimg.org/v7o9grjdt/figure_2.png)](https://postimg.org/image/ejwre9om5/)

The blue dots illustrate the polarity of individual lines from a given file. The black dots show the total polarity of the lines in that file. The polarity of an individual line is a float within the range [-1.0, 1.0]. Summing these lines gives a good idea of the sentiment of a file.

The helper file clean_files.py creates copies of all files in a directory without characters that the TextBlob libary finds invalid. Useful for automating the cleaning of large amounts of data scraped from the internet before running the plot_sentiment.py file.

The test_txt folder has example text to test the program. It also shows the benefit of naturally sorting the titles of the text files for a chronological sentiment analysis.
