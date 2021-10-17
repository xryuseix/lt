---
theme: default
highlighter: shiki
title: 1日1コードのすゝめ - 111日間毎日プログラムを書く方法と結果
colorSchema: dark
download: true
---

<!-- @format -->

# <carbon-logo-github /> 1 日 1 コードのすゝめ

<div style="margin-left:5em">
111日間毎日プログラムを書く方法と結果
</div>
<div class="under-right">
  <a href="https://xryuseix.github.io/lt/github-111days">
    <img src="/qrcode.png" />
    https://xryuseix.github.io/lt/github-111days
  </a>
  <br />
<mdi-arrow-up-bold-outline />詳しく資料が見たい方はこちら！
</div>

<style>
  img {
    height: 10em;
  }
</style>

---

# 自己紹介

<div class="flex">
<div class="flex-grow">

## <img src="https://avatars.githubusercontent.com/u/51394682" height="1832" width="1832" style="height: 1.5em; width: auto; display: inline-block; border-radius: 100%" /> 石川琉聖

<br />

- 立命館大学 サイバーセキュリティ研究室 **3**回生
- paiza 学生スタッフ (2020/03~)
  - 問題集を作成しています
- アルゴリズムとセキュリティに興味があります
  - SecHack365'20 研究駆動コース
  - Seccamp'19 暗号化通信ゼミ
  - AtCoder <span style="color:lightblue">**水色**</span> / CodeForces <span style="color:#6495ed">**青色**</span>
