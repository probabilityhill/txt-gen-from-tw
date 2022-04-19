import csv

CSV_PATH = "tweets.csv"
TXT_PATH = "tweets.txt"

tweets = []
with open(CSV_PATH, mode="r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if(row == []):
            continue
        tweets.append([row[1] + "<|endoftext|>"])

with open(TXT_PATH, mode="w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(tweets)
