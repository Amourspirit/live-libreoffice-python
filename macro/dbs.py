import debugpy

debugpy.listen(8550)
debugpy.wait_for_client()  # blocks execution until client is attached
print("Debug Proceeding ...")

import importlib
from macro import ooodev_ex


def mod():
    return ooodev_ex


def rl():
    importlib.reload(ooodev_ex)


# make sure this is not run as macro in LibreOffice
g_exportedScripts = ()
