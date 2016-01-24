# toytools
interesting little tools

job_spider
------------
A spider for job title and description in the freelancer websites Upwork

This sample only takes jobs in Web, Mobile & Software Dev department

MongoDB is used, in order to test you have to set your Mongodb service up

Basic setting is in runSpider.py

Step 1:
 set the settings in runSpider.py and run a Mongodb service
 
Step 2:
 run runSpider.py, this will crawl the pages and save data in database

Step 3:
 run dataProcess.py, this will process the data in database and produce a bar chart on the hottest skill key words in Upwork

A sample output is like this:

![image](https://github.com/YunruL/toytools/blob/master/job_spider/figure_1.png)


nonsense:
------------
A chinese version of this blog:
http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/

Produce meaningless sentences using markov chain model

通过马尔可夫模型生成一段毫无意义的中文，news.txt为示例语料库，可以改为任何自己喜欢的语料库。

chainLen=4 的一段例文：

“零售额55387亿元，比下降3.3%。从城乡村币（M1）余额2458495个乡结构看，其中住宅新理
念指导新宏观谷物商品网上涨1.0%，12月份，制造业增长7.6%。八届三产量2999亿元，衣着
上年名义增长5.9%。分经济工业产投资增1.8%。场销率为64.2%，”
