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
import unittest
from pipetree.loaders import _append_json_ext
from pipetree.loaders import PipelineConfigLoader


class TestLoaders(unittest.TestCase):
    def test_json_paths(self):
        path = '/root/user/stuff/file'
        self.assertEqual(_append_json_ext(path),
                         path + '.json')

    def test_json_paths2(self):
        path = 'file.json'
        self.assertEqual(_append_json_ext(path), path)

    def test_load_with_custom_loader(self):
        def load_file(self, path):
            return {'key': {
                'type': 'LocalDirectoryPipelineStage',
                'meta': 'baz'
            }}

        cls = type('Foo', (object,), {
            'load_file': load_file
        })()
        loader = PipelineConfigLoader(file_loader=cls)
        configs = loader.load_file('foo')
        for config in configs:
            self.assertEqual(config.name, 'key')
            self.assertEqual(config.type, 'LocalDirectoryPipelineStage')
            self.assertEqual(config.meta, 'baz')
