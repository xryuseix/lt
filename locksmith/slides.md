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
5. 興味を持った方へ

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
    画像: 映画サマーウォーズ
  </div>
</div>

<div class="under-right">
  <a href="https://tsukuctf.sechack365.com">
    <img src="/tsukuctf.png" />
    https://tsukuctf.sechack365.com/
  </a>
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
  .under-right img {
    height: 10em;
    margin: auto;
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

---

# 3. ピッキング

<h2>前提知識</h2>

<div style="height: 80%">
 <img src="/padlock_center.png" style="height: 100%; display: block; margin: auto;"/>
</div>

<div class="comment">
  ところで，一人暮らしで撮影しながら作業するのは大変でした．ピッキングは両手必要ですからね，足で撮影してました．<span style="font-size:0.5em">夏の風物詩・鬱クワガタ！w</span>
</div>

---

# 3. ピッキング

<h2>前提知識</h2>

<div style="height: 80%">
 <img src="/padlock_open.png" style="height: 100%; display: block; margin: auto;"/>
</div>

<div class="comment">
  ところで，一人暮らしで撮影しながら作業するのは大変でした．ピッキングは両手必要ですからね，足で撮影してました．<span style="font-size:0.5em">夏の風物詩・鬱クワガタ！w</span>
</div>

---

# 3. ピッキング

<h2>道具</h2>



<div class="flex">
  <div class="flex-grow">
    <ul>
      <li>テンション(上の棒)</li>
      <li>ピック(下の棒)</li>
    </ul>
  </div>
  <div class="flex-grow" style="width: 30%;margin-right: 40px;">
    <img src="/dougu.jpg"/>
  </div>
</div>

注意: 特殊開錠用具所持禁止法より，この工具は所持自体が違法です！！！  
(僕は鍵師資格を所持しています)

---

# 3. ピッキング

<h2>開け方の手順</h2>

<div style="height: 75%">
 <img src="/pick.jpg" style="height: 100%; display: block; margin: auto;"/>
</div>

注意: 特殊開錠用具所持禁止法より，この工具は所持自体が違法です！！！  
(僕は鍵師資格を所持しています)

---

# 3. ピッキング

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
    <img src="/pick_naname.jpg" style="width: 15em"/>
    <img src="/pick_naname2.jpg" style="width: 15em"/>
    <a href="http://s-akademeia.sakura.ne.jp/main/books/lock/">
    画像: ハッカーの学校 鍵開けの教科書 P176
    </a>
  </div>
</div>

---

# 3. ピッキング

<video controls>
  <source src="/padlock_pick.mp4" type="video/mp4">
</video>

---

# 3. ピッキング

<video controls>
  <source src="/pick_fast.mp4" type="video/mp4">
</video>

---

# 4. ピッキング対策

## そんな簡単に開いたら困るだろ！！！！！！

つまり

<h2><mdi-arrow-right-bold-outline />南京錠はDES暗号みたいなものです</h2>

専門知識を持った人はすぐ開く，そうではない人は開かない．

<h2><mdi-arrow-right-bold-outline />特に玄関錠はちゃんとしてないと困る！！！</h2>

空いたら困るシリーズだと，あとは金庫とかね．金庫は今回話しませんが，簡単なものは20分くらいで開きます．  
(南京錠と比べるとかなり難しい)

---

# 4. ピッキング対策

## 4-1. ピン数を増やす / ピンの位置をずらす

<div style="height: 85%">
  <a href="https://www.rrrmaji.com/data/rrrrr/product/20170118_ed250f.png">
    <img src="/goalv18.jpeg" style="height: 100%; display: block; margin: auto;"/>
  </a>
</div>

---

# 4. ピッキング対策

## 4-2. アンチピッキングピン

<div class="flex">
  <div class="flex-grow" style="width: 45%; margin-right: 10px">
    <br />普通のピン
    <img src="/normal_pin.png" class="table-img-content" style="height: 100%"/>
  </div>
  <div class="flex-grow" style="width: 45%">
    <br />異形ピン
    <img src="/ikei_pin.png" class="table-img-content" style="height: 100%"/>
  </div>
</div>

---

# 4. ピッキング対策

## 4-2. アンチピッキングピン

<div class="flex">
  <div class="flex-grow" style="width: 45%; margin-right: 10px">
    <br />画像: ハッカーの学校 鍵開けの教科書 P186
    <img src="/anti_pick.jpg" class="table-img-content" style="width: 100%"/>
  </div>
  <div class="flex-grow" style="width: 45%">
    <br />異形ピン
    <img src="/ikei_pin.png" class="table-img-content" style="width: 100%"/>
  </div>
</div>
<div class="comment">
  ↑鍵開けの教科書わかりやすくない？？全人類買いましょう^^
</div>

---

# 4. ピッキング対策

## これまでの対策は初歩の初歩です

<br />

* 今の玄関錠はこの何倍も開きにくくなる対策をいっぱいしてます．
* 破錠(ドリリング)対策もしてます．
* なので開かないです(開く場合もありますが)．

<h2>一般人の一番の対策は空き巣に入るときに</h2>
<h2 style="text-align:center;margin: 10px;">「開けるのめんどくせえな」「他の家にしよう」</h2>
<h2 style="text-align:right">と思わせることです．</h2>

<div class="comment">
  なんとしても玄関を開けたいと思われるような<b>豪邸にお住みの方</b>，至急ご連絡ください．叙々苑にいきましょう．
</div>

---

# 4. ピッキング対策

## じゃあ玄関にはどの鍵使えばいいの？

<div class="flex">
  <div class="flex-grow">
    <br />
    とりま MIWA U9 を使っておけばおk<br />
    (まあ鍵屋さん行って)
    <br />
    <ul>
      <li>ピッキングは絶対に無理</li>
      <li>破錠も厳しい(時間がかかる)</li>
      <li>↑場合によっては壁突き破った方が楽</li>
    </ul>
  </div>
  <div style="height: 85%">
    <a href="http://www.kagiyasan.jp/img/item/common/cylinder/MIWA/U9-MCY-136_2.jpg">
      <img src="/miwau9.jpeg" style="height: 100%; display: block; margin: auto;"/>
    </a>
  </div>
</div>

---

# 5. 興味を持った方へ

## 入門はとりあえずこれが良き

<div class="flex">
  <div class="flex-grow" style="text-align: center;">
    <a href="http://s-akademeia.sakura.ne.jp/main/books/lock/">
    <img src="kagiake_cover.png" style="height: 65%; display: block; margin: auto;"/>
    ハッカーの学校 鍵開けの教科書
    </a>
  </div>
</div>

---

# 5. 興味を持った方へ

## ピッキング(実技)も知りたい

<div class="flex">
  <div class="flex-grow" style="text-align: center;">
    <img src="youtube.png" style="height: 60%; display: block; margin: auto;"/>
    Youtubeで「ピッキング 鍵」とかで検索 <span style="font-size:0.8em">(<code>鍵</code>がないとギターが出てくる)</span>
  </div>
</div>

---

# 5. 興味を持った方へ

## ピッキングしてみたい

<div class="flex">
  <div class="flex-grow" style="width: 100em">
    <br />
    鍵師として働くための講習が受けられます
    <ul>
      <li>ピッキング</li>
      <li>合鍵作成</li>
      <li>シリンダー交換</li>
    </ul>
    など
  </div>
  <div class="flex-grow" style="text-align: center;">
    <img src="kagisi.png" style="height: 85%; display: block; margin: auto;"/>
    僕の場合，講習代+試験代+交通費+飲食費=15,6万くらいでした
  </div>
</div>

---

# 6. 最後に

<div class="text">
  物理 & サイバー ハッキングを<br />
  是非両方やってみませんか？？？
</div>

<div class="under-right">
  以上！ご静聴ありがとうございました！！
</div>

<style>
.text {
  width: 90%;
  text-align: center;
  font-size: 2em;
  line-height: 1.5em;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translateY(-50%) translateX(-50%);
}
</style>