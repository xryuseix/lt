---
theme: default
highlighter: shiki
title: 物理鍵の仕組みと開け方[作成中]
colorSchema: dark
download: true
---

<!-- @format -->

<!--
[内容]
* 導入
  * 自己紹介
  * 物理鍵と電子鍵
* 鍵の種類の紹介
* ピンタンブラー錠の仕組み
* ピッキング
  * ピンタンブラー錠のピッキング
* ピッキング対策
  * 結局何使えばいいの？
* 興味を持った人へ
  * 鍵師の紹介
  * 鍵師講座の紹介
* 想定Q&A
-->

# <mdi-lock /> 物理鍵の仕組みと開け方

<div style="margin-left:5em">
物理鍵の仕組みと開け方を <b>超簡単に</b> 紹介
</div>
<div class="under-right">
<mdi-arrow-down-bold-outline />詳しく資料が見たい方はこちら！
  <a href=https://xryuseix.github.io/lt/locksmith>
    <img src="/qrcode.png" />
    https://xryuseix.github.io/lt/locksmith
  </a>
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
- アルゴリズムとセキュリティに興味があります
  - SecHack365'20 研究駆動コース
  - Seccamp'19 暗号化通信ゼミ
  - AtCoder <span style="color:lightblue">**水色**</span> / CodeForces <span style="color:#6495ed">**青色**</span>
- Web サイト <mdi-arrow-right-bold-outline /> [https://xryuseix.github.io](https://xryuseix.github.io)
- アカウント <mdi-arrow-right-bold-outline /> <span class="text-twitter">[<carbon-logo-twitter />@ryusei_ishika](https://twitter.com/ryusei_ishika)</span> / [<carbon-logo-github /> xryuseix](https://github.com/xryuseix)
  - ID はだいたい **xryuseix** です
- SecHack での研究テーマ
  - 競プロのプログラムの盗作検知
  - [Zoom のバーチャル背景適用動画から部屋の復元](https://github.com/Tsuku43/zoomg)

</div>

<div class="flex-grow">

<div class="qrcode under-right">
  <a href=https://xryuseix.github.io/lt/locksmith>
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

1. 鍵の種類の紹介
2. ピンタンブラー錠の仕組み
3. ピッキング
4. ピッキング対策
5. 興味を持った人へ
6. Q & A

<div class="under-left">
画像: <a href="https://ja.wikipedia.org/wiki/南京錠">https://ja.wikipedia.org/wiki/南京錠</a>
</div>

---

# 1. 鍵の種類の紹介

## 電子鍵

<div class="flex">
  <div class="flex-grow left">
    <br />
    皆さんが詳しいやつです．
    <ul>
      <li>公開鍵</li>
      <li>秘密鍵</li>
    </ul>
    などがありますね．
    <br />
    <br />
    CTF でも暗号分野でよく使われています．<br />
    ところで，今日は <br />
    <div class="gaming">TsukuCTF</div>
    が併催されています．僕も数問提供しています．
  </div>
  <div class="flex-grow summer">
    <img src="/summer.jpeg"/>
    <div class="under-right">画像: 映画サマーウォーズ</div>
  </div>
</div>

<style>
  .left {
    width: 60%;
    margin-right: 20px;
  }
  .summer img {
    width: 75%;
  }
  .gaming{
    text-align: center;
    height: 1.5em;
    line-height: 1.5em;
    font-weight: bold;
    -webkit-text-stroke: 2px black;
    font-size: 2.4em;
    margin: 10px;
    color: black;
    background-clip: text;          /*背景を文字で切り抜く*/
    background-image : linear-gradient(45deg,
        red,
        orange,
        yellow,
        green,
        aqua,
        blue,
        purple
    );
  }
</style>

---

# 1. 鍵の種類の紹介

## 物理鍵

<table class="table">
  <tr>
    <td class="table-img">
      <a href="https://www.miwa-lock.co.jp/lock_day/lineup/cylinder/subbnr/hole1.gif">
        玄関錠<img src="/hole.png" class="table-img-content">
      </a>
    </td>
    <td class="table-img">
      <a href="https://content.misumi-ec.com/image/upload/t_popover_main/v1/p/jp/product/series/223300463137/223300463137_001.jpg">
        ダイヤル錠<img src="/dial.jpeg" class="table-img-content">
      </a>
    </td>
  </tr>
  <tr>
    <td class="table-img">
      <a href="https://www.kk-alpha.com/cp/img/img_alpha11.jpg">
        八万ロック錠<img src="/hatiman.jpeg" class="table-img-content">
      </a>
    </td>
    <td class="table-img">
      <a href="https://www.kagi110qq.co.jp/test_com/img/works/img_31.png">
        金庫のダイヤル錠<img src="/kotei_dial.png" class="table-img-content">
      </a>
    </td>
  </tr>
</table>

<style>
  .table-img-content {
    display: block; margin: auto;
  }
  img {
    height: 9.5em;
  }
</style>

---

# 1. 鍵の種類の紹介

## 今回話す錠前について

<div class="flex">
  <div class="flex-grow">
    <br />ピンタンブラー錠
    <img src="/padlock_ana.jpg"  class="table-img-content"/>
  </div>
  <div class="flex-grow">
    <br />ディスクシリンダー錠
    <a href="https://www.miwa-lock.co.jp/lock_day/lineup/cylinder/subbnr/hole1.gif">
      <img src="/hole.png" class="table-img-content">
    </a>
  </div>
</div>

<style>
  .flex {
    font-size: 1.2em;
  }
  .table-img-content {
    display: block;
    margin: auto;
  }
  img {
    height: 14em;
  }
</style>

---

# 2. ピンタンブラー錠の仕組み

<div style="height: 85%">
  <a href="https://www.alsok.co.jp/person/keystory/09/">
    <img src="/padlock_yoko.png" style="height: 100%; display: block; margin: auto;"/>
  </a>
</div>

---

# 2. ピンタンブラー錠の仕組み

<table class="table">
  <tr>
    <td class="table-img">
      <a href="https://ja.wikipedia.org/wiki/ピンタンブラー錠">
        1.何もさしていない状態<img src="/padlock_no_key.png" class="table-img-content">
      </a>
    </td>
    <td class="table-img">
      <a href="https://ja.wikipedia.org/wiki/ピンタンブラー錠">
        2.違う鍵をさした状態<img src="/padlock_bad_key.png" class="table-img-content">
      </a>
    </td>
  </tr>
  <tr>
    <td class="table-img">
      <a href="https://ja.wikipedia.org/wiki/ピンタンブラー錠">
        3.合鍵をさした状態<img src="/padlock_with_key.png" class="table-img-content">
      </a>
    </td>
    <td class="table-img">
      <a href="https://ja.wikipedia.org/wiki/ピンタンブラー錠">
        4.合鍵で回した状態<img src="/padlock_unlocked.png" class="table-img-content">
      </a>
    </td>
  </tr>
</table>

<style>
  .table-img-content {
    display: block; margin: auto;
  }
  img {
    height: 9.5em;
  }
</style>

---

# 2. ピンタンブラー錠の仕組み

<video controls>
  <source src="/padlock_skeleton.mp4" type="video/mp4">
</video>

---

# 3. ピッキング

<video controls>
  <source src="/padlock_pick.mp4" type="video/mp4">
</video>

