[![GitHub Pages](https://github.com/xryuseix/LT/actions/workflows/deploy.yml/badge.svg)](https://github.com/xryuseix/LT/actions/workflows/deploy.yml)

# LT 資料の index ページ(開発中)

[https://xryuseix.github.io/lt](https://xryuseix.github.io/lt)

## 開発 / デプロイ

* httpで特定スライドを起動

```sh
cd なんか/dist && php -S 127.0.0.1:8088
```

* 開発環境で起動

```sh
cd なんか && yarn dev
```

* PDF 取得

```sh
cd なんか && slidev export --format pdf
```

## vue.js の README

### Project setup
```
yarn install
```

### Compiles and hot-reloads for development
```
yarn serve
```

### Compiles and minifies for production
```
yarn build
```

### Lints and fixes files
```
yarn lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
