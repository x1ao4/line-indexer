# line-indexer
使用 line-indexer 可以为你的文本自动逐行添加索引号。
<br>
<br>
## 功能演示
假设`input.txt`文件中的内容如下：
```
apple
banana
cherry
```
运行脚本后，`output.txt`文件中的内容将变为：
```
1;apple
2;banana
3;cherry
```
每一行前面都添加了一个索引号，用`;`与原来的内容分隔。
<br>
<br>
## 运行条件
请确保您的系统上安装了 Python 3.6 或更高版本。
<br>
<br>
## 使用方法
1. 将仓库克隆或下载到计算机上的一个目录中。
2. 修改`start.command (Mac)`或`start.bat (Win)`中的路径，以指向您存放`line-indexer.py`脚本的目录。
3. 将要处理的文本保存为`input.txt`文件，并放在与脚本相同的目录中。
4. 双击运行`start.command`或`start.bat`脚本以执行`line-indexer.py`脚本。
5. 结果将写入到同一目录下名为`output.txt`的文件中。

您也可以通过编辑`line-indexer.py`脚本中`{i};{line}`的部分来自定义分隔符，将`;`替换为您想要的分隔符即可。
<br>
<br>
<br>
# line-indexer
With line-indexer, you can automatically add line numbers to your text file.
<br>
<br>
## Example
Assuming the contents of the`input.txt`file are as follows:
```
apple
banana
cherry
```
After running the script, the content of the`output.txt`file will be:
```
1;apple
2;banana
3;cherry
```
A line index number is added before each line, separated by a`;`from the original content.
<br>
<br>
## Requirements
Make sure you have Python 3.6 or higher installed on your system.
<br>
<br>
## Usage
1. Clone or download the repository to a directory on your computer.
2. Modify the path in`start.command (Mac)`or`start.bat (Win)`to point to the directory where you store the`line-indexer.py`script.
3. Save the text to be processed as an`input.txt`file and place it in the same directory as the script.
4. Double-click`start.command`or`start.bat`to execute the`line-indexer.py`script.
5. The result will be written to a file named`output.txt`in the same directory.

You can also customize the separator by editing the`{i};{line}`part in the`line-indexer.py`script. Simply replace`;`with your desired separator.
