import csv

coinList = open('./haveToProcess.csv', 'r', encoding='utf-8')
ss = open('./onlyURL.csv', 'w', encoding='utf-8', newline="")
wr = csv.writer(ss)

coins = csv.reader(coinList)

for coin in coins:
    flag=0
    url = coin[2]
    url = url[2:]
    url = url[:-2]
    wr.writerow([coin[0],coin[1],url])
