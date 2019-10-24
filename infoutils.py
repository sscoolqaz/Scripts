"""
Module contains untilies to get information on programs on Windows
"""
import ctypes

#Module contains untilies to get information on certain programs on Windows

if __name__ == "__main__":
    import sys
    PID = getpid(sys.argv[1:])
    print(PID)


#Function is a modified version of https://sjohannes.wordpress.com/2012/03/23/win32-python-getting-all-window-titles/

def getpid(*WindowTitle):

    """
    This function prints out the Process ID on a windows computer\n
    The arguments for this have to be a string\n
    The CLI arguments have to be in quotes\n
    """

    #Used to hook into the functions
    EnumWindows = ctypes.windll.user32.EnumWindows
    GetWindowThreadProcessId = ctypes.windll.user32.GetWindowThreadProcessId

    #sets up the callback function EnumWindowsProc so that we can use it to actually get the Windows ProcessID's from the callback
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

    #hooks into the functions
    #these are used to get the buffers needed to process
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW

    #creates a dword type pointer because
    p_id = ctypes.pointer(ctypes.c_ulong(0))
    #creates a dictionaru of Window Titles with their Process ID's
    TitlesList = {}

    def foreach_window(hwnd, lParam):

        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowThreadProcessId(hwnd, p_id)
        GetWindowText(hwnd, buff, length + 1)
        TitlesList[buff.value] = p_id.contents.value

        #has to return true to keep enumerating
        return True


    EnumWindows(EnumWindowsProc(foreach_window), 0)

    #
    for title in WindowTitle:
        return(TitlesList[title])