#!/usr/bin/python
# -*- coding: utf-8 -*-
#局部函数（函数作用域）

def demo1():

    def demo1_1():
        print("demo1_1")
        return

    print("demo1")
    demo1_1()

    return

demo1()
#demo1_1()
