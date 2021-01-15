# ソニーの株価変動を予測してみた！

[google colabで開く](https://colab.research.google.com/drive/1PkRAXsBzbp4z9OTw9KnpAli7WlG19N_O?usp=sharing)

今回はRNNでおなじみのLSTMを使って明日のソニーの終値を予測するモデルを作ってみました。<br>
実装環境はgoogle colabを使いました。

<br>

#### 株価データを取得する

```
import pandas_datareader as web
com = 6758 #ソニー銘柄コード
web.DataReader([str(com) + '.JP'], 'stooq')
```

上記のコードで銘柄コードに対する企業の過去5年間の終値、高値、安値、始値、出来高を取得できます。<br>
<br>

<img src="https://user-images.githubusercontent.com/67414951/102814016-39ce0a00-440d-11eb-9cfd-07514ef0d583.PNG" width="300px">
<図1 : ソニーの過去5年間の株価データ><br>
<br>
<br>

<img src="https://user-images.githubusercontent.com/67414951/102814018-39ce0a00-440d-11eb-9df8-f2bb466c5d18.PNG" width="300px">
<図2 : ソニーの過去5年間の終値の変動><br>


#### データ処理

株価データの内、直近228日分の終値をテスト用データ、それ以前の912日分の終値を訓練用データにしました。<br>
<br>

#### LSTMモデルを作成・学習させる

以下のようなモデルを作成<br>

```
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], x_train.shape[2])))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(120))
model.add(Dense(1))
model.compile(
    optimizer='adam',
    loss='mean_squared_error')
model.summary()
```
<図3 : モデル作成コード><br>

<img src="https://user-images.githubusercontent.com/67414951/102813956-1e62ff00-440d-11eb-9ff5-37843dd25575.PNG" width="300px">
<図4 : モデルの詳細><br>
<br>

最適化アルゴリズムにはAdam、<br>
モデル評価のための損失関数は平均二乗誤差(MSE)を設定しました。<br>
<br>

#### 結果

予測結果と実際の値を比較<br>
<img src="https://user-images.githubusercontent.com/67414951/102814013-389cdd00-440d-11eb-8b14-38b7f3f5bd40.PNG" width="500px"><br>
<図5 : 予測結果の変動と実際の変動の様子><br>
<br>

ぱっと見高精度な予測ができているように見えます。<br>
しかし現実は甘くなく、グラフをよく見ると予測値は前日の変動をなぞっているだけでした。
<br>

#### 結論

やはり終値というデータだけを学習に使ったり、実際の終値と予測した終値の平均二乗誤差を最小にするような学習をさせるだけでは、未来を予測することはできないことが分かりました。<br>
今後は別のアプローチを考えていきたいと思います！<br>
以上です。
