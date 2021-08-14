---
theme: default
highlighter: shiki
title: '南京錠ピッキング術 - ピンタンブラー錠の仕組みと開け方を5分で紹介'
colorSchema: 'dark'
---

# <mdi-lock /> 南京錠ピッキング術
<div style="margin-left:5em">
ピンタンブラー錠の仕組みと開け方を5分で紹介！！
</div>

---

# 自己紹介


<div class="flex">
<div class="flex-grow">

## <img src="https://avatars.githubusercontent.com/u/51394682" height="1832" width="1832" style="height: 1.5em; width: auto; display: inline-block; border-radius: 100%" /> 石川琉聖
<br />

- サイバーセキュリティ研究室 **3**回生
- アルゴリズムとセキュリティに興味があります
  - AtCoder <span style="color:lightblue">**水色**</span> / CodeForces <span style="color:#6495ed">**青色**</span>
  - Seccamp'19 暗号化通信ゼミ
  - SecHack365'20 研究駆動コース
- ポートフォリオサイト <mdi-arrow-right-bold-outline /> [https://xryuseix.github.io](https://xryuseix.github.io)
- アカウント <mdi-arrow-right-bold-outline /> <span class="text-twitter">[<carbon-logo-twitter />@ryusei_ishika](https://twitter.com/ryusei_ishika)</span> / [<carbon-logo-github /> xryuseix](https://github.com/xryuseix)
  - IDはだいたい xryuseix です
- 研究(してた)テーマ
  - 競プロのプログラムの盗作検知
  - Zoomのバーチャル背景適用動画から部屋の復元

</div>

<div class="flex-grow">

## 好きな○○
<br />

- 言語 <mdi-arrow-right-bold-outline /> <logos-c-plusplus /> C++, <logos-rust style="background:white"/> Rust, <logos-python /> Python
<img src="https://camo.githubusercontent.com/37eb24996c3cae0fe6b7b804e6bcb32f2141e5bdffbdeecaf046ff64244fc5a9/68747470733a2f2f6769746875622d726561646d652d73746174732e76657263656c2e6170702f6170692f746f702d6c616e67733f757365726e616d653d7872797573656978266c61796f75743d636f6d70616374266c616e67735f636f756e743d3130266578636c7564655f7265706f3d53412d506c61672c4174436f6465725f4261636b75702c5365634861636b3336352d446174617365742c26686964653d68746d6c2c4d616b6566696c652c6373732c5465782c434d616b652c534353532c43267468656d653d746f6b796f6e69676874" style="height:10em" />
- エディタ <mdi-arrow-right-bold-outline /> <vscode-icons-file-type-vscode /> VSCode
- OS <mdi-arrow-right-bold-outline /> <mdi-apple /> macOS
- データ構造 <mdi-arrow-right-bold-outline /> <carbon-decision-tree /> Segment Tree
- キーボード <mdi-arrow-right-bold-outline /> <carbon-keyboard /> REALFORCE

</div>
</div>

---
layout: image-right
image: padlock.jpg
---

# 今回話すこと

1. 南京錠の仕組み
2. 南京錠のピッキングの仕方
3. ピッキングされないための鍵の工夫

画像: https://ja.wikipedia.org/wiki/南京錠 より

---
layout: image-right
image: padlock_ana.jpg
---

# 1. 南京錠の仕組み(1)

* 南京錠の鍵穴ってみたことありますか？？
* 南京錠はだいたい<h2>ピンタンブラー錠</h2>と呼ばれる鍵です

画像: https://kagi-otasuketai.com

---

# 1. 南京錠の仕組み(2)

<div style="height: 85%">
 <img src="/padlock_yoko.png" style="height: 100%; display: block; margin: auto;"/>
</div>

画像: https://www.alsok.co.jp

---

# 1. 南京錠の仕組み(3)

<table class="table">
  <tr>
    <td class="table-img">
      <img src="/padlock_no_key.png" class="table-img-content">
    </td>
    <td class="table-img">
      <img src="/padlock_bad_key.png" class="table-img-content">
    </td>
  </tr>
  <tr>
    <td class="table-img">
      <img src="/padlock_with_key.png" class="table-img-content">
    </td>
    <td class="table-img">
      <img src="/padlock_unlocked.png" class="table-img-content">
    </td>
  </tr>
</table>

画像: https://ja.wikipedia.org/wiki/ピンタンブラー錠

<style>
  .table-img-content {
    display: block; margin: auto;
  }
</style>

---

# 2. 南京錠のピッキングの仕方

---

# 3. ピッキングされないための鍵の工夫
