# PRMLのざっくりまとめ

## 1章
１章の内容まとめスライド  
https://www.slideshare.net/takushimiki/prml-52113785  
機械学習全般の教師あり、教師なし、強化学習の大きな枠についての説明。  

### 1-1
簡単なsin(x)から生成したノイズいりの人工データから曲線フィッティングによる回帰を行う。  
観測データにはノイズが乗っており、与えられたxに対する目的変数tの値には不確実性がある。  
確率論は、不確実性を厳密に定量的に表現する。  
基底関数を多項式とする線形回帰を考える。  
線形モデルの係数値は予測値と目的変数の差を表す誤差関数（損失関数と同義？）を最小化して達成できる。  
単純で、1番使われている誤差関数は二乗話誤差。  
平均二乗平方根誤差RMSEの利点はNで割ることでサイズの異なるデータ集合を比較できる。目的変数tと同じ尺度（単位）であることが保証されること。  
回帰モデルの多項式の次数を増やすと、次数の増加に伴い、係数の値が増大し、訓練データに適合しすぎてしまう。  
最小二乗でモデルのパラメータを求めるのは、最尤推定での特別な場合に相当する。  
→過学習が最尤推定の一般的な性質である。  
過学習の問題を避けるために、ベイズ的アプローチが有効。  
正則化の概念について説明。  
二次の正則化＝Ridge回帰＝ニューラルネットワークの文脈で荷重減衰  

### 1-2
確率論の基礎的な概念の解説。  
確率の同時分布の対称性と、情報定理からベイズの定理が導かれる。  
事前確率：観測するより前にわかっている確率  
事後確率：一度事象が確認されてからベイズの定理から求められる、推定した事象の確率  
今まで直感的に使ってきた確率はランダムな繰り返しの頻度とみなされる、古典的確率、頻度主義的な確率解釈。
ベイズの定理を機械学習に当てはめるとすると  
p（w|X） = p(X|w)p(w) / p(X)  
パラメータの事後確率　＝　モデル・パラメータの事前分布 / 規格化定数  
事象xを確認した後に、wに関する不確実性を事後分布の形で評価する。  
不確実性を定量的に表現し、新たなデータで修正していく方法をベイズ的な確率解釈は実現可能。  
p(X|w)を尤度といい,尤度を最大化させる方法を最尤推定法という。  
ベイズの定理は  
事後確率 ∝ 尤度 × 事前確率  
最尤推定の気持ちとしては、データを生成する確率を最大にするパラメータがいいパラメータだろうという考え。  
最尤推定の問題点  
・尤度p(X|w)は厳密には確率ではない  
・単純に尤度を最大化すると過学習しやすい  
・モデル選択が難しい場合が多い。   
ベイズ的なアプローチの利点は、事前知識を、事前確率として自然にモデルに入れることができる点。  
公平に見えるコインを３回投げて毎回表がでたとしても、表がでる確率を頻度主義的な考えだと１になるのを防ぐことができる。  
マルコフ連鎖モンテカルロ法MCMC法のようなサンプリング法の開発がベイズの定理を実用化させてきた。  

#### 1-2-4
ガウス分布の性質についての内容。  
ガウス分布は、平均と分散によって定められ、全領域で積分すると１になるため確率分布の用件を満たす。  
ガウス分布での最頻値と平均は一致する。  
同一の正規分布から独立にデータがN個生成された場合のデータ集合の確率（尤度）は、正規分布の積で表される。  
最尤推定で求めたパラメータの期待値はE=N-1/N σ^2で、バイアスのある推定量  
データ点の数が増えればバイアスの影響はなくなる。データ量が多い理由の一つ。  

#### 1-2-5
最尤法を用いて曲線フィッティングを行う。  
ノイズが正規分布から発生していると考えると、モデルは正規分布の形で書くことができる。p(t|x,w,β) = N(t|y(x,w), β^-1)  
ここから全てのデータからの尤度を求めて、最尤推定法によりパラメータを求める。  
データに基づいた事後確率を最大にするパラメータ推定法を最大事後確率（MAP）推定という。  

#### 1-2-6
完全なベイズアプローチではwのすべての値に関して積分する必要がある。  
予測分布はガウス分布の形で与えられる。  

### 1-3
モデルの性能評価をまとめた内容  
交差分割検証:訓練データをs分割、訓練時間はs倍。  
情報量規準：赤池情報量規準AIC、ベイズ情報量規準BICを用いる。  

### 1-4
データをます目に分割すると、入力変数が増加するとマス目の数が指数関数的に増大する。  
多項式曲線フィッティングを複数個の入力変数に拡張した場合、より高次の多項式が必要となり、係数の数はべき乗に増える。  
N次元の球の体積は表面に近い薄皮部分に集中するという、幾何的直感と一致しない  
大きい異次元空有間に伴う困難全般のことを次元の呪いとよぶ  
実用では目的変数の変化を生じさせる方向は限られているため、意外と高次元でもなんとかなる。

### 1-5
クラス分類や、回帰予測の値の決定はご識別率が最小になるように決定される。  
最大事後確率を
最大事後確率をもつクラスに決定される。






