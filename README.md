# testing-module-logger-with-pytest

## これは何

「pytestのcaplogを使ったログ出力のテスト」における落とし穴を検証するためのサンプルコードです。  

## 事前準備

このリポジトリではDocker及びdocker-composeによってDebianベースのコンテナの環境構築を行います。  
よって、Docker及びdocker-composeの2つがインストールされていればOKです。

参考程度に、筆者（[@koralle](https://github.com/koralle)）がこのリポジトリを作成時の環境は以下の様になっています。

- PC ... MacBook Pro (13-inch, 2019, Four Thunderbolt 3 ports)
- OS ... macOS BigSur バージョン11.4

```bash
docker --version
Docker version 20.10.7, build f0df350
```

```bash
docker-compose --version
docker-compose version 1.29.2, build 5becea4c
```

## 環境構築

### VSCodeの拡張機能Remote Containersを使用する場合

VSCodeでこのプロジェクトフォルダを開きます。  
その後コマンドパレットを開き、`Remote-Containers: Rebuild and Reopen in Container`を選択するとコンテナのビルド〜Poetryによる依存関係のインストールまで自動で完了します。

### VSCodeの拡張機能Remote Containersを使用しない場合

`docker-compose`でコンテナを立ち上げ、`docker exec`でコンテナに入ります。

```bash
docker-compose up -d && docker exec -it testing-module-logger-with-pytest /bin/bash
```

その後、コンテナ内で `make setup`を実行すると内部でPoetryによる依存関係のインストールが始まります。

```bash
make setup
```

## 参考

- [Logging — pytest documentation](https://docs.pytest.org/en/6.2.x/logging.html)
- [Handling of loggers with propagate=False · Issue #3697 · pytest-dev/pytest](https://github.com/pytest-dev/pytest/issues/3697)
- [pytestでログ出力をテストしたい (caplog) - Qiita](https://qiita.com/mag-chang/items/446eeb5f04022eb663f1)
- [pytestでloggingのログ出力をテストする - yiskw note](https://yiskw713.hatenablog.com/entry/2021/04/08/105245)
- [pytestのcaplogを使ってログのテストをする | | とむるの目録](https://tommru.com/programing/python/sample_caplog/)
