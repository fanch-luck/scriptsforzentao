#!usr/bin/env python
# -*- coding:utf-8 -*-
# -----------------------------------------------------------
# File Name: zentaoconnection
# Author:    fan20200225
# Date:      2020/12/27 0027
# -----------------------------------------------------------

import hashlib
import json
import sys
import requests


class ZentaoConnection(object):
    def __init__(self, account, password):
        self.account = account
        self.password = password
        self.header = dict()

    def calc_md5(self, string):
        _md5 = hashlib.md5()
        _md5.update(string.encode("utf-8"))
        return _md5.hexdigest()

    def


if __name__ == "__main__":
    zt = ZentaoConnection("fanchunhui", "fanchun!@#")
    print(zt.calc_md5("fanchun!@#"))