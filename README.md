# 萌娘百科编辑助手

萌娘百科编辑助手是一款vscode插件，基于[Wikitext-VSCode-Extension](https://github.com/Frederisk/Wikitext-VSCode-Extension)。

## 特性

- 语法高亮
![](./Resource/2021-07-05-12-54-12.png)
- 括号补全
![](./Resource/1.gif)
- 模板提示（目前支持的模板较少，欢迎补充）
![](./Resource/2.jpg)

## 使用方法

## 补充模板提示
由于只有我一人开发，本仓库目前只收录了少部分常用模板。大家可以按以下方式补充：
1. 下载[模板提示表](https://github.com/oxygen-dioxide/moegirl-helper/blob/master/snippets/moegirl-snippets.xlsx)
2. 按以下格式在表格最后一行后追加：
    - 第一列为模板的最简短说明
    - 第二列为模板名称
    - 第三列为模板的完整格式，用${1:}、${2:}等符号代表用户输入的参数
    - 第四列为模板的较详细说明
    - 第一列以\开头的行为注释，可用于分隔
3. [创建issue](https://github.com/oxygen-dioxide/moegirl-helper/issues/new/choose)，将你修改过的xlsx文件作为附件上传。

## 开发
1. 安装[Nodejs](https://nodejs.org/) 10以上版本
2. 下载本仓库并进入目录
```
git clone https://github.com/oxygen-dioxide/moegirl-helper
cd moegirl-helper
```
3. 安装依赖项
```
npm install yarn vsce -g # VS Code Extension Manager
yarn install # Install devDependencies
```
4. 用github打开当前文件夹
```
code .
```
5. 按F5调试
