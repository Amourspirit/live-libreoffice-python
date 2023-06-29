from ooodev.utils.lo import Lo
from ooodev.office.write import Write
from ooodev.utils.color import StandardColor
from ooodev.format.writer.direct.char.font import Font
from ooodev.dialog.msgbox import MsgBox, MessageBoxButtonsEnum, MessageBoxType

# OooDev framwork needs to be initialized when being used in a macro.
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
    """
    try:
        cursor = Write.get_cursor(Write.active_doc)
        cursor.gotoEnd(False)
        ft = Font(size=24, b=True, color=StandardColor.GREEN_DARK2)
        Write.append_para(cursor=cursor, text="Hello World!", styles=[ft])
    except Exception as e:
        _ = MsgBox.msgbox(f"This method requires a Writer documnet.\n{e}")


g_exportedScripts = (show_hello, write_hello)
