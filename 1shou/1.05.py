s=input().split() #sは各単語をリスト化した配列

moji="".join(s) #文章を１つなぎの文字列にする
a=[]
for i in range(len(moji)-1):
    a.append(moji[i:i+2])
print(a)

tango=["".join(s[i]+s[i+1]) for i in range(len(s)-1)] #sの隣り合った単語をjoinして単語bi-gramを作成
print(tango)
