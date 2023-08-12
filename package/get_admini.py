def main():
    import ctypes
    import sys

    if ctypes.windll.shell32.IsUserAnAdmin():
        return
    else:
        ret = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
        if ret <= 32:
            raise Exception("无法以管理员身份运行脚本")
        sys.exit()