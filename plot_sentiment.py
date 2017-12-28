# solvedem

from textblob import TextBlob
import matplotlib.pyplot as plt
import os
from natsort import natsorted

# Returns the polarity and average subjectivty of a file
def file_sentiment(filename, count_):
    file = open(filename, "r")
    num_lines = float(sum(1 for line in file))
    file.close()
    file = open(filename, "r")
    total_polarity, total_subjectivity, line_count, tried_line_count = 0., 0., 0., 0.
    for line in file:
        analysis = TextBlob(line)
        try:
            current_polarity, current_subjectivity = analysis.sentiment[0], analysis.sentiment[1]
            total_polarity += current_polarity
            total_subjectivity += current_subjectivity
            if current_polarity != 0.00:
                plt.plot([count_ + (tried_line_count / num_lines)], [current_polarity], marker='o', markersize=2, color="cyan")
                line_count += 1
            tried_line_count += 1
        except UnicodeDecodeError:
            print "Unreadable line: ", line
        
    return total_polarity / line_count, total_subjectivity / line_count

# Retrieves, sorts, and returns
# all valid txt files in directory
def get_txt_files():
    files = []
    for fn in os.listdir("."):
        if os.path.isfile(fn):
            if str(fn).endswith(".txt"):
                files.append(fn)
    return natsorted(files)

# Compute sentiment analysis on all files in directory
# Return list of results
# Puts title text on plot
def multiple_file_analysis():
    results = []
    count = 0
    for file_ in get_txt_files():
        fs = file_sentiment(file_, count)
        plt.text(count, fs[0], str(file_)[:-4], fontsize = 8)
        results.append(fs[0])
        count += 1
    return results
    
def plot_results(results):
    plt.style.use('seaborn-deep')
    plt.scatter(range(len(results)), results, color='k', s=50, marker="o")
    plt.title('Sentiment Analysis')
    plt.ylabel('Polarity')
    plt.show()

plot_results(multiple_file_analysis())


