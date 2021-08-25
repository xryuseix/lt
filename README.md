<!-- @format -->

[![GitHub Pages](https://github.com/xryuseix/LT/actions/workflows/deploy.yml/badge.svg)](https://github.com/xryuseix/LT/actions/workflows/deploy.yml) ![Vue.js](https://img.shields.io/badge/Vue.js-3.0.0-3FB27F?logo=Vue.js) ![Slidev](https://img.shields.io/badge/Slidev-0.22.7-4AC2D3)

# LT 資料一覧

**[https://xryuseix.github.io/lt](https://xryuseix.github.io/lt)**

<div style="text-align: center">
  <a href="https://xryuseix.github.io/lt">
    <img src="./images/logo.png" width="50%">
  </a>
</div>

## 開発 / デプロイ

### LT 資料の開発

#### 開発環境で起動 - Slidev

```sh
cd {LTフォルダ}
yarn dev
```

#### 本番環境で起動

```sh
cd {LTフォルダ}/dist
php -S 127.0.0.1:8088
```

#### PDF を取得

```sh
cd {LTフォルダ}
yarn export
```

### index ページの開発

#### 開発環境で起動 - Vue.js

```sh
yarn serve
```

#### デプロイ

- PUSH 時に GitHub Actions が自動デプロイ
- 手元でビルドテストする際は以下のコマンドを打つ

```sh
./deploy_test.sh
```
