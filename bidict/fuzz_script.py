#!/usr/bin/env python

import ast
import sys
import bidict


def main():
    s = sys.stdin.read().strip()
    print repr(s)
    b = bidict.bidict()
    # each line attempts to manipulate the `b` object
    for line in s.splitlines():
        print
        print repr(line)
        # we need a verb
        # use partition as there may be no spaces
        cmd, _, arg_str = line.partition(' ')
        if arg_str:
            try:
                # need to convert the remaining inoput string into a Python
                # object but we can't let a fuzzer loose on the built-in eval
                # as it could find a way to destroy the host OS.
                # so use literal_eval which will only resolve built-in data
                # types
                args = ast.literal_eval(arg_str)
            # it's hard to know all the possible exceptions types here.
            # we're not intending to fuzz literal_eval for unexpected
            # exceptions anyway
            except:
                args = ()
        else:
            args = ()
        if not isinstance(args, (list, tuple, set)):
            args = (args,)
        if hasattr(b, cmd):
            method = getattr(b, cmd)
            print method, args
            try:
                res = method(*args)
                print 'res', res
            # we may not meet the argspec of the method
            except TypeError as e:
                print e
        else:
            print 'no attr', b, cmd


if __name__ == '__main__':
    import afl
    afl.start()
    main()
