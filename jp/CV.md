# Keisuke Fujii

<img src='../figs/face_maldives.jpg' width=240pt>

[English version](../README.md)

### 現在の職
京都大学工学研究科
機械理工学専攻
助教  
博士（工学）（京都大学）

<!-- TODO translate in JP -->
[**経歴の詳細**](../work_education.md)

### 住所
615-8540  
京都市西京区 京都大学桂 C3棟b4N02室

### 電話番号
075-383-3647

### 研究の概要

大型科学研究（ビッグサイエンス）、特にプラズマ核融合研究に対する
機械学習やベイズ推定の手法開発に興味を持って研究を進めています。

私はこれまで、核融合プラズマ研究に関する計測機器開発研究に取り組んできました。
そのこともあり、現在進めているプロジェクトの一つは、科学計測の精度向上です。
一般的に計測データは複雑な性質のノイズを含んでいますが、
それを機械学習やベイズ統計を用いて推定・補正する方法を開発しました。

機械学習に関する初めての論文は
[K. Fujii 2017 RSI](http://aip.scitation.org/doi/full/10.1063/1.4974344)
[arXiv](https://arxiv.org/abs/1607.05380)に掲載されました。
この論文では、
+ ガウス過程回帰を用いて、多チャンネル計測システムの感度較正誤差を推定する手法の開発
+ その誤差を補正し、より高精度の電子密度分布を得る手法の開発  

を行いました。


### これまでの研究内容
現在の研究内容に取り組む前は、核融合プラズマ研究の分光計測に貢献してきました。  
主な成果としては、
+ 超高温プラズマ中の水素原子Balmer線スペクトルが、
ガウス関数で表すことのできない大きな裾形状を有することを発見した  
[K.Fujii 2011 NIMA]
+ 上記スペクトル裾が、これまで存在しないと考えられてきた超高温部に侵入し、
数keVにまで加熱された超高温の水素原子からの発光であることを実証した
[K.Fujii 2013 Phys. Plasmas]
+ 上記スペクトル裾を10^6のダイナミックレンジで計測できる新たな分光計測手法を開発した
[K.Fujii 2013 Rev. Sci. Instrum]
+ 高精度に計測したスペクトル裾から、超高温プラズマ中に侵入した中性水素原子密度を計測する
手法を世界で初めて開発した
[K.Fujii 2014 Nucl. Fusion]

ことです。

### 最近の発表
Bayesian Inference for the LHD Experiment Data  
*IAEA Technical Meeting on Uncertainty Assessment and Benchmark Experiments for Atomic and Molecular Data for Fusion Applications (19-21 December 2016, IAEA Headquarters, Vienna, Austria)*

https://www-amdis.iaea.org/meetings/UQ2016/


[**国際会議発表のリスト**](talks.md)

[**国内会議発表のリスト**](https://kyouindb.iimc.kyoto-u.ac.jp/e/hR3uG)

### ソフトウェア

上記研究活動に用いるため、いくつかのソフトウェアを開発しています。
+ [**Henbun**](https://github.com/fujii-team/Henbun)  
Variational Bayesian inference for big data.

+ [**PyLHD**](https://github.com/fujii-team/PyLHD)  
A Python library for the LHD experiments
(this is currently closed-source software).

以下のオープンソースソフトウェアの開発にも一部貢献しました。
+ [**GPflow**](https://github.com/GPflow/GPflow)  
Gaussian processes in TensorFlow
