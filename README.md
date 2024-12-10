# File-Manipulator-Program

### 概要

テキストファイルの内容を反転・コピー・複製・文字の置き換えした新しいファイルを作成するプログラムです

### 操作方法

-  reverse：inputpath にあるファイルを受け取り、outputputh に inputpath の内容を逆にした新しいファイルを作成します

    ```python3 main.py reverse inputpath outputpath```

- copy：inputpath にあるファイルをコピーを作成し、outputpath として保存します

    ```python3 main.py copy inputpath outputpath```

- duplicate-contents：inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します

    ```python3 main.py duplicate-contents inputpath n```

- replace-string：inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' のすべてを 'newString' に置き換えます

    ```python3 main.py replace-string needle newstring```

