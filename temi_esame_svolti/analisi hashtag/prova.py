#def leggi_hashtags(nome_file):
record_hashtags = {}
with open("hashtags.csv", "r", encoding="utf-8") as f:
    for riga in f:
        campi = riga.rstrip("\n").split(" ")
        if campi[0] not in record_hashtags:
            record_hashtags[campi[0]] = campi[2:]
        else:
            record_hashtags[campi[0]].extend(campi[2:])

hashtags_per_day = {}
for data, hashtags in record_hashtags.items():
    hashtag_counts = {}
    for hashtag in hashtags:
        if hashtag in hashtag_counts:
            hashtag_counts[hashtag] += 1
        else:
            hashtag_counts[hashtag] = 1
    hashtags_per_day[data] = hashtag_counts



