从我进米帮的第一个项目Baade开始我就一直对单元测试感兴趣，只是到现在我对单元测试这个东西还不是很懂。

今天花了点时间看了python.org上面关于unittest的部分。

虽然早就知道单元测试，说的就是单元，每个测试用例之间应该有隔离性。但是今天的十分想把这些测试用例联系起来，这样可以少维护一份数据库，但事实证明这是一个错误的选择。

python unittest模块中TestCase中方法的执行顺序是通过函数名来确定的，虽然可以通过重写字符串比较方法来指定执行的顺序，也可以通过按一个约定来命名测试方法，但是违背作者初衷写测试始终是不对的。不过一个有意思的地方就是可以在整个TestCase测试完毕之后在tearDownClass中恢复环境，可以在setUpClass中创建环境。

今天还看了Mock这个东西，这个东西还是蛮牛逼的，不过不太适合我们当前项目的单元测试，成本有点大，而且覆盖度不容易保证。
之前公司测试都是手工测的，我在测试上面浪费了不少时间，既然我是米帮的工程师，那我就有义务推动米帮向前进步。我决定带头写单元测试。
中间问了死月学长，发现花瓣也是单独维护一套测试数据库的。然后问了赵云峰，群核云计算也和我们公司一样在网测试自动化的方向转型。当然还是十分感谢很多IT界的朋友的，最后主要要感谢杨忠秀老师，她说她以前在华为也是和我一样的做法。维护一套测试数据库，每次跑测试脚本的时候都重新生成一下。加油，测试自动化之后效率就会提高很多了。

###### Mock的一些文章
* http://www.toptal.com/python/an-introduction-to-mocking-in-python
* http://www.oschina.net/translate/unit-testing-with-the-python-mock-class?cmp&p=1#
* 官方文档：http://www.voidspace.org.uk/python/mock/index.html
* 看了这个才觉得恍然大悟： http://googletesting.blogspot.com/2013/05/testing-on-toilet-dont-overuse-mocks.html