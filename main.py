import time as t

print("bilgi yarışmasına hoş geldiniz!!1!11!","\n",50*"*")
t.sleep(2)
print("her soru 3 puan ve her yanlış soru -2 puandır")
t.sleep(1)
print("lütfen cevap olarak sadece şıkkı yazınız","soruları boş bırakmayınız")
t.sleep(1)
print("hadi başlayalım","(çıkış yapmak için q giriniz)")


sorular_ve_cvplar = [["kaç tane canlı alemi bulunmaktadır?","a)3 b)4 c)5 d)6  "],
           ["istkilal marşının kabulunun tarihi kaçtır?","a)14 şubat 1925 b)30 haziran 1922 c)12 mart 1921 d)8 aralık 1919  "],
           ["şu dünyadaki en zengin kişi?","a)acıya gülendir b)insafa gelendir c)sevmeyi bilendir d)gönül fethedendir  "],
           ["islamın kaç şartı vardır?","a)12 b)52 c)79 d)5  "],
           ["periyodik tabloda 105. element hangisidir?","a)vanadyum b)dubniyum c)toryum d)protaktinyum  "],
           ["bir nanometre kaç ångströmdür?","a)10 b)100 c)1000 d)10000  "],
           ["yanalalz nasıl yazılır?","a)yalnız b)yanlız c)yalnış d)yanlış  "]]

dogrular = ["d","c","d","d","b","a","a"]

girintiler = []

puan = 0

for i in range(0,7):
    print(sorular_ve_cvplar[i][0])
    cvp=input(sorular_ve_cvplar[i][1])
    if cvp.lower()=="q":
        print("çıkış yapılıyor")
        t.sleep(0.2)
        break
    else:
        girintiler.append(cvp)

print("puanınız hesaplanıyor",end="")
for i in range(0,5):
    t.sleep(0.2)
    print(".",end="")

for i in range(0,7):
    if girintiler[i]==dogrular[i]:
        puan += 3
    else:
        puan -=2

t.sleep(0.5)
print("\nsınavınz bitmiştir","\nPuanınız: ",puan,sep="")





