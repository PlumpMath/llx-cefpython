from distutils.core import setup

setup(
    name='cefpython3', # No spaces here, so that it works with deb packages.
    version='27.2',
    description='Python bindings for the Chromium Embedded Framework',
    license='BSD 3-Clause',
    author='Czarek Tomczak',
    author_email='czarek.tomczak@gmail.com',
    url='http://code.google.com/p/cefpython/',
    packages=['cefpython3', 'cefpython3.wx'],
    package_data={'cefpython3': [
        'examples/*.py',
        'examples/*.html',
        'examples/wx/*.py',
        'examples/wx/*.html',
        'examples/wx/*.png',
        'locales/*.pak',
        'wx/*.txt',
        'wx/images/*.png',
        '*.txt',
        'cefclient',
        'subprocess',
        '*.so',
        '*.pak',
    ]}
)

# ------------------------------------------------------------------------------
# Chmod +x the subprocess and cefclient executables.
# ------------------------------------------------------------------------------

import sys
import os
import subprocess

# Import the cefpython3 module from dist-packages/ directory.
# We do not want to import from the local "cefpython3" directory.
del sys.path[0]
sys.path.append('')
import cefpython3

package_dir = os.path.dirname(cefpython3.__file__)
# Make sure this is not a local package imported.
assert not package_dir.startswith(os.path.dirname(os.path.abspath(__file__)))

subprocess_exe = os.path.join(package_dir, "subprocess")
cefclient_exe = os.path.join(package_dir, "cefclient")

print("chmod +x " + subprocess_exe)
subprocess.call("chmod +x "+subprocess_exe, shell=True)

print("chmod +x " + cefclient_exe)
subprocess.call("chmod +x "+cefclient_exe, shell=True)
