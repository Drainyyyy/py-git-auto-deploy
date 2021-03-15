# -*- coding: utf-8 -*-

#  Covered by The MIT License (MIT)
#
#  Copyright 2021 Drainyyy
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
#  (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge,
#  publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
#  subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
#  WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
#  CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

__all__ = ["Deployer"]


class Deployer:
    def __init__(self, port: int, secret: str):
        """TODO docs

        :param secret:
        """

        self.port = port
        self.secret = secret

    def start(self):
        print("Starting up flask server.")
        print("The IP address you need to enter in the GitHub webhook is: ")  # TODO flask server; Show IP-Address
        pass
