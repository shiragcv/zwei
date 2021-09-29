# -*- coding: utf-8 -*-

import utils


metadata = utils.get_metadata('setup.cfg')

name = metadata.get('name')

version = metadata.get('version')

description = metadata.get('version') or ''

build_command = 'pip install --target={install_path} {root}'

def commands():
    env.PYTHONPATH.append('{root}')
