#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if len(sentence) < 0:
        return None
    else:
        first = sentence[0]
    return size, first
