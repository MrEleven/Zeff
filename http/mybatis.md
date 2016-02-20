今天闲的蛋疼(错了不是闲的蛋疼，而是把电脑忘在公司了)，于是就跑到公司去学mybatis。首先看完了mybatis官方中文文档和mybatis-spring的官方中文文档。感觉有些东西模模糊糊，特别是没有jdbc的基础。

并着绝对清晰的原则，我决定不跳跃从mybatis开始熟悉。

按照官方的教程一路过来听顺利的，不过配置
```
<property name="driver" value="com.mysql.jdbc.Driver"/>
```
这个问题倒是花了不少时间，依赖的maven包是

```
	<dependency>
		<groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <version>5.1.25</version>
    </dependency>
```
终于跑通了第一个数据库查询。


总得来说就是两个对象，搞清楚三个对象是干嘛用的你就能跑通第一个查询了。

* SqlSessionFactory：这个对象包含了一个数据源和事务管理器(事务管理器我还没用)。
* SqlSession：这个类是专门用来执行sql的，所有的数据库查询都需要通过这个类。
* Mapper：就是要执行的sql，只不过加上了结果集和结果类的关系映射。* 

然后是手动创建SqlSessionFactory，这里的数据源可以用MysqlDataSource

Environment的Mapper需要以接口的形式来提供，不然java语法上通不过。

好吧，终于把mybatis官方文档(除了java api部分)看完了，明天继续看mybatis-spring和druid的文档。

