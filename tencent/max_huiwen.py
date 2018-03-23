# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180323
    Last Modified Person: HZT
    Last Modified Date: 20180323
    Last Modified Thing: 创建文件
'''
'''
题目描述:
给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？
输出需要删除的字符个数。

输入描述:
输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000.
输出描述:
对于每组数据，输出一个整数，代表最少需要删除的字符个数。

示例1
输入
abcda
google
输出
2
2
'''


def maxlcp(input_str, fan_str, x, y):
    # 求出输入字符串和其反序字符串的最大公共子序列
    if (not input_str) or len(input_str) == 0 or (
            not fan_str) or len(fan_str) == 0:
        return 0
    if x < 0 or y < 0:
        return 0

    lcp_len = 0
    if (input_str[x] == fan_str[y]):
        lcp_len = maxlcp(input_str, fan_str, x - 1, y - 1) + 1
    else:
        lcp_len = max(
            maxlcp(input_str, fan_str, x - 1, y),
            maxlcp(input_str, fan_str, x, y - 1))

    # print("---debug input_str[:x]", input_str[:x + 1], x)
    # print("---debug fan_str[:y]", fan_str[:y + 1], y)
    return lcp_len


if __name__ == '__main__':
    while True:
        input_str = input()
        if not input_str:
            break
        lens = len(input_str)
        fan_str = input_str[::-1]
        maxlcp_len = maxlcp(input_str, fan_str, lens - 1,
                            lens - 1)  # 求出的最大公共子序列的长度
        print(lens - maxlcp_len)
