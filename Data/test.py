from snownlp import SnowNLP
import csv

with open('C:\Works\playground\Data\sample.csv', 'r', encoding='utf', errors='replace') as sample:
    lines = csv.reader(sample)
    # print(lines)
    for line in lines:
        line_id, line_title, line_text, line_mark = line
        # predict the sentiment of text
        snow_text = SnowNLP(line_text)
        sentiment = snow_text.sentiments
        summary = snow_text.summary(5)
        print("{0} {1} {2} {3}".format(line[0], summary, sentiment, line_mark))
