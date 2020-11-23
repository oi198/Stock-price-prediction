### ソニーの株価変動を予測してみた！

[google colabで開く](https://colab.research.google.com/drive/1PkRAXsBzbp4z9OTw9KnpAli7WlG19N_O?usp=sharing)

今回はRNNでおなじみのlstmを使って明日のソニーの終値を予測するモデルを作ってみました。
実装環境はgoogle colabを使いました。

`import pandas_datareader as web`<br>
`com = 6758 #ソニー銘柄コード`
`web.DataReader([str(com) + '.JP'], 'stooq')`<br>

上記のコードで銘柄コードに対する企業の過去5年間の終値、高値、安値、始値、出来高を取得できる。

![株価画像1](https://uploda1.ysklog.net/49edcf2db85d8fff471c2851a80ff6cb.png)
