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
import json
import click
from pipetree import __version__ as pipetree_version
from pipetree.templates import DEFAULT_CONFIG


@click.group()
@click.version_option(version=pipetree_version, message='%(prog)s %(version)s')
@click.option('--debug/--no-debug', default=False,
              help='Write debug logs to standard error.')
@click.option('--project_dir', help='The project directory. '
              'Defaults to the current directory.')
@click.pass_context
def cli(ctx, project_dir, debug=False):
    if project_dir is None:
        project_dir = os.getcwd()
    ctx.obj['project_dir'] = project_dir
    ctx.obj['debug'] = debug


@cli.command()
@click.argument('project_name', required=True)
@click.pass_context
def init(ctx, project_name):
    if os.path.isdir(project_name):
        click.echo('Already a directory named: %s' % project_name)
        raise click.Abort()
    pipetree_dir = os.path.join(project_name, '.pipetree')
    config = os.path.join(pipetree_dir, 'config.json')
    os.makedirs(pipetree_dir)
    with open(config, 'w') as f:
        f.write(DEFAULT_CONFIG % project_name)
    click.echo("Created new project %s" %project_name)


def main():
    cli(obj={})
