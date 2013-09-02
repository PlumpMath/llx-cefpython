import ctypes, os

package_dir = os.path.dirname(os.path.abspath(__file__))

# This loads the libcef.so library for the main python executable.
libcef_so = os.path.join(package_dir, "libcef.so")
ctypes.CDLL(libcef_so, ctypes.RTLD_GLOBAL)
# Other .so libraries may also be required
libffmpegsumo_so = os.path.join(package_dir, "libffmpegsumo.so")
ctypes.CDLL(libffmpegsumo_so, ctypes.RTLD_GLOBAL)

# This loads the libcef.so library for the subprocess executable.
os.environ["LD_LIBRARY_PATH"] = package_dir

import sys
if 0x02070000 <=  sys.hexversion < 0x03000000:
    from . import cefpython_py27 as cefpython
else:
    raise Exception("Unsupported python version: " + sys.version)

__version__ = "27.2"
__author__ = "The CEF Python authors"
