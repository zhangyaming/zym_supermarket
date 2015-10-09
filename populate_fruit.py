# coding=utf-8
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mydeb_3.settings')

import django
django.setup()

from fruit.models import *

def add_person(name):
	c = Person.objects.get_or_create(name = name)[0]
	return c


def add_case(name):
	c = Case.objects.get_or_create(name = name)[0]
	return c

def add_goods(case, name, price):
	c = Goods.objects.get_or_create(case = case, name = name, price = price)


def populate():
	add_person(name = '张亚明')
	add_person(name = '郝鹏')
	add_person(name = '陈旭')
	add_person(name = '周伦浩')

	fruit_case = add_case(name = '水果')
	add_goods(case = fruit_case, name = '苹果', price = 10)
	add_goods(case = fruit_case, name = '香蕉', price = 20)
	add_goods(case = fruit_case, name = '桃子', price = 50)
	add_goods(case = fruit_case, name = '榴莲', price = 100)

	vega_case = add_case(name = '蔬菜')
	add_goods(case = vega_case, name = '黄瓜', price = 5)
	add_goods(case = vega_case, name = '番茄', price = 8)
	add_goods(case = vega_case, name = '茄子', price = 2)

	snack_case = add_case(name = '零食')
	add_goods(case = snack_case, name = '士力架', price = 4)
	add_goods(case = snack_case, name = '老婆饼', price = 10)
	add_goods(case = snack_case, name = '怪味豆', price = 12)

if __name__ == '__main__':
	print "Starting fruit population script..."
	populate()


