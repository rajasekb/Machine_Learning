from pyspark import SparkConf,SparkContext
import configparser as cp
import sys

props = cp.RawConfigParser()
props.read("Machie_Learning/Resources/application.properties")

#C:\Users\Lenovo\PycharmProjects\Machine_Learning\Resources\application.properties

env = sys.argv[1]

conf = SparkConf().\
    setMaster(props.get(env,'executionMode')).\
    setAppName("Daily_Revenue")

sc = SparkContext(conf=conf)

orders = sc.textFile(props.get(env ,'input.base.dir' ) +"/part-00000")
print(str(orders.count()))
