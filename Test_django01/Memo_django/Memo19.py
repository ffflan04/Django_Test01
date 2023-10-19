# *args, **kwargs の使い方
# 引数の位置と、対応関係は考える必要があります。
# *args, **kwargs 引数の指定は、強制ではありません。
# *args は、複数の引数をタプル型で受け取る。
# *argsは受け取る引数を指定できる。
# **kwargs は、複数の引数を辞書型で受け取る。
# **kwargs は、引数の最後に指定するべきです。
# what=any この形は、key=valueの引数って考えてOKです。

def mysum(*args, hoge, hoge01): # 受け取る引数をそれぞれ指定できる。
    print(args)
    print(hoge)
    print(hoge01)

mysum(2,3,4,5,hoge=100, hoge01='トマト') 


def mysum01(args1, *, args2): # 引数の指定を強制する。
    print(args1)
    print(args2)

mysum01('坂道', args2='星が綺麗に見える') # *の後に続く引数は、必ず指定をする必要がある。


def mysum02(*args, **kwargs): # このように設定すれば、ほぼ全ての引数を受け取れる。
    print(args) # 数値も、文字列も引数として、混合して受け取れます。
    print(kwargs) # 複数の辞書型の引数を受け取れますね。

mysum02(1,2,3,'あの時の笑顔はなんだったん', kagi='りんご', kagi01='アップル') 


def test(): # 辞書の使い方の確認。
    context = {}
    context['try'] = '目を細めて'
    context['try01'] = 'この歌何度も歌うよ'
    print(context)
    print(context['try'])


def test01(*args): # *argsの運用方法、タプルをアンパックしただけじゃ。
    a, b, c = args
    print(a)
    print(b)
    print(c)

test01(12, 32, '抱えてる思いを')


def test02(args01, args02, **kwargs): # **kwargsは最後の引数に指定しなければなりません。
    print(args01)
    print(args02)
    print(kwargs)

# キーワード引数の対応させる位置は気を使う必要があります。
test02(try00=12, try01=13, args01='ねぇ', args02='あなたの心臓を')


def test03(request, *args, **kwargs): # *args, **kwargs の引数の取得は、強制ではない。
    print('hello world')

test03('アッカーマン')


def test04(*args, **kwargs): # **kwargsの引数の指定は、代入と似ているのだ。
    print(kwargs['mata'])
    

yattana='やったな'
test04('合言葉', mata=yattana) # what=any この形は、key=valueの引数って考えてOKです。



