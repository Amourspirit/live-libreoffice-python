from __future__ import annotations
import uno
from ooodev.utils.lo import Lo
from ooodev.office.calc import Calc
from ooodev.utils.gui import GUI


def main():
    _ = Lo.load_office(Lo.ConnectSocket())
    doc = Calc.create_doc()
    try:
        GUI.set_visible()
        Lo.delay(3_000)
    finally:
        Lo.close_doc(doc)


if __name__ == "__main__":
    main()
