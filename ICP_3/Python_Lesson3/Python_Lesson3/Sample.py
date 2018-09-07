import csv

with open("D:\\chumma\codon.tsv") as tsvfile1:
  reads = csv.reader(tsvfile1, delimiter='\t')
with open('reads', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    for rows in reader:
        k = rows[0]
        v = rows[1]
        mydict = {k:v for k, v in rows}
    print(mydict)
