#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = "Сегодня       прекрасная    погода !"
    count = 0
    max_count = 0

    for i, char in enumerate(s):
        if s[i] == ' ':
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0

    print(f"Максимальное количество пробелов: {max_count}")
