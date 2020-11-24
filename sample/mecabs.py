import MeCab
mecab = MeCab.Tagger('-Ochasen')
print(mecab.parse('このソフトクリームとってもおいしくない'))

#mecabrc:(引数なし)
#-Ochasen: (ChaSen 互換形式)
#-Owakati: (分かち書きのみを出力)
#-Oyomi: (読みのみを出力)