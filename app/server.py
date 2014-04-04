#!/usr/bin/env python
# Copyright (C) 2014 Linaro Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""The Tornado application base module."""

import pymongo
import tornado

from concurrent.futures import ThreadPoolExecutor
from tornado.web import Application

from handlers.app import AppHandler
from urls import APP_URLS


class KernelCiBackend(Application):
    """The Kernel CI backend application.

    Where everything starts.
    """

    mongodb_client = pymongo.MongoClient()

    def __init__(self):

        settings = {
            'client': self.mongodb_client,
            'default_handler_class': AppHandler,
            'executor': ThreadPoolExecutor(max_workers=10),
        }

        super(KernelCiBackend, self).__init__(APP_URLS, **settings)


if __name__ == '__main__':
    KernelCiBackend().listen(8888)
    tornado.ioloop.IOLoop.instance().start()