- Web サイト <mdi-arrow-right-bold-outline /> [https://xryuseix.github.io](https://xryuseix.github.io)
- アカウント <mdi-arrow-right-bold-outline /> <span class="text-twitter">[<carbon-logo-twitter />@ryusei_ishika](https://twitter.com/ryusei_ishika)</span> / [<carbon-logo-github /> xryuseix](https://github.com/xryuseix)
  - ID はだいたい **xryuseix** です

</div>

<div class="flex-grow">

<div class="qrcode under-right">
  <a href="https://xryuseix.github.io/lt/github-111days">
    <img src="/qrcode.png" />
  </a>
</div>

<style>
  .qrcode img {
    height: 7em;
  }
</style>

## 好きな ○○

<br />

- 言語 <mdi-arrow-right-bold-outline /> <logos-c-plusplus /> C++, <logos-rust style="background:white"/> Rust, <carbon-logo-python /> Python
  <img src="https://camo.githubusercontent.com/37eb24996c3cae0fe6b7b804e6bcb32f2141e5bdffbdeecaf046ff64244fc5a9/68747470733a2f2f6769746875622d726561646d652d73746174732e76657263656c2e6170702f6170692f746f702d6c616e67733f757365726e616d653d7872797573656978266c61796f75743d636f6d70616374266c616e67735f636f756e743d3130266578636c7564655f7265706f3d53412d506c61672c4174436f6465725f4261636b75702c5365634861636b3336352d446174617365742c26686964653d68746d6c2c4d616b6566696c652c6373732c5465782c434d616b652c534353532c43267468656d653d746f6b796f6e69676874" style="height:10em" />
- エディタ <mdi-arrow-right-bold-outline /> <vscode-icons-file-type-vscode /> VSCode
- OS <mdi-arrow-right-bold-outline /> <mdi-apple /> macOS (M1)
- データ構造 <mdi-arrow-right-bold-outline /> <carbon-decision-tree /> Segment Tree
- キーボード <mdi-arrow-right-bold-outline /> <carbon-keyboard /> REALFORCE

</div>
</div>

---

# 今回話すこと

<div class="flex">

<div class="flex-grow">
<br />

<carbon-logo-github /> GitHub で 111 日間コードを書き続けました．  
そこで...

1. 111 日間でできた成果物
2. 毎日プログラムを書き続けるコツ
3. 習慣化
</div>
<div class="flex-grow">
  <div class="image grass">
    <img src="/github_grass.png"/>
  </div>
  <div class="image">
    <img src="/github_streak.png" />
  </div>
</div>
</div>

<style>
.image {
  margin-bottom:20px;
}
img {
  height: 170px;
}
</style>

---

# (1) 111 日間でできた成果物 - 一覧

- 自分のポートフォリオサイトの機能開発とリファクタリング (<logos-javascript /> <logos-react /> <logos-gatsby /> <logos-vue />)
- 競プロ用ストレステストツール (<logos-rust style="background:white"/>)
- フィッシングサイト判定 chrome 拡張 (<carbon-logo-python /> <logos-javascript />)
- 自宅用監視カメラ (<carbon-logo-python /> <logos-opencv />)
- 仕事用業務効率化ツール  (<logos-rust style="background:white"/>)
- 文章構成ツール (<carbon-logo-python />)
- Spotify cli ツール (<carbon-logo-python />)
- 暗号化ツール (<logos-rust style="background:white"/>)
- zoom のバーチャル背景を剥がすツール (<logos-c-plusplus /> <carbon-logo-python /> <logos-opencv />)
- ReDoS やられサイト(CTF 用) (<carbon-logo-python /> <logos-flask style="background:white" />)
- その他，<b>複数のレポジトリの</b>リファクタリングとドキュメント作成
- ...

<div>とにかくいっぱいできました！！！！</div>

<style>
div {
  text-align:center;
  font-size:2.5em;
  font-weight: bold;
}
</style>

---

# (1) 111 日間でできた成果物 - 紹介 1

## ポートフォリオサイト (<logos-javascript /> <logos-react /> <logos-gatsby /> <logos-vue />)

<div style="height: 60%">
  <a href="https://xryuseix.github.io/">
    <img src="/toppage.png" style="height: 100%; display: block; margin: auto;"/>
  </a>
</div>

- 自分の成果物・実績などを紹介するときのサイト
- インターンのとき実績欄に URL 貼るだけで便利だった
- Markdown スライドを SPA で表示・PDF スライドを専用 viewer で表示する機能などもある

<div class="under-right">
  https://xryuseix.github.io/
</div>
---

# (1) 111 日間でできた成果物 - 紹介 2

<div class="flex">
  <div class="flex-grow">
    <h2>ProofLeader (<carbon-logo-python />)</h2>
    <br />
    <ul>
      <li>文章の校正 (Formatter) を行う</li>
      <li>競プロ問題作成において共通して使用可能</li>
      <li>定期的に"フォーマット状態"の仕様が変わってる</li>
      <li><s>既知のバグがめっちゃある</s></li>
      <li>↑最近結構治った</li>
    </ul>
  </div>
  <div class="flex-grow" style="width: 45%; margin-right: 40px;">
    <a href="https://github.com/xryuseix/ProofLeader">
      <img src="/proofleader.png" style="height: 100%; display: block; margin: auto;"/>
    </a>
  </div>
</div>

<div class="under-left">
  <a href="https://github.com/xryuseix/ProofLeader">
    https://github.com/xryuseix/ProofLeader
  </a>
</div>

---

# (2) 毎日プログラムを書き続けるコツ

<div class="center-text">
  意外と特定の作業を毎日続けるのは難しい
  <p class="h3">自分の <b>趣味</b> を想像してみてください</p>
  <p class="h3">自分の <b>仕事</b> を想像してみてください</p>
  <p class="h4">他にも普段の生活 (1日3食，早寝早起き，薬，料理) など</p>
</div>

<div class="comment">
  競プロerは streak 続いてる人多いけど，あれは競プロer の頭がバグってるだけだからな
</div>

<style>
.h3 {
  font-size: 0.6em;
}
.h4 {
  font-size: 0.5em;
}
</style>

---

# (2) 毎日プログラムを書き続けるコツ

<div class="center-text2">
  続けるのに必要な条件は三つ
</div>

<div class="flex">
  <div class="flex-grow">
    ①
  </div>
  <div class="flex-grow">
    ②
  </div>
  <div class="flex-grow">
    ③
  </div>
</div>

<style>
.flex-grow {
  text-align: center;
  font-size: 10em;
  margin: 20px;
}
.flex {
  position: absolute;
  bottom: 80px;
  left: 50%;
  transform: translate(-50%, -50%);
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
}
.center-text2 {
  width: 90%;
  text-align: center;
  font-size: 2.2em;
  line-height: 1.5em;
  position: absolute;
  top: 35%;
  left: 50%;
  transform: translateY(-50%) translateX(-50%);
}
</style>

---

# (2) 毎日プログラムを書き続けるコツ

<div class="center-text2">
  続けるのに必要な条件は三つ
</div>

<div class="flex">
  <div class="flex-grow">
    友情
  </div>
  <div class="flex-grow">
    努力
  </div>
  <div class="flex-grow">
    勝利
  </div>
</div>

<v-click>
  <div class="batu">
    ❌
  </div>
  <div class="comic blur">
    <img src="https://images-fe.ssl-images-amazon.com/images/I/6102HGQDRWL._SY291_BO1,204,203,200_QL40_ML2_.jpg" />
  </div>
</v-click>

<style>
.flex-grow {
  text-align: center;
  font-size: 4em;
  margin: 20px;
  line-height: normal;
}
.flex {
  position: absolute;
  bottom: -100px;
  left: 50%;
  transform: translate(-50%, -50%);
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
}
.center-text2 {
  width: 90%;
  text-align: center;
  font-size: 2.2em;
  line-height: 1.5em;
  position: absolute;
  top: 35%;
  left: 50%;
  transform: translateY(-50%) translateX(-50%);
}
.batu {
  font-size: 16em;
  position: absolute;
  left: 50%;
  transform: translateY(-50%) translateX(-50%);
  top: 73%;
}
.comic {
  position: absolute;
  right: 1%;
  bottom: 1%;
}
.blur {
  -ms-filter: blur(5px);
  filter: blur(5px);
}
</style>

---

# (2) 毎日プログラムを書き続けるコツ

<div class="center-text2">
  続けるのに必要な条件は三つ
</div>

<div class="flex">
  <div class="flex-grow motibe">
    モチベ
  </div>
  <div class="flex-grow">
    根性
  </div>
  <div class="flex-grow">
    計画
  </div>
</div>

<style>
.flex-grow {
  text-align: center;
  font-size: 4em;
  margin: 20px;
  line-height: normal;
}
.motibe {
  writing-mode: vertical-lr;
  font-size: 3.8em;
}
.flex {
  position: absolute;
  bottom: -100px;
  left: 50%;
  transform: translate(-50%, -50%);
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
}
.center-text2 {
  width: 90%;
  text-align: center;
  font-size: 2.2em;
  line-height: 1.5em;
  position: absolute;
  top: 35%;
  left: 50%;
  transform: translateY(-50%) translateX(-50%);
}
</style>

---

# (2) 毎日プログラムを書き続けるコツ - モチベ

<div class="center-text">
  Twitterとかで頑張ってる人を見て<br />
  影響されましょう(?)
</div>

<div class="comment">
  iPhone 版 GitHub アプリのコントリビューショングラフとか便利です．スマホで草をウィジェットとしてみれます．
</div>

---

# (2) 毎日プログラムを書き続けるコツ - 根性

<div class="center-text">
  いっぱい頑張りましょう(?)
</div>

---

# (2) 毎日プログラムを書き続けるコツ - 計画

## よくある一日のスケジュール

<br />

| 時間             | 内容                                                              |
| :--------------- | :---------------------------------------------------------------- |
| 10:00 ごろ       | 起床                                                              |
| 10:00~15:00 ごろ | 大学 (ここで今夜の実装内容を考えとく)                             |
| ~18:00           | サークル・課題など                                                |
| ~24:00           | 実装のための勉強<small>(\*1)</small>・趣味など                    |
| 24:00~2:00       | <span class="big">今日のプログラミング<small>(\*2)</small></span> |

<br />

<v-click>
<div class="kome center">
  <ol>
    <li>知識を増やさず新しいコードは書けない</li>
    <li>今日の commit は昨日やっておく</li>
  </ol>
</div>
</v-click>

<style>
.kome {
  font-size: 2em;
}
.big {
  font-size: 1.4em;
}
</style>

---

# (3) 習慣化

## 成果物以外に得られたこと

<div class="center-text">
  習慣
</div>

<style>
.center-text {
  font-size: 9em;
}
</style>

---

# (3) 習慣化

## 習慣化をしよう

<div class="center-text">
  100 日の作業の成果 ≠ 100 日<b>連続の</b>作業の成果
</div>

---

# (3) 習慣化

## 習慣化をしよう

<div class="center-text">
  昨日やる気になれたことは<br />
  今日もやる気になりやすい
</div>

---

# (3) 習慣化

## 習慣化をしよう

<div class="center-text">
  習慣化こそが上達への近道
</div>

<style>
.center-text {
  font-size: 4em;
}
</style>

---

# (3) 習慣化

## 習慣化するためのコツ

<div class="center-text">
  目標の設定と記録
</div>

<style>
.center-text {
  font-size: 4em;
}
</style>

---

# (3) 習慣化

## 目標の設定

<div class="center center-text">
  <img src="https://www.kaonavi.jp/dictionary/wp-content/uploads/2019/02/mandarart_img02.jpg" /><br />
  <span>目標設定が難しいとき「マンダラート」</span>
</div>

<div class="comment">
  <a href="https://www.kaonavi.jp/dictionary/mandalart/">
    https://www.kaonavi.jp/dictionary/mandalart/
  </a>
</div>

<style>
.center-text {
  font-size: 2em;
}
img {
  height: 340px;
  display: block;
  margin: auto;
  padding: 40px 0 0 0;
}
</style>

---

# (3) 習慣化

## 記録

<div class="flex">

<div class="flex-grow">
<br />

GitHub や OSS で自分の成果を記録する

</div>
<div class="flex-grow">
  <div class="image grass">
    <img src="/github_grass.png"/>
  </div>
  <div class="image">
    <img src="/github_streak.png" />
  </div>
</div>
</div>

---

# (3) 習慣化

## 記録

<div class="center">
  <a href="https://github-readme-streak-stats.herokuapp.com/demo/">
    <img src="/readme_stats.png"/>
  </a>
</div>

<div class="comment">
  <a href="https://github-readme-streak-stats.herokuapp.com/demo/">
  https://github-readme-streak-stats.herokuapp.com/demo/
  </a>
</div>

<style>
img {
  height: 370px;
  display: block;
  margin: auto;
}
</style>

---

# まとめ

<div class="center-text">
  プログラミングを習慣化することが上達への近道<br />
  <mdi-arrow-right-bold-outline />「モチベ・根性・計画」が必要<br />
  目標は正しく設定して，成果は記録する
</div>

<div class="comment">
This slide was created by Slidev
</div>

<div class="under-right">
Thank you for listening!
</div>