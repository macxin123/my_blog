# coding:utf-8
import json
from elasticsearch import Elasticsearch

# Elasticsearch
es = Elasticsearch([{"host": "192.168.0.141", "port": 9200}])
mapping = {
    'properties': {
        'title': {
            'type': 'text',
            'analyzer': 'ik_max_word',
            'search_analyzer': 'ik_max_word'
        }
    }
}
es.indices.create(index='blogs', ignore=400)
result = es.indices.put_mapping(index='blogs', doc_type='politics', body=mapping, ignore=400, include_type_name=True)

dsl1 = {
    'doc': {
        'bad': 0,
        'body': '![](https://upload-images.jianshu.io/upload_images/21642236-456737a42524076a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)\r\n\r\n### 什么是正则表达式？\r\n\r\n正则表达式(Regular Expression)，又称规则表达式，通常被用来检索、替换那些符合某个模式(规则)的文本。许多程序设计语言都支持利用正则表达式进行字符串操作。\r\n\r\nPython 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。re 模块使 Python 语言拥有全部的正则表达式功能。\r\n\r\n正则表达式的使用对特殊字符进行了转义，所以如果我们要使用原始字符串，只需加一个 r 前缀。\r\n\r\n### 元字符\r\n\r\n正则表达式由一些普通字符和一些元字符（metacharacters）组成。普通字符包括大小写的字母和数字，而元字符则具有特殊的含义。下列为一些常见的元字符的使用说明。\r\n\r\n```\r\n匹配边界:\r\n\t^     匹配行首\r\n\t$     匹配行尾\r\n\t\r\n重复次数:\r\n\t？    重复匹配0次或1次\r\n\t*     重复匹配0次或更多次\r\n\t+     重复匹配1次或更多次\r\n\t{n}   重复n次\r\n\t{n,}  重复n次或更多次\r\n\t{n,m} 重复n~m次\r\n\t\r\n各种字符的表示:\r\n\t.     匹配除了换行符以外的任意字符串\r\n\t[a-z] 任意a-z的字母\r\n\t[abc] a,b,c中任意字符\r\n\t\\d    匹配数字\r\n\t\\D    匹配任意非数字的字符\r\n\t\\w    数字，字母，下划线\r\n\t\\W    匹配任意不是字母，数字，下划线的字符\r\n\t\\s    空白字符（回车，制表，空格）\r\n\t\\S    匹配任意不是空白符的字符\r\n\t\\b    单词的边界\r\n\t\\B    匹配不是单词开始和结束的位置\r\n\t\r\n其他:\r\n\t[^123abc] 匹配除了123abc这几个字符以外的任意字符\r\n\t123|abc   匹配123或者abc \r\n```\r\n\r\n### Pattern 对象\r\n\r\ncompile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 re 模块的查找方法使用。语法格式为：\r\n\r\n```python\r\npattern = re.compile(r\'正则表达式\'，\'匹配模式\')\r\n\r\n# 常用的匹配模式:\r\n#   re.S    可以让 . 匹配换行符\r\n#   re.I    忽略大小写\r\n#   re.M    多行匹配，影响 ^ 和 $ \r\n```\r\n\r\n###  单次匹配\r\n\r\nre 模块中，有两个方法，match 函数和 search 函数，这两个函数都是单次匹配，都返回一个\r\nMatch 对象。\r\n\r\n```python\r\nre.match(pattern, string, start, end)\r\n# pattern.match(string, start, end)\r\n\r\nre.search(pattern, string, start, end)\r\n# pattern.match(string, start, end)\r\n\r\n# pattern  正则表达式对象\r\n# string   要匹配的目标字符串\r\n# start    要匹配的目标字符串的起始位置(可选)\r\n# end为    要匹配的目标字符串的结束位置(可选)\r\n\r\n"""案例"""\r\n\r\nimport re\r\n\r\npattern = re.compile(r\'\\w+\', re.I)\r\n\r\nstring = \'I love python\'\r\n\r\nresult = pattern.match(string, 2, 6)\r\n\r\nprint(result)\r\n# <re.Match object; span=(2, 6), match=\'love\'>\r\n\r\nprint(result.group())\r\n# love\r\n```\r\n\r\n需要注意的是，match 函数 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，而 search 函数是匹配整个字符串，直到找到一个匹配。\r\n\r\n```python\r\nimport re\r\n\r\nstring = \'i am 18 !!!\'\r\n\r\nresult1 = re.match(r\'\\d+\', string)\r\nresult2 = re.search(r\'\\d+\', string)\r\n\r\nprint(result1)\r\n# None\r\nprint(result2.group())\r\n# 18\r\n```\r\n\r\n### 分组\r\n\r\n在Python中，正则表达式分组就是用一对圆括号“()”括起来的正则表达式，匹配出的内容就表示一个分组。即每个圆括号都是一个分组，从1开始。需要注意的是，有一个隐含的全局分组（就是0），也就是整个正则表达式。\r\n\r\n```python\r\nimport re\r\n\r\npattern = re.compile(r\'name is (.*),age:(\\d+)\', re.I)\r\n\r\nstring = \'my name is 啊哈哈君,age:18 !\'\r\n\r\nresult = pattern.search(string)\r\n\r\nprint(result)\r\n# <re.Match object; span=(3, 22), match=\'name is 啊哈哈君,age:18\'>\r\nprint(result.group())\r\n# name is 啊哈哈君,age:18\r\nprint(result.group(1))\r\n# 啊哈哈君\r\nprint(result.group(2))\r\n# 18\r\n```\r\n\r\n###  Match  对象\r\n\r\n关于match函数和search函数返回的match对象，也是有很多方法可以调用的。如上述案例的group函数，会返回被匹配的字符串。\r\n\r\n```python\r\n# 返回被匹配的字符串，等价于group(0)\r\nMatch.group()  \r\n\r\n# 返回第n个分组匹配的字符串，如果组号不存在，则返回indexError异常\r\nMatch.group(n)\r\n\r\n# 返回组号为n到m组所匹配的字符串的元组，如果组号不存在，则返回indexError异常\r\nMatch.group(n,m) \r\n\r\n# 返回所有分组匹配的字符串的元组\r\nMatch.groups()\r\n\r\n# 返回匹配开始的位置\r\nMatch.start()\r\n\r\n# 返回匹配结束的位置\r\nMatch.end()\r\n\r\n# 返回一个元组包含匹配 (开始,结束) 的位置\r\nMatch.span()\r\n```\r\n\r\n### 多次匹配\r\n\r\nre 模块中的findall函数与finditer函数用于进行多次匹配。相信通过函数名，有些小伙伴就可以知道这两个函数的返回值。\r\n\r\n```python\r\nimport re\r\n\r\nstring = \'abcdefg\'\r\n\r\nresult1 = re.findall(r\'\\w\', string)\r\nresult2 = re.finditer(r\'\\w\', string)\r\n\r\nprint(result1)\r\n# [\'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'g\']\r\nprint(result2)\r\n# <callable_iterator object at 0x000002452F017848>\r\n```\r\n\r\n由上述案例可看出，多次匹配与单次匹配的函数用法相同，也可以加start和end。只是findall函数返回的是一个列表，而finditer返回的是一个迭代器。\r\n\r\n### 分割字符串\r\n\r\nre 模块提供了一个spilt函数，用于通过正则表达式分割字符串，并返回一个列表。\r\n\r\n```\r\nimport re\r\n\r\npattern = re.compile(r\'\\s\', re.I)\r\n\r\nstring = \'python java c++\'\r\n\r\nresult = pattern.split(string)\r\n\r\nprint(result)\r\n# [\'python\', \'java\', \'c++\']\r\n```\r\n\r\n### 替换字符串\r\n\r\nre 模块中的sub函数用于通过正则表达式替换字符串。格式为：\r\n\r\n```python\r\nre.sub(pattern, repl, string, count)\r\n# pattern.sub(repl, string, count)\r\n\r\n# pattern  正则表达式或者正则对象\r\n# repl     替换的字符串，也可为一个函数\r\n# string   要被查找替换的原始字符串\r\n# count    匹配后替换的最大次数，默认为0，表示替换所有的匹配\r\n```\r\n\r\n这个函数通过案例是很容易理解的。\r\n\r\n```\r\nimport re\r\n\r\npattern = re.compile(r\'python\', re.I)\r\n\r\nstring = \'I Love Python, Python NB!\'\r\n\r\nresult1 = pattern.sub(\'java\', string)\r\nresult2 = pattern.sub(\'java\', string, 1)\r\n\r\nprint(result1)\r\n# I Love java, java NB!\r\nprint(result2)\r\n# I Love java, Python NB!\r\n```\r\n\r\n当repl为函数时，函数的参数只能为match对象，并且这个函数必须有返回值，返回值的格式是字符串，将来就用这个字符串作为替换的内容。\r\n\r\n```python\r\nimport re\r\n\r\npattern = re.compile(r\'python\', re.I)\r\n\r\n\r\ndef func(matched):\r\n    return matched.group()+\' And Java\'\r\n\r\n\r\nstring = \'I Love Python\'\r\n\r\nresult = pattern.sub(func, string)\r\n\r\nprint(result)\r\n# I Love Python And Java\r\n```\r\n\r\n### 贪婪模式与非贪婪模式\r\n\r\n**贪婪匹配**:正则表达式一般趋向于最大长度匹配，也就是所谓的贪婪匹配。\u3000\r\n\r\n**非贪婪匹配**：就是匹配到结果就好，取最少的匹配字符。\r\n\r\n在Python中，默认是贪婪模式，而在正则表达式的量词后面直接加上一个问号？就会转换为非贪婪模式。\r\n\r\n```\r\nimport re\r\n\r\nstring = \'i am 18 ！\'\r\n\r\nresult1 = re.search(r\'\\d+\', string)\r\nresult2 = re.search(r\'\\d+?\', string)\r\n\r\nprint(result1.group())\r\n# 18\r\nprint(result2.group())\r\n# 1\r\n```\r\n\r\n在上述案例中的正则为\\d+，也就是匹配数字1次或多次。也就是说，在贪婪模式下，这个正则会往多的次数匹配，也就是优先多次，即匹配到了18，而非贪婪模式下，则会优先匹配1次，也就是优先匹配到了1，满足条件便会立刻返回结果。\r\n',
        'collection': 0,
        'a_flower': 0,
        'id': 19,
        'author_id': 6,
        'title': '正则表达式',
        'a_content': '<p><img src="https://upload-images.jianshu.io/upload_images/21642236-456737a42524076a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt=""></p>\r\n<h3 id="h3--"><a name="什么是正则表达式？" class="reference-link"></a><span class="header-link octicon octicon-link"></span>什么是正则表达式？</h3><p>正则表达式(Regular Expression)，又称规则表达式，通常被用来检索、替换那些符合某个模式(规则)的文本。许多程序设计语言都支持利用正则表达式进行字符串操作。</p>\r\n<p>Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。re 模块使 Python 语言拥有全部的正则表达式功能。</p>\r\n<p>正则表达式的使用对特殊字符进行了转义，所以如果我们要使用原始字符串，只需加一个 r 前缀。</p>\r\n<h3 id="h3-u5143u5B57u7B26"><a name="元字符" class="reference-link"></a><span class="header-link octicon octicon-link"></span>元字符</h3><p>正则表达式由一些普通字符和一些元字符（metacharacters）组成。普通字符包括大小写的字母和数字，而元字符则具有特殊的含义。下列为一些常见的元字符的使用说明。</p>\r\n<pre><code>匹配边界:\r\n    ^     匹配行首\r\n    $     匹配行尾\r\n\r\n重复次数:\r\n    ？    重复匹配0次或1次\r\n    *     重复匹配0次或更多次\r\n    +     重复匹配1次或更多次\r\n    {n}   重复n次\r\n    {n,}  重复n次或更多次\r\n    {n,m} 重复n~m次\r\n\r\n各种字符的表示:\r\n    .     匹配除了换行符以外的任意字符串\r\n    [a-z] 任意a-z的字母\r\n    [abc] a,b,c中任意字符\r\n    \\d    匹配数字\r\n    \\D    匹配任意非数字的字符\r\n    \\w    数字，字母，下划线\r\n    \\W    匹配任意不是字母，数字，下划线的字符\r\n    \\s    空白字符（回车，制表，空格）\r\n    \\S    匹配任意不是空白符的字符\r\n    \\b    单词的边界\r\n    \\B    匹配不是单词开始和结束的位置\r\n\r\n其他:\r\n    [^123abc] 匹配除了123abc这几个字符以外的任意字符\r\n    123|abc   匹配123或者abc\r\n</code></pre><h3 id="h3-pattern-"><a name="Pattern 对象" class="reference-link"></a><span class="header-link octicon octicon-link"></span>Pattern 对象</h3><p>compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 re 模块的查找方法使用。语法格式为：</p>\r\n<pre><code class="lang-python">pattern = re.compile(r&#39;正则表达式&#39;，&#39;匹配模式&#39;)\r\n\r\n# 常用的匹配模式:\r\n#   re.S    可以让 . 匹配换行符\r\n#   re.I    忽略大小写\r\n#   re.M    多行匹配，影响 ^ 和 $\r\n</code></pre>\r\n<h3 id="h3-u5355u6B21u5339u914D"><a name="单次匹配" class="reference-link"></a><span class="header-link octicon octicon-link"></span>单次匹配</h3><p>re 模块中，有两个方法，match 函数和 search 函数，这两个函数都是单次匹配，都返回一个<br>Match 对象。</p>\r\n<pre><code class="lang-python">re.match(pattern, string, start, end)\r\n# pattern.match(string, start, end)\r\n\r\nre.search(pattern, string, start, end)\r\n# pattern.match(string, start, end)\r\n\r\n# pattern  正则表达式对象\r\n# string   要匹配的目标字符串\r\n# start    要匹配的目标字符串的起始位置(可选)\r\n# end为    要匹配的目标字符串的结束位置(可选)\r\n\r\n&quot;&quot;&quot;案例&quot;&quot;&quot;\r\n\r\nimport re\r\n\r\npattern = re.compile(r&#39;\\w+&#39;, re.I)\r\n\r\nstring = &#39;I love python&#39;\r\n\r\nresult = pattern.match(string, 2, 6)\r\n\r\nprint(result)\r\n# &lt;re.Match object; span=(2, 6), match=&#39;love&#39;&gt;\r\n\r\nprint(result.group())\r\n# love\r\n</code></pre>\r\n<p>需要注意的是，match 函数 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，而 search 函数是匹配整个字符串，直到找到一个匹配。</p>\r\n<pre><code class="lang-python">import re\r\n\r\nstring = &#39;i am 18 !!!&#39;\r\n\r\nresult1 = re.match(r&#39;\\d+&#39;, string)\r\nresult2 = re.search(r&#39;\\d+&#39;, string)\r\n\r\nprint(result1)\r\n# None\r\nprint(result2.group())\r\n# 18\r\n</code></pre>\r\n<h3 id="h3-u5206u7EC4"><a name="分组" class="reference-link"></a><span class="header-link octicon octicon-link"></span>分组</h3><p>在Python中，正则表达式分组就是用一对圆括号“()”括起来的正则表达式，匹配出的内容就表示一个分组。即每个圆括号都是一个分组，从1开始。需要注意的是，有一个隐含的全局分组（就是0），也就是整个正则表达式。</p>\r\n<pre><code class="lang-python">import re\r\n\r\npattern = re.compile(r&#39;name is (.*),age:(\\d+)&#39;, re.I)\r\n\r\nstring = &#39;my name is 啊哈哈君,age:18 !&#39;\r\n\r\nresult = pattern.search(string)\r\n\r\nprint(result)\r\n# &lt;re.Match object; span=(3, 22), match=&#39;name is 啊哈哈君,age:18&#39;&gt;\r\nprint(result.group())\r\n# name is 啊哈哈君,age:18\r\nprint(result.group(1))\r\n# 啊哈哈君\r\nprint(result.group(2))\r\n# 18\r\n</code></pre>\r\n<h3 id="h3-match-"><a name="Match  对象" class="reference-link"></a><span class="header-link octicon octicon-link"></span>Match  对象</h3><p>关于match函数和search函数返回的match对象，也是有很多方法可以调用的。如上述案例的group函数，会返回被匹配的字符串。</p>\r\n<pre><code class="lang-python"># 返回被匹配的字符串，等价于group(0)\r\nMatch.group()  \r\n\r\n# 返回第n个分组匹配的字符串，如果组号不存在，则返回indexError异常\r\nMatch.group(n)\r\n\r\n# 返回组号为n到m组所匹配的字符串的元组，如果组号不存在，则返回indexError异常\r\nMatch.group(n,m) \r\n\r\n# 返回所有分组匹配的字符串的元组\r\nMatch.groups()\r\n\r\n# 返回匹配开始的位置\r\nMatch.start()\r\n\r\n# 返回匹配结束的位置\r\nMatch.end()\r\n\r\n# 返回一个元组包含匹配 (开始,结束) 的位置\r\nMatch.span()\r\n</code></pre>\r\n<h3 id="h3-u591Au6B21u5339u914D"><a name="多次匹配" class="reference-link"></a><span class="header-link octicon octicon-link"></span>多次匹配</h3><p>re 模块中的findall函数与finditer函数用于进行多次匹配。相信通过函数名，有些小伙伴就可以知道这两个函数的返回值。</p>\r\n<pre><code class="lang-python">import re\r\n\r\nstring = &#39;abcdefg&#39;\r\n\r\nresult1 = re.findall(r&#39;\\w&#39;, string)\r\nresult2 = re.finditer(r&#39;\\w&#39;, string)\r\n\r\nprint(result1)\r\n# [&#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;d&#39;, &#39;e&#39;, &#39;f&#39;, &#39;g&#39;]\r\nprint(result2)\r\n# &lt;callable_iterator object at 0x000002452F017848&gt;\r\n</code></pre>\r\n<p>由上述案例可看出，多次匹配与单次匹配的函数用法相同，也可以加start和end。只是findall函数返回的是一个列表，而finditer返回的是一个迭代器。</p>\r\n<h3 id="h3-u5206u5272u5B57u7B26u4E32"><a name="分割字符串" class="reference-link"></a><span class="header-link octicon octicon-link"></span>分割字符串</h3><p>re 模块提供了一个spilt函数，用于通过正则表达式分割字符串，并返回一个列表。</p>\r\n<pre><code>import re\r\n\r\npattern = re.compile(r&#39;\\s&#39;, re.I)\r\n\r\nstring = &#39;python java c++&#39;\r\n\r\nresult = pattern.split(string)\r\n\r\nprint(result)\r\n# [&#39;python&#39;, &#39;java&#39;, &#39;c++&#39;]\r\n</code></pre><h3 id="h3-u66FFu6362u5B57u7B26u4E32"><a name="替换字符串" class="reference-link"></a><span class="header-link octicon octicon-link"></span>替换字符串</h3><p>re 模块中的sub函数用于通过正则表达式替换字符串。格式为：</p>\r\n<pre><code class="lang-python">re.sub(pattern, repl, string, count)\r\n# pattern.sub(repl, string, count)\r\n\r\n# pattern  正则表达式或者正则对象\r\n# repl     替换的字符串，也可为一个函数\r\n# string   要被查找替换的原始字符串\r\n# count    匹配后替换的最大次数，默认为0，表示替换所有的匹配\r\n</code></pre>\r\n<p>这个函数通过案例是很容易理解的。</p>\r\n<pre><code>import re\r\n\r\npattern = re.compile(r&#39;python&#39;, re.I)\r\n\r\nstring = &#39;I Love Python, Python NB!&#39;\r\n\r\nresult1 = pattern.sub(&#39;java&#39;, string)\r\nresult2 = pattern.sub(&#39;java&#39;, string, 1)\r\n\r\nprint(result1)\r\n# I Love java, java NB!\r\nprint(result2)\r\n# I Love java, Python NB!\r\n</code></pre><p>当repl为函数时，函数的参数只能为match对象，并且这个函数必须有返回值，返回值的格式是字符串，将来就用这个字符串作为替换的内容。</p>\r\n<pre><code class="lang-python">import re\r\n\r\npattern = re.compile(r&#39;python&#39;, re.I)\r\n\r\n\r\ndef func(matched):\r\n    return matched.group()+&#39; And Java&#39;\r\n\r\n\r\nstring = &#39;I Love Python&#39;\r\n\r\nresult = pattern.sub(func, string)\r\n\r\nprint(result)\r\n# I Love Python And Java\r\n</code></pre>\r\n<h3 id="h3-u8D2Au5A6Au6A21u5F0Fu4E0Eu975Eu8D2Au5A6Au6A21u5F0F"><a name="贪婪模式与非贪婪模式" class="reference-link"></a><span class="header-link octicon octicon-link"></span>贪婪模式与非贪婪模式</h3><p><strong>贪婪匹配</strong>:正则表达式一般趋向于最大长度匹配，也就是所谓的贪婪匹配。\u3000</p>\r\n<p><strong>非贪婪匹配</strong>：就是匹配到结果就好，取最少的匹配字符。</p>\r\n<p>在Python中，默认是贪婪模式，而在正则表达式的量词后面直接加上一个问号？就会转换为非贪婪模式。</p>\r\n<pre><code>import re\r\n\r\nstring = &#39;i am 18 ！&#39;\r\n\r\nresult1 = re.search(r&#39;\\d+&#39;, string)\r\nresult2 = re.search(r&#39;\\d+?&#39;, string)\r\n\r\nprint(result1.group())\r\n# 18\r\nprint(result2.group())\r\n# 1\r\n</code></pre><p>在上述案例中的正则为\\d+，也就是匹配数字1次或多次。也就是说，在贪婪模式下，这个正则会往多的次数匹配，也就是优先多次，即匹配到了18，而非贪婪模式下，则会优先匹配1次，也就是优先匹配到了1，满足条件便会立刻返回结果。</p>\r\n',
        'good': 0,
        'a_time': '2020-09-09T14:15:45'
    }
}

dsl2 = {
    'query': {
        "match_all": {}
    }
}

dsl3 = {
    'query': {
        'bool': {
            'must': [
                {
                    'match': {
                        'title': 'python'
                    }
                },
                {
                    'match': {
                        'author_id': 6
                    }
                }
            ]
        }
    },
    "sort": {
        "good": {                 # 根据age字段升序排序
            "order": "asc"       # asc升序，desc降序
        }
    },
    'size': 4
}

# s = es.update(index='blogs', id='19', doc_type='politics', body=dsl1, ignore=400)

# s = es.delete(index='blogs', doc_type='politics', id='23')
#
res = es.search(index='blogs', doc_type='politics', body=dsl3)

# print(s)
# print(res)
