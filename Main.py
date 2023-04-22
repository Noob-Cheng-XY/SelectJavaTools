from __future__ import print_function


class SetJavaVersion:
    def __init__(self) -> None:
        # 初始化

        import os
        import json
        # 导入模块

        self.JavaList = {}
        self.JavaVersionList = {}
        self.AppData = f"{os.environ.get('Appdata')}\\SetJavaVersion"
        self.Temp = f"{os.environ.get('Temp')}\\SetJavaVersion"
        self.CommandList = ["help", "add", "remove", "reset"]
        self.Backup = f"{self.AppData}\\Backup"
        # 设置可能需要用到的全局变量

        self.admini()  # 检测是否以管理员身份运行
        find_java_list = self.find_java() # 搜索Java

        print("欢迎使用Java切换器!")

        if not os.path.exists(self.AppData):  # 判断是否存在配置文件夹
            os.makedirs(self.AppData, exist_ok=True)
            os.makedirs(self.Backup, exist_ok=True)
            self.First = True
            self.first_start()
            # 不存在，创建目录并开始配置
        else:
            # 存在，判断配置文件是否存在
            if not os.path.exists(f"{self.AppData}\\JavaPath.json"):
                with open(f"{self.AppData}\\JavaPath.json", "w") as f1:
                    self.JavaList = json.load(f1, strict=False)
                self.first_start()
                # 不存在，创建文件并开始配置
            else:
                with open(f"{self.AppData}\\JavaPath.json", "w", encoding="utf-8") as f1:
                    pass
                if self.JavaList == {}:
                    print("配置文件已丢失, 请重新配置")
                    self.first_start()
                else:
                    self.setting_java_version()

    def find_java(self):
        import os
        find_java_list = {}
        java_version = None

        for i in range(65, 91):
            if not os.path.exists(f"{chr(i)}:"):
                continue
            p64 = f"{chr(i)}:\\Program Files\\Java"
            p32 = f"{chr(i)}:\\Program Files (x86)\\Java"
            if os.path.exists(p64):
                for j in os.listdir(p64):
                    if os.path.exists(f"{p64}\\{j}\\bin"):
                        if "javac.exe" in os.listdir(f"{p64}\\{j}\\bin"):
                            attribute = "JDK"
                        else:
                            attribute = "JRE"
                    else:
                        continue
                    try:
                        with open(f"{p64}\\{j}\\release") as f1:
                            t1 = f1.readlines()
                        for k in t1:
                            if "JAVA_VERSION" in k and "JAVA_VERSION_DATE" not in k:
                                java_version = k[13:].strip().replace("\"", "")
                    except (FileNotFoundError, IOError):
                        java_version = None
                    t2 = len(find_java_list)
                    find_java_list[f"f_{t2 + 1}"] = {"name": None, "path": f"{p64}\\{j}\\bin", "version": java_version,"attribute": attribute}
            if os.path.exists(p32):
                for j in os.listdir(p32):
                    if os.path.exists(f"{p32}\\{j}\\bin"):
                        if "javac.exe" in os.listdir(f"{p32}\\{j}\\bin"):
                            attribute = "JDK"
                        else:
                            attribute = "JRE"
                    else:
                        continue
                    try:
                        with open(f"{p64}\\{j}\\release") as f1:
                            t1 = f1.readlines()
                        for k in t1:
                            if "JAVA_VERSION" in k and "JAVA_VERSION_DATE" not in k:
                                java_version = k[13:].strip().replace("\"", "")
                    except (FileNotFoundError, IOError):
                        java_version = None
                    t2 = len(find_java_list)
                    find_java_list[f"find_{t2 + 1}"] = {"name": None, "path": f"{p32}\\{j}\\bin", "version": java_version, "attribute": attribute}
        return find_java_list

    def admini(self):
        import ctypes
        import sys
        if ctypes.windll.shell32.IsUserAnAdmin():
            return
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

    def new_input(self, values, now_mode=None):
        out = input(values)
        if out == "help":
            if now_mode != "help":
                self.help()
            else:
                print("你已经在该模式中")
        elif out == "add":
            if now_mode != "add":
                self.add()
            else:
                print("你已经在该模式中")
        elif out == "remove":
            if now_mode != "remove":
                self.remove()
            else:
                print("你已经在该模式中")
        elif out == "reset":
            if now_mode != "reset":
                self.reset()
            else:
                print("你已经在该模式中")
        else:
            return out

    def help(self):
        print("""
帮助文档
    常用指令:
        1. help
        打开帮助文档
        2. add
        打开 [添加新的Java] 面板
        3. remove
        打开 [移除一个Java] 面板
        4. reset
        移除所有该程序修改过的系统变量(不包括JAVA_HOME)

    Java路径保存位置: 
        %AppData%\\SetJavaVersion

声明: 该程序由程虚员制作, 使用程序或源码时请开源
            """)

    def add(self):

        import json
        import os

        if not self.First:
            os.system("cls")

        n1 = self.new_input("请问你要添加多少个Java: ", "add")

        for i in range(int(n1)):
            java_name = self.new_input(f"请输入您要导入的第{i + 1}个Java版本名(自定义, 啥都行): ")
            java_path = self.new_input(f"请输入您要导入的第{i + 1}个Java目录: ")
            self.JavaList[java_name] = java_path
        with open(f"{self.AppData}\\JavaPath.json", "w+", encoding="utf-8") as f1:
            json.dump(self.JavaList, f1, indent=4)

    def remove(self):
        import os

        os.system("cls")
        print("开发中, 敬请期待,")

    def reset(self):
        import os

        os.system("cls")
        print("开发中, 敬请期待,")

    def first_start(self):
        self.First = True
        self.add()
        self.setting_java_version()

    def get_now_java(self):
        import os
        if os.environ.get("JAVA_HOME") is not None:
            now_java_path = os.environ.get("JAVA_HOME")
        else:
            print("当前JAVA变量不正常, 请立即更换!")
            return
        t1 = 0
        for i in self.JavaList:
            if self.JavaList[i]["java_name"] == now_java_path:
                print(f"当前Java为{i}, 位于{now_java_path}")
                continue
            else:
                t1 += 1
        if t1 == len(self.JavaList):
            print("当前JAVA变量不正常, 请立即更换!")

    def popen(self, command: str) -> tuple:
        import subprocess
        stdout, stderr = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ).communicate()
        try:
            out = stdout.decode("utf-8")
        except UnicodeDecodeError:
            out = stdout.decode("GBK")
        try:
            err = stderr.decode("utf-8")
        except UnicodeDecodeError:
            err = stderr.decode("GBK")
        return out, err

    def setting_java_version(self):

        import os
        import time
        import subprocess
        import sys

        self.get_now_java()

        while True:
            version = str(self.new_input("请输入要切换的Java版本: "))
            if version in self.JavaList:
                print("\n正在更改%JAVA_HOME%...")
                out, err = self.popen(f"setx -m \"JAVA_HOME\" \"{self.JavaList[version]}")
                if "成功" in out:
                    print("\n保存成功！")
                else:
                    print("\n保存失败，请重新以管理员身份运行！")

                print("\n正在获取%Path%")
                # setx改变后的%Path%是没有变量存在的，wmic可以
                out, err = self.popen(
                    "wmic ENVIRONMENT where \"name = 'path' and username='<system>'\" get VariableValue")
                path = out.replace(
                    "VariableValue                                                                                "
                    "                                                                                             "
                    "                                                                             ",
                    "")
                path = path.replace("\r\r\n", "")
                if "%JAVA_HOME%\\bin\\" not in path:
                    print("正在备份%path%")
                    now_time = time.strftime("%y %a %b %d %H:%M:%S", time.localtime())
                    with open(f"{self.Backup}\\path_{now_time}.txt", "w+") as f1:
                        f1.write(path)

                    out, err = subprocess.Popen(
                        f"wmic ENVIRONMENT where \"name = 'a' and username='<system>'\" set VariableValue = \"%JAVA_HOME%\\bin\\;{path}%\"")

                    if "成功" in out:
                        print("备份成功")

                time.sleep(2)
                sys.exit()
            else:
                print("当前没有该Java, 若您已安装该Java, 请输入add添加Java")
                os.system("cls")


if __name__ == "__main__":
    SetJavaVersion()
