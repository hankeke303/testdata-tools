# testdata-tools

**一个可以用来快速生成可以适用于 syzoj 的配置文件 `data.yml`。**

使用方法：

```sh
python tool.py
```

`Input-pre: ` 你要配置的输入文件的前缀；

`Input_suf: ` 你要配置的输入文件的后缀，如果为空，则默认为 `.in`；

`Output_pre: ` 你要配置的输出文件的前缀，如果为空，则默认与 `Input-pre` 相同；

`Output_suf: ` 你要配置的输入文件的后缀，如果为空，则默认为 `.out`；

`Numbers of subtasks: ` 你要配置的 `subtask` 的数量，如果为空则默认为 `0`。
后面每一行的格式为：

```plain
score(type): data-list
```

其中，`score` 为该 `subtask` 的分值，`type` 为评分方式，可选的有 `min`, `max`, `sum`, `mul`。如果没有 `(type)` 这一部分，默认为 `min`。

后面的 `data-list` 中，每一个测试点编号用 `,` 隔开。可以使用 `l-r` 表示从 `l` 到 `r` 的所有编号。

测试点编号中可以带英文字母，如果需要使用一段英文字母后带编号的格式，可以使用类似于 `chess(1-10)` 的格式，即将 `l-r` 外加入括号。单独的 `l-r` 不需要括号。

## Todo

1. 自动识别当前文件夹的数据，把子文件夹作为 `subtasks`。
2. 增加帮助修改数据名称的功能。
