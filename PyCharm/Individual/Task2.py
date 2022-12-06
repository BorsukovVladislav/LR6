#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = "Доброе утро, товарищ"

    if 'а' in s:
        print(f"Порядковый номер первой буквы а: {s.find('а') + 1}")
    else:
        print("В предложении нет буквы а")