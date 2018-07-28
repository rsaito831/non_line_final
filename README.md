# non-line_final

##  環境

- Python：3.6.5



## logistic

- logistic.py：ロジスティクス写像の計算．（一回実行すれば良い）

  ```
  $ python logistic.py
  -> log.csv（分岐図必要な結果）
  -> lyapunov_ex_log.csv（分岐点とリアプノフ指数の比較グラフに必要な結果）
  -> attractor.csv（アトラクタを作成する際に必要な結果）
  
  もし、再度実行する場合は，実行前にattractor.csvを消すこと
  $ rm attractor.csv
  ```



- func_cal.py：下記の式を計算

  $y=x　(1)式$

  $ax_k(1-x_k)　(2)$

  ```
  $ python func_cal.py [parameter a]
  -> func1.csv（1の結果 0<=x<=4）
  -> func2.csv（2の結果 0<=x<=4）
  
  ex.
  $ python func_cal.py 3.3
  ```



- extraction_a.py：attractor.csvからparameter aのときの結果を抽出

  ```
  $ python extraction_a.py [parameter a]
  -> extraction.csv
  
  ex.
  $ python python extraction_a.py 3.3
  ```

  

## delay_logistic

- logistic.py：遅延ロジスティクス写像の計算．（一回実行すれば良い）

  ```
  $ python logistic.py
  -> delay_log.csv（分岐図必要な結果）
  -> lambda1_log.csv, lambda2_log.csv（分岐点とリアプノフ指数の比較グラフに必要な結果）
  -> attractor.csv（アトラクタを作成する際に必要な結果）
  
  もし、再度実行する場合は，実行前にattractor.csvを消すこと
  $ rm attractor.csv
  ```



- extraction_b.py：attractor.csvからparameter bのときの結果を抽出

  ```
  $ python extraction_b.py [parameter b]
  -> extraction.csv
  
  ex.
  $ python python extraction_b.py 2.1
  ```



## logisticとdelay_logsticに共通すること

attractor.csvを消さいない限り，

func_cal.pyとextraction_(a)or(b).pyの引数さえ変えれば，他パラメータのときのアトラクターを観測できる．

- 