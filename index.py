import MeCab
from Emotions import *

'''my = '名前'
name = input('あなたの名前を教えてください')
print('こんにちは' + name + 'さん、私は' + my + 'といいます。')

#一人称一覧
user_my = ['私','儂','僕','俺','わたくし']
#他にさすもの
this_word = ['それ','これ','あれ','どれ']'''

nol_word = []
adjective = []
non_adjective = []
split_word = []

'''mecab = MeCab.Tagger('-Ochasen')
word = mecab.parse('この色はきれいじゃないし、超絶おいしくない')
a = [line for line in word.splitlines() if '名詞' in line.split()[-1]]
for i in word.splitlines():
    split_word.append(i.split('\t'))

#print(split_word)
#形容詞の否定を何とかする

for i in split_word[:-1]:
    #if 'ない' in i[2]:
    #    print(i)
    if '名詞' in i[3]:
        nol_word.append(i[2])
    if '形容詞' in i[3]:
        adjective.append(i[2])

print('名詞')
print(nol_word)
print('形容詞')
print(adjective)'''

#main処理
#モデル読み込み
#model = gensim.models.KeyedVectors.load_word2vec_format('model.vec', binary=False)
#「非常にポジティブな単語」と「非常にネガティブな単語」を任意で指定
happy = ['喜び']
angle = ['怒り']
sad = ['悲しい']
joy = ['楽しい']

x = '面白い'
#setup = Emotion(happy, angle, sad, joy, model)
#a = setup.emotion_score(x)
#print(a)