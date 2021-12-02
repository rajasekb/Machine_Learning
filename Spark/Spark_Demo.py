from pyspark import SparkConf,SparkContext
# demo
conf = SparkConf().\
    setMaster("local").\
    setAppName("Daily_Revenue")
sc = SparkContext(conf=conf)
orders = sc.textFile("C:\\Users\\Lenovo\\Desktop\\Orders.txt")
print(str(orders.count()))
