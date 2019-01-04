#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique
import re

path = './data_light.json'

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path) as f:
    data = json.load(f)

data=[value['job-name'] for value in data]


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов 

@print_result
def f1(arg):

    return list( unique(arg) )


@print_result
def f2(arg):
    return filter(lambda x: re.search('программист',x ),arg )


@print_result
def f3(arg):
    return list(map(lambda x: x+' с опытом Python',arg ))


@print_result
def f4(arg):
    beg=100000 
    end=200000
    salarys=list(gen_random(beg,end,len(arg)))
    return list(zip(salarys,arg)) 


with timer():
    f4(f3(f2(f1(data))))
