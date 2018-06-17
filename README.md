# 競技プログラミングのための標準入出力（Python）
[参考:Pythonで競技プログラミングする時に知っておきたいtips(入出力編)(Qiita)](https://qiita.com/lethe2211/items/6cbade2bc547649bc040#1%E8%A1%8C%E3%81%AB%E6%96%87%E5%AD%97%E5%88%971%E3%81%A4%E3%81%AE%E5%85%A5%E5%8A%9B)

## 入力
### 1行に1つの文字列の入力
~~~
str_val = input()
~~~

### 1行に1つの整数の入力
~~~
int_val = int(input())
~~~

### 1行にスペース区切りで複数の文字列の入力
~~~
str_list = input().split()
~~~

### 1行にスペース区切りで複数の整数の入力
~~~
int_list = list(map(int, input().split()))
~~~

## 出力
### 1変数を出力(改行なし)
~~~
print(A)
~~~

### 複数変数をスペース区切りで出力
~~~
print(A, B, C)
~~~
または、リスト内の要素をスペース区切りで出力する場合
~~~
print(*A)
~~~

### 複数変数をカンマ区切りで出力
~~~
print(','.join([A, B, C]))
~~~

[Markdown記法チートシート](https://qiita.com/Qiita/items/c686397e4a0f4f11683d)
