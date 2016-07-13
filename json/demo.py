#!/usr/bin/env python

import sys
import json


def main():
    s = sys.stdin.read()
    try:
        json.loads(s)
    except ValueError as e:
        # we expect malformed input to cause ValueErrors
        # any other exception or crash is interesting
        print repr(e)


if __name__ == '__main__':
    import afl
    afl.start()
    main()
