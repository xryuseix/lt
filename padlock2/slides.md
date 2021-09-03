---
theme: default
highlighter: shiki
title: 南京錠の仕組みと開け方 - ピンタンブラー錠の仕組みと開け方を5分で紹介(KC3用)
colorSchema: dark
download: true
---

# <mdi-lock /> 南京錠の仕組みと開け方
<div style="margin-left:5em">
ピンタンブラー錠の仕組みと開け方を <b>超簡単に</b> 紹介
</div>
<div class="qrcode">
<mdi-arrow-down-bold-outline />詳しく資料が見たい方はこちら！
  <a href=https://xryuseix.github.io/lt/padlock>
    <img src="/qrcode.png" />
    https://xryuseix.github.io/lt/padlock
  </a>
</div>

<style>
  .qrcode {
    position: absolute;
    bottom: 2%;
    right: 1%;
    text-align: center;
  }
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

- 立命館大学 RiST/RiPPro所属 **3**回生
- アルゴリズムとセキュリティに興味があります
  - AtCoder <span style="color:lightblue">**水色**</span> / CodeForces <span style="color:#6495ed">**青色**</span>
  - Seccamp'19 暗号化通信ゼミ
  - SecHack365'20 研究駆動コース
- Webサイト <mdi-arrow-right-bold-outline /> [https://xryuseix.github.io](https://xryuseix.github.io)
- アカウント <mdi-arrow-right-bold-outline /> <span class="text-twitter">[<carbon-logo-twitter />@ryusei_ishika](https://twitter.com/ryusei_ishika)</span> / [<carbon-logo-github /> xryuseix](https://github.com/xryuseix)
  - IDはだいたい **xryuseix** です

</div>

<div class="flex-grow">

<div class="qrcode">
  <a href=https://xryuseix.github.io/lt/padlock>
    <img src="/qrcode.png" />
  </a>
</div>

<style>
  .qrcode {
    position: absolute;
    bottom: 2%;
    right: 1%;
  }
  .qrcode img {
    height: 7em;
  }
  .comment {
    position: absolute;
    bottom: 2%;
    left: 1%;
    font-size: 0.7em;
  }
</style>

## 好きな○○
<br />

- 言語 <mdi-arrow-right-bold-outline /> <logos-c-plusplus /> C++, <logos-rust style="background:white"/> Rust, <logos-python /> Python
<img src="https://camo.githubusercontent.com/37eb24996c3cae0fe6b7b804e6bcb32f2141e5bdffbdeecaf046ff64244fc5a9/68747470733a2f2f6769746875622d726561646d652d73746174732e76657263656c2e6170702f6170692f746f702d6c616e67733f757365726e616d653d7872797573656978266c61796f75743d636f6d70616374266c616e67735f636f756e743d3130266578636c7564655f7265706f3d53412d506c61672c4174436f6465725f4261636b75702c5365634861636b3336352d446174617365742c26686964653d68746d6c2c4d616b6566696c652c6373732c5465782c434d616b652c534353532c43267468656d653d746f6b796f6e69676874" style="height:10em" />
- エディタ <mdi-arrow-right-bold-outline /> <vscode-icons-file-type-vscode /> VSCode
- OS <mdi-arrow-right-bold-outline /> <mdi-apple /> macOS (M1)
- データ構造 <mdi-arrow-right-bold-outline /> <carbon-decision-tree /> Segment Tree
- キーボード <mdi-arrow-right-bold-outline /> <carbon-keyboard /> REALFORCE

</div>
</div>

---
layout: image-right
image: /padlock.jpg
---

# 今回話すこと

1. 南京錠の仕組み
2. 南京錠のピッキングの仕方
3. 南京錠のピッキング対策

画像: [https://ja.wikipedia.org/wiki/南京錠](https://ja.wikipedia.org/wiki/南京錠)

---
layout: image-right
image: /padlock_ana.jpg
---

# 1. 南京錠の仕組み(1)

* 南京錠の鍵穴ってみたことありますか？？
* 南京錠はだいたい<h2>ピンタンブラー錠</h2>と呼ばれる鍵です
* 今日はピンタンブラー錠について話します

画像: https://kagi-otasuketai.com

---

# 1. 南京錠の仕組み(2)

<div style="height: 85%">
 <img src="/padlock_yoko.png" style="height: 100%; display: block; margin: auto;"/>
</div>

画像: [https://www.alsok.co.jp](https://www.alsok.co.jp/person/keystory/09/)

---

# 1. 南京錠の仕組み(3)

<table class="table">
  <tr>
    <td class="table-img">
      1.何もさしていない状態<img src="/padlock_no_key.png" class="table-img-content">
    </td>
    <td class="table-img">
      2.違う鍵をさした状態<img src="/padlock_bad_key.png" class="table-img-content">
    </td>
  </tr>
  <tr>
    <td class="table-img">
      3.合鍵をさした状態<img src="/padlock_with_key.png" class="table-img-content">
    </td>
    <td class="table-img">
      4.合鍵で回した状態<img src="/padlock_unlocked.png" class="table-img-content">
    </td>
  </tr>
</table>

画像: [https://ja.wikipedia.org/wiki/ピンタンブラー錠](https://ja.wikipedia.org/wiki/ピンタンブラー錠)

<style>
  .table-img-content {
    display: block; margin: auto;
  }
  img {
    height: 9.5em;
  }
</style>

---

# 2. 南京錠を開ける方法 - ピッキング(1)

<h2>前提知識</h2>

<div style="height: 85%">
 <img src="/padlock_center.png" style="height: 100%; display: block; margin: auto;"/>
</div>

---

# 2. 南京錠を開ける方法 - ピッキング(2)

<h2>前提知識</h2>

<div style="height: 85%">
 <img src="/padlock_open.png" style="height: 100%; display: block; margin: auto;"/>
</div>

---

# 2. 南京錠を開ける方法 - ピッキング(3)

<h2>道具</h2>

<div style="height: 75%">
 <img src="/dougu.jpg" style="height: 100%; display: block; margin: auto;"/>
</div>

注意: 特殊開錠用具所持禁止法より，この工具は所持自体が違法です！！！  
(僕は日本鍵師協会の許可を得て所持しています)

---

# 2. 南京錠を開ける方法 - ピッキング(4)

<h2>開け方の手順</h2>

<div style="height: 75%">
 <img src="/pick.jpg" style="height: 100%; display: block; margin: auto;"/>
</div>

注意: 特殊開錠用具所持禁止法より，この工具は所持自体が違法です！！！  
(僕は日本鍵師協会の許可を得て所持しています)

---

# 2. 南京錠を開ける方法 - ピッキング(5)

<video controls>
  <source src="/pick_fast.mp4" type="video/mp4">
</video>

---

# 2. 南京錠を開ける方法 - ピッキング(6)

<h2>なぜ開くのか</h2>

<div class="flex">
  <div class="flex-grow">
    <ol>
      <li>テンションをかけると上ピンが内筒と外筒の間に引っかかる</li>
      <li>引っかかった状態で下ピンをピックで軽く押すと，<br>上ピンが下に落ちて来なくなる</li>
      <li>下ピンは引っかかることなく，重力でおちる</li>
      <li>シェアラインが揃う！</li>
    </ol>
  </div>
  <div class="flex-grow">
    <img src="/pick_naname.jpg" style="width: 14em"/>
    <img src="/pick_naname2.jpg" style="width: 14em"/>
    <a href="http://s-akademeia.sakura.ne.jp/main/books/lock/">
    画像: ハッカーの学校 鍵開けの教科書 P176
    </a>
  </div>
</div>

---

# 3. ピッキングされないための鍵の工夫

<div class="flex">
  <div class="flex-grow">
    GOAL v18シリンダー<br />... ピンが大量にあります．
    <br />
    <a href="https://www.rrrmaji.com/product/823"><img src="/goalv18.jpeg" style="height: 13em"/>
    画像: https://www.rrrmaji.com/product/823</a>
  </div>
  <div class="flex-grow">
    アンチピッキングピン<br />... ピッキングすると鍵が回らなくなります．
    <div class="flex">
      <div class="flex-grow">
        <br />普通のピン
        <a href="kagi110qq.com"><img src="/normal_pin.png" style="height: 8em"/></a>
      </div>
      <div class="flex-grow">
        <br />異形ピン
        <a href="kagi110qq.com"><img src="/ikei_pin.png" style="height: 8em"/></a>
      </div>
    </div>
    <br />
    他にも最近のには...
    <ul>
    <li>鍵穴の向きが違ってピックが入らない</li>
    <li>ピンに溝があってピックが抜ける</li>
    <li>ピッキングした際には二度と閉まらなくなる</li>
    などの工夫が！
    </ul>
  </div>
</div>

