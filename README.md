# uekspider
Scrapy，Python开发的一个快速、高层次的屏幕抓取和web抓取框架，用于抓取web站点并从页面中提取结构化的数据。Scrapy用途广泛，可以用于数据挖掘、监测和自动化测试。  
Scrapy吸引人的地方在于它是一个框架，任何人都可以根据需求方便的修改。它也提供了多种类型爬虫的基类，如BaseSpider、sitemap爬虫等，最新版本又提供了web2.0爬虫的支持。
#### 一、目录结构
```python
 uekspider     项目文件
    |-spiders  爬虫
        |-__init__.py  （忽略）
        |-a185666.py  爬虫文件
        |- ...  其他爬虫文件
    |-items.py 爬取数据字段，类似数据库字段
    |-middlewares.py  中间件模块（忽略）
    |-pipelines.py    管道文件 （忽略）
    |-settings.py     爬虫设置文件
 |- README.md
 |-scrapy.cfg  Scrapy设置文件（忽略）
```
#### 二、入门教程
###### 1、windows安装
>(1) 下载Twisted，Scrapy 依赖Twisted。Twisted是用Python实现的基于事件驱动的网络引擎框架 [点击下载](https://www.lfd.uci.edu/~gohlke/pythonlibs/) 下载请确认本地python版本  
(2)执行语句 **pip install Twisted-18.9.0-cp37-cp37m-win32.whl**  进行Twisted安装  
(3)安装scrapy pip install scrapy

##### 2、创建scrapy项目
```python
scrapy startproject 项目名
```
##### 3、创建爬虫文件
```python
scrapy genspider 爬虫名字(名字我使用的是id表示)  站点地址如(baidu.com)
```
运行完程序，项目spiders\文件夹中会出现一个爬虫文件  
```python
import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"   # 爬虫名
    allowed_domains = ["dmoz.org"]  # 站点名
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    ]  # 爬虫第一次爬取页面地址

    def parse(self, response): # 运行爬虫要执行的文件
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)

```
##### 4、运行爬虫
```python
scrapy crawl 爬虫名字
```

##### 5、项目中可能用到的response对象方法
>xpath()
```python
def parse(self,response): 
    # （1）获取元素对象方法
    res1 = response.xpath("xpath语法")
    # （2）获取元素内容方法
    res2 = response.xpath("xpath语法").extract() 
    # （3）获取元素对象并通过正则进行匹配内容，返回元素内容
    res3 = response.xpath("xpath语法").re("正则语法")
    # 一般我们测试时只获取元素内容，常用（2）（3）
    print(res1,res2,res3) #输出内容检查是否能够获取
```

