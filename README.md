[![GitHub Pages](https://github.com/xryuseix/LT/actions/workflows/deploy.yml/badge.svg)](https://github.com/xryuseix/LT/actions/workflows/deploy.yml)

# LT資料

* httpで特定スライドを起動

```sh
cd なんか/dist && php -S 127.0.0.1:8088
```

* httpで全てのスライドを起動

```sh
php -S 127.0.0.1:8088
```

* 開発環境で起動

```sh
cd なんか && yarn dev
```

# これからやること

1. これ作る

```txt
public/
  - index.html
  - github-111days/
    - index.html
    - assets/
      - hoge.png
      - fuga.js
      - piyo.css
    - XXX.png
```

2. index.htmlのパスを相対パスにする
3. deploy.ymlを編集する