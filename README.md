# afl fuzzing demos
Fuzzing things with [afl](http://lcamtuf.coredump.cx/afl/) and [python-afl](https://bitbucket.org/jwilk/python-afl/overview)

## Installing Fuzzing Tools

- create a working directory and virtual env
- afl
    - [Download](http://lcamtuf.coredump.cx/afl/releases/afl-latest.tgz) and unpack from http://lcamtuf.coredump.cx/afl/
    - follow instructions in [docs/INSTALL](https://github.com/mcarpenter/afl/blob/master/docs/INSTALL)
- python-afl
    - https://bitbucket.org/jwilk/python-afl/overview
    - `hg clone ...` and `pip install -e python-afl/`

## Fuzzing Python's JSON library

- [json fuzzing example](https://github.com/tomviner/afl-fuzzing-demos/blob/master/json)
