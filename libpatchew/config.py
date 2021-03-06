#!/usr/bin/env python2
#
# The MIT License (MIT)
#
# Copyright (c) 2014 Fam Zheng <fam@euphon.net>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import ConfigParser

_config = ConfigParser.ConfigParser()

def load_config(*try_files):
    for f in try_files:
        print f
        try:
            if _config.read(f):
                return True
        except:
            pass
        continue
    return False

def _value(r):
    if r.upper() in ["TRUE", "FALSE", "YES", "NO"]:
        return r.upper() in ["TRUE", "YES"]
    try:
        if r == str(int(r)):
            return int(r)
    except:
        return r

def get(section, key, default=None):
    """ Return int if value in digits;
        bool if in "yes", "no", "true" or "false";
        otherwise a string;
        list of value if "," is found"""
    try:
        r = _config.get(section, key)
    except:
        r = None
    if not r:
        return default
    elif "," in r:
        return [_value(x) for x in r.split(",")]
    else:
        return _value(r)

def items(section):
    return _config.items(section)
