import re
import math
import os
import multiprocessing as mp
import sys

p2 = re.compile('[^a-zA-Z/<>]')
#p(category)訓練データのカテゴリの出現確率
orate =76/300
trate =64/300
thrate =64/300
frate =51/300
firate =45/300
no=0
ol = []
tl = []
thl = []
fl = []
fil = []

#テストデータを成形
def textpro(text):
    #テストデータから除去する記号
    stop = ["<DOCUMENT>", "<ID>", "</ID>", "<BODY>","</BODY>", "<CAT>", "</CAT>"]
    po = 0
    num = []
    #テストデータのID番号格納と記号除去
    with open(text, 'r') as f:
        for line in f:
            cat = line[:-1]
            #ID格納
            if po == 1:
                num.append(cat)
                po = 0
                continue
            if cat == "<ID>":
                po = 1
                continue
            #記号除去
            if cat in stop:
                continue
            cat = re.sub(p2,"",cat)
            if cat == "":
                continue
            cat = cat.lower()
            with open("karitest.txt", "a") as fout:
                fout.write(cat+"\n")
    return num

#ナイーブベイズ計算
def culcat(input,rate,listname):
    count = 0
    couadd = 0
    allword = 0
    lista = []
    #カテゴリ内の全単語数を計算
    allword = sum(1 for line in open(input))
    with open("karitest.txt", 'r') as fo:
        for line in fo:
            count = 0
            doc = line[:-1]
            #ドキュメントがカテゴリに属する確率を保存
            if doc == "</document>":
                result = math.log(rate) + couadd
                listname.append(result)
                couadd = 0
                continue
            else:
                #単語が訓練データに何回出現するかカウント
                with open(input, 'r') as f:
                    for line in f:
                        cat = line[:-1]
                        if cat ==doc:
                            count += 1
                            continue
                        else:
                            continue
                #P(document|category)を計算
                x = count/allword
                if x == 0:
                    #スムージング
                    x = 1/25000
                    couadd += math.log(x)
                else:
                    couadd += math.log(x)
    return listname

def writefile(resnum,correct):
    with open("result.txt", "a") as fou:
        fou.write(resnum + " " + correct+"\n")

if __name__ == '__main__':
    argvs = sys.argv
    if len(argvs) != 2:
        print("Usage: python3 report.py [input]")
        exit()
    nums = textpro(argvs[1])
    #並列処理するために５つのプロセスを作成
    pool = mp.Pool(5)
    #カテゴリごとに分けたテキストファイルを並列にナイーブベイズで計算する
    callback = pool.starmap(culcat,[("one.txt",orate,ol),("two.txt",trate,tl),("three.txt",thrate,thl),("four.txt",frate,fl),("five.txt",firate,fil)])
    #テストデータのID順に並んだ各データとカテゴリ(o,t,th,f,fi)の条件付き確率
    o = callback[0]
    t = callback[1]
    th = callback[2]
    f = callback[3]
    fi = callback[4]
    #確率が一番大きいカテゴリをIDと共にファイルに書き込む
    while no < len(w):
        maxa = max(w[no],c[no],g[no],n[no],o[no])
        if maxa == w[no]:
            writefile(nums[no],"one")
        if maxa == c[no]:
            writefile(nums[no],"two")
        if maxa == g[no]:
            writefile(nums[no],"three")
        if maxa == n[no]:
            writefile(nums[no],"four")
        if maxa == o[no]:
            writefile(nums[no],"five")
        no += 1
