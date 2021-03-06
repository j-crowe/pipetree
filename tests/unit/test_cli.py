# MIT License

# Copyright (c) 2016 Morgan McDermott & John Carlyle

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import click
import unittest
from click.testing import CliRunner
from pipetree.cli import cli
from pipetree.cli.utils import _get_config_path


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.dirname = 'foo'
        self.runner = CliRunner()
        self.fs = self.runner.isolated_filesystem()
        self.fs.__enter__()
        self.runner.invoke(cli, ['init', self.dirname])

    def tearDown(self):
        self.fs.__exit__(None, None, None)

    def test_get_config_path(self):
        ctx = click.Context(click.Command('cli'))
        ctx.obj = {'project_dir': 'foo/bar/baz/'}
        path = _get_config_path(ctx)
        self.assertEqual(path, 'foo/bar/baz/.pipetree/config.json')
