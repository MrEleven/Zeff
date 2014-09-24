现在在公司上班，因为等着同事给我的模块，所以有空，就决定提前吧今天的Github给写了。
今天来说一下Python的string类型。
<pre>
str.capitalize() 表示将第一个字符大写，后面的所有字母小写。(PS:这个方法对我个人很有用。)
str.center(width, [fillchar]) 表示将str用fillchar填充撑固定宽度，str处于被填充的字符的中间。
str.count(sub), 统计子字符串在str中出现的次数
str.decode() 解码
str.encode() 编码
str.endswith(suffix) 判断是否以suffix结束
str.find(sub) 查找sub在str中的位置,如果没有找到则返回-1
str.format() 格式化显示
str.index(sub) 索引，查找sub在str中的位置
str.isalnum() 判断一个字符串是否全部由字母或者数字组成
str.isalpha() 判断一个字符串是否全部由英文字母组成
str.isdigit() 判断一个字符串是否全部由数字组成
str.isspace() 判断一个字符串是否由空白字符组成。(如果是空字符串，返回False)
str.istitle() 判断一个字符串是否是title格式
str.isupper() 判断一个字符串中的字符是否是大写格式
str.join() 这个我就不用多说了
str.ljust(width) 填充字符串，向左对齐
str.lower() 将字符串转化撑小写
str.lstrip() 清除左边的空白符
str.partition(sep) 以sep为标准吧字符串分割撑三个部分，如果没有找到sep，则返回包含字符串本身，两个空字符串的一个三元组
str.replace(old, new) 这个也没有什么好说的，字符串替换
str.rfind() 从右边开始查找
str.rindex() 从邮编开始suoyin
str.rjust(width) 填充固定宽度，向右侧漂浮
str.rpartition(seq) 从右侧开始切割
str.rsplit(sep[, maxsplit]) 从右边开始切割, 在没有指定maxsplit的时候str.rsplit()和str.split()的行为是一样的
str.rstrip() 清除右边的空白符
str.split(seq[,maxsplit]) 从左侧开始切割
str.startswith(prefix) 判断str的开始几个字符串是否就是prefix
str.strip() 清除左右两边的空白字符
str.swapcase() 表示将大写字符串转化撑小写，小写字符串转化为大写。
str.title() 将字符串转化成title模式。
str.translate() 将字符串过滤一些制定的字符
str.upper() 将字符串转化撑大写
str.zfill() 将数字字符串填充成指定的宽度
unicode.isnumeric() 判断这个unicode是否由数字字符组成
unicode.isdecimal() 判断这个unicode是否代表decimal类型。


今天还发现Dictionary View Objects这个有用的东西。 dictview通过dict.viewitems(), dict.viewkeys(), dict.viewvalues()获得，可以进行与/或，与非，异或等运算，可以很方便的用在筛选合并上。

对了，今天还去参加了杭州的Docker开发者大会，是在一家西城广场的网咖里，网咖环境还不错，以后可以去玩玩。参加了这次Docker开发者大会之后，有个体会，不能一直做工程啊。