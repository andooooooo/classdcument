import re
import math
import os
import sys

#英字以外除去
p2 = re.compile('[^a-zA-Z]')

#カテゴリごとに分けて、英字以外除去、タグ除去、小文字化しファイルに保存
def catpart(inputfile):
    co = 0
    ct = 0
    cth = 0
    cf = 0
    cfi = 0
    opo = 0
    #タグ除去
    stop = ["<DOCUMENT>", "<ID>", "</ID>", "<BODY>", "</DOCUMENT>", "<CAT>", "</CAT>"]
    with open(inputfile, 'r') as f:
        for line in f:
            cat = line[:-1]
            if cat in stop:
                continue
            elif opo == 2:
                if cat == "</BODY>":
                    opo = 0
                    continue
                cat = cat.lower()
                cat =  re.sub(p2,"",cat)
                with open("one.txt", "a") as fout:
                    fout.write(cat+"\n")
            elif opo == 3:
                if cat == "</BODY>":
                    opo = 0
                    continue
                cat = cat.lower()
                cat =  re.sub(p2,"",cat)
                if cat == "":
                    continue
                with open("two.txt", "a") as fout:
                    fout.write(cat+"\n")
            elif opo == 4:
                if cat == "</BODY>":
                    opo = 0
                    continue
                cat = cat.lower()
                cat =  re.sub(p2,"",cat)
                if cat == "":
                    continue
                with open("three.txt", "a") as fout:
                    fout.write(cat+"\n")
            elif opo == 5:
                if cat == "</BODY>":
                    opo = 0
                    continue
                cat = cat.lower()
                cat =  re.sub(p2,"",cat)
                if cat == "":
                    continue
                with open("four.txt", "a") as fout:
                    fout.write(cat+"\n")
            elif opo == 6:
                if cat == "</BODY>":
                    opo = 0
                    continue
                cat = cat.lower()
                cat =  re.sub(p2,"",cat)
                if cat == "":
                    continue
                with open("five.txt", "a") as fout:
                    fout.write(cat+"\n")
            else:
                if cat == "one":
                    co += 1
                    opo = 2
                elif cat == "two":
                    ct += 1
                    opo = 3
                elif cat == "three":
                    cth += 1
                    opo = 4
                elif cat == "four":
                    cf += 1
                    opo = 5
                elif cat == "five":
                    cfi += 1
                    opo = 6
    #全てのカテゴリ総数
    all = co+ct+cth+cf+cfi
    #各カテゴリの数と総数表示
    print("one: "+repr(co)+"\ntwo: "+repr(ct)+"\nthree: "+repr(cth)+"\nfour: "+repr(cf)+"\nfive: "+repr(cfi)+"\nall: "+repr(all))

if __name__ == '__main__':
    argvs = sys.argv
    if len(argvs) != 2:
        print("Usage: python3 report.py [input]")
        exit()
    catpart(argvs[1])
