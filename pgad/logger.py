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

import logging
import logging.config
import typing

__all__ = ["Logging"]


class Logging:
    def __init__(self, config: typing.Union[str, dict] = None, level: int = 60, filename: str = None):
        """Logging object for logging application data to the console and possibly to a file (if filename is given).

        See Logging().logger() for more information.

        :param config: Config file/dict after https://docs.python.org/3/library/logging.config.html#logging.config (default: None)
        :type config: str, dict
        :param level: Logging level after https://docs.python.org/3/library/logging.html#logging-levels (default: 60 -> Nothing is logged)
        :type level: int
        :param filename: Filename of log file (default: None -> No log file)
        :type filename: str
        """

        self._logger = logging.getLogger("py-git-auto-deploy")
        self._config = config
        self._level = level
        self._filename = filename
        self.formatter = logging.Formatter("[%(asctime)s] [%(filename)s:%(lineno)d-%(funcName)s] %(levelname)s > %(message)s", "%Y-%m-%d %H:%M:%S")

    @property
    def config(self) -> str:
        return self._config

    @property
    def level(self) -> int:
        return self._level

    @property
    def filename(self) -> str:
        return self._filename

    def logger(self) -> logging.Logger:
        """Create StreamHandler and FileHandler for logger. If config file/dict is given, it will be used instead.

        :return: Logger (type: logging.Logger)
        """

        if self.config:  # If a config file/dict exists, they will be used instead of the pre-configured logger.
            if isinstance(self._config, str):
                logging.config.fileConfig(self._config, disable_existing_loggers=False)
            else:
                logging.config.dictConfig(self._config)

        sh = logging.StreamHandler()
        sh.setFormatter(self.formatter)
        self._logger.addHandler(sh)

        if self.filename:
            fh = logging.FileHandler(f"{self.filename}")
            fh.setFormatter(self.formatter)
            self._logger.addHandler(fh)

        self._logger.setLevel(self.level)
        return self._logger
