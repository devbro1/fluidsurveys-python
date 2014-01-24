import os
import sys



try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt')
install_requires = [str(ir.req) for ir in install_reqs]

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

requests = 'requests >= 0.8.8'
if sys.version_info < (2, 6):
    requests += ', < 0.10.1'



sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'fluidsurveys'))
from fluidsurveys.version import VERSION

# Get simplejson if we don't already have json
if sys.version_info < (3, 0):
    try:
        from util import json
    except ImportError:
        install_requires.append('simplejson')

setup(name='fluidsurveys',
      cmdclass={'build_py': build_py},
      version=VERSION,
      description='Fluidsurvey python bindings',
      author='Fluidware',
      author_email='support@fluidware.com',
      url='https://github.com/fluidware/fluidsurveys-python.git',
      packages=['fluidsurveys', 'fluidsurveys.tests'],
      install_requires=install_requires,
      test_suite='fluidsurveys.test.all',
      use_2to3 = True,
      )