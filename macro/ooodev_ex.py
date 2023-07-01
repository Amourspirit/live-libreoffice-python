from __future__ import annotations
from typing import TYPE_CHECKING, cast
from ooodev.utils.lo import Lo
from ooodev.office.write import Write
from ooodev.utils.color import StandardColor
from ooodev.format.writer.direct.char.font import Font
from ooodev.dialog.msgbox import MsgBox, MessageBoxButtonsEnum, MessageBoxType
from ooodev.format.writer.direct.para.alignment import Alignment

if TYPE_CHECKING:
    from com.sun.star.script.provider import XScriptContext

    XSCRIPTCONTEXT = cast(XScriptContext, None)

# OooDev framework needs to be initialized when being used in a macro.
# This can be done by accessing the this_component property or Lo.XSCRIPTCONTEXT
_ = Lo.this_component


def show_hello(*args) -> None:
    """
    Displays a message box for Hello World
    """
    _ = MsgBox.msgbox("Hello World!", "HI", boxtype=MessageBoxType.INFOBOX, buttons=MessageBoxButtonsEnum.BUTTONS_OK)


def write_hello(*args) -> None:
    """
    Writes Hello World in Bold to a writer document.

    If not a Writer document then a error message is displayed.

    Returns:
        None:
    """
    # for more on formatting Writer documents see,
    # https://python-ooo-dev-tools.readthedocs.io/en/latest/help/writer/format/index.html
    try:
        # cursor = Write.get_cursor(Write.active_doc)
        cursor = Write.get_cursor(XSCRIPTCONTEXT.getDocument())  # type: ignore
        cursor.gotoEnd(False)
        al = Alignment().align_center
        ft = Font(size=36, u=True, b=True, color=StandardColor.GREEN_DARK2)
        Write.append_para(cursor=cursor, text="Hello World!", styles=[ft, al])
    except Exception as e:
        _ = MsgBox.msgbox(f"This method requires a Writer document.\n{e}")


g_exportedScripts = (show_hello, write_hello)
