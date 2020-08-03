import io
import subprocess
from datetime import datetime, timezone

import setuptools


def get_version():
    result = subprocess.run(['git', 'show', '-s', '--format=%ct', 'HEAD'], stdout=subprocess.PIPE)
    committed_date = datetime.fromtimestamp(int(result.stdout)).astimezone(timezone.utc)
    committed_date_str = committed_date.strftime('%Y%m%d%H%M%S')
    return f'1.5.2b{committed_date_str}'


setuptools.setup(
    name='e2e.pca-jsonpath-ng',
    version=get_version(),
    description=(
        'Fork from https://github.com/jsonpath-ng v1.5.1 to fix filtering with None'
    ),
    author='Tomas Aparicio',
    author_email='tomas@aparicio.me',
    url='https://github.com/trilogy-group/jsonpath-ng',
    license='Apache 2.0',
    long_description=io.open('README.rst', encoding='utf-8').read(),
    packages=['jsonpath_ng', 'jsonpath_ng.bin', 'jsonpath_ng.ext'],
    entry_points={
        'console_scripts': [
            'jsonpath_ng=jsonpath_ng.bin.jsonpath:entry_point'
        ],
    },
    test_suite='tests',
    install_requires=[
        'ply', 'decorator', 'six'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
	'Programming Language :: Python :: 3.7',
	'Programming Language :: Python :: 3.8',
    ],
)
