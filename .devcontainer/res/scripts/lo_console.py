#!/usr/bin/env python3
import code
import rlcompleter
import readline
from os import getenv

try:
    import psutil
except ImportError:
    print("psutil is not installed. Please install it with 'poetry add --group=dev psutil'")
    SystemExit(1)

try:
    from ooodev.utils.lo import Lo
except ImportError:
    print("ooodev is not installed. Please install it with 'poetry add --group=dev ooodev'")
    SystemExit(1)

from ooodev.conn.connectors import ConnectSocket


def check_if_process_running(process_name: str) -> bool:
    """
    Check if there is any running process that contains the given name process_name.
    """
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


lo_port = int(getenv("LO_CONN_PORT", 2002))
variables = globals().copy()
variables.update(locals())
if check_if_process_running("soffice.bin"):
    _ = Lo.load_office(connector=ConnectSocket(host="localhost", port=lo_port, start_office=False))
else:
    _ = Lo.load_office(
        connector=ConnectSocket(host="localhost", port=lo_port, start_office=True, invisible=False, headless=False)
    )
variables["XSCRIPTCONTEXT"] = Lo.XSCRIPTCONTEXT

# https://stackoverflow.com/questions/50917938/enabling-console-features-with-code-interact
readline.set_completer(rlcompleter.Completer(variables).complete)
readline.parse_and_bind("tab: complete")


shell = code.InteractiveConsole(variables)
shell.interact()
