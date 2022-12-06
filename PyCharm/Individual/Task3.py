#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word = "Привет"

    word = word.replace(word[2], "")
    print(f"Слово с удалённой третьей буквой: {word}")

    k = int(input("Введите номер буквы, которую нужно удалить: "))
    if k <= len(word):
        word = word.replace(word[k-1], "")
        print(f"Слово с удалённой буквой под номером {k}: {word}")
    else:
        print("В слове нет буквы с таким номером")
