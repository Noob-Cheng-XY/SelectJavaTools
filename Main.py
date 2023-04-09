from __future__ import print_function


class SetJavaVersion:
    def __init__(self) -> None:
        # 初始化

        import os
        import json
        # 导入模块

        self.JavaList = {}
        self.JavaVersionList = {}
        self.AppData = os.environ.get("AppData") + "\\SetJavaVersion"
        self.Temp = os.environ.get("Temp") + "\\SetJavaVersion"
        self.CommandList = ["help", "add", "remove", "reset"]
        self.Backup = f"{self.AppData}\\Backup"
        # 设置可能需要用到的全局变量

        self.admini()  # 检测是否以管理员身份运行

        print("欢迎使用Java切换器! 请以管理员身份运行, 在可输入的地方输入help查看帮助")

        if not os.path.exists(self.AppData):  # 判断是否存在配置文件夹
            os.mkdir(self.AppData)
            os.mkdir(self.Backup)
            self.First = True
            self.FirstStart()
            # 不存在，创建目录并开始配置
        else:
            # 存在，判断配置文件是否存在
            if not os.path.exists(f"{self.AppData}\\JavaPath.json"):
                with open(f"{self.AppData}\\JavaPath.json", "w+") as f1:
                    self.JavaList = json.load(f1, strict=False)
                self.FirstStart()
                # 不存在，创建文件并开始配置
            else:
                with open(f"{self.AppData}\\JavaPath.json", "w", encoding="utf-8") as f1:
                    pass
                if self.JavaList == {}:
                    print("配置文件已丢失, 请重新配置")
                    self.FirstStart()
                else:
                    self.SettingJavaVersion()

    def admini(self):
        import ctypes
        import sys
        if ctypes.windll.shell32.IsUserAnAdmin():
            return
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

    def NewInput(self, values, now_mode=None):
        out = input(values)
        if out == "help":
            if now_mode != "help":
                self.Help()
            else:
                print("你已经在该模式中")
        elif out == "add":
            if now_mode != "add":
                self.Add()
            else:
                print("你已经在该模式中")
        elif out == "remove":
            if now_mode != "remove":
                self.Remove()
            else:
                print("你已经在该模式中")
        elif out == "reset":
            if now_mode != "reset":
                self.Reset()
            else:
                print("你已经在该模式中")
        else:
            return out

    def Help(self):
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

声明: 该程序由Wen_Shao制作, 使用程序或源码时请开源
            """)

    def Add(self):

        import json
        import os

        if not self.First:
            os.system("cls")

        n1 = self.NewInput("请问你要添加多少个Java: ", "add")

        for i in range(int(n1)):
            JavaVersion = self.NewInput(f"请输入您要导入的第{i + 1}个Java版本名(自定义, 啥都行): ")
            VersionPath = self.NewInput(f"请输入您要导入的第{i + 1}个Java目录(例: C:\Program Files\Java\Jre_8u231): ")
            self.JavaList[JavaVersion] = VersionPath
        with open(f"{self.AppData}\\JavaPath.json", "w+", encoding="utf-8") as f1:
            json.dump(self.JavaList, f1, indent=4)

    def Remove(self):
        import os

        os.system("cls")
        print("开发中, 敬请期待,")

    def Reset(self):
        import os

        os.system("cls")
        print("开发中, 敬请期待,")

    def FirstStart(self):
        self.Add()
        self.SettingJavaVersion()

    def GetNowJava(self):
        import os
        if os.environ.get("JAVA_HOME") is not None:
            NowJavaPath = os.environ.get("JAVA_HOME")
        else:
            print("当前JAVA变量不正常, 请立即更换!")
            return
        t1 = 0
        for NowJavaVersion in self.JavaList.keys():
            if self.JavaList[NowJavaVersion] == NowJavaPath:
                print(f"当前Java为{NowJavaVersion}, 位于{NowJavaPath}")
                continue
            else:
                t1 += 1
        if t1 == len(self.JavaList):
            print("当前JAVA变量不正常, 请立即更换!")

    def Popen(self, command):
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
        if out != "" and "成功" in out:
            return 1
        else:
            return 0

    def SettingJavaVersion(self):

        import os
        import time
        import subprocess

        self.GetNowJava()

        while True:
            version = str(self.NewInput("请输入要切换的Java版本: "))
            if version in self.JavaList:
                print("\n正在更改%JAVA_HOME%...")
                if self.Popen(f"setx -m \"JAVA_HOME\" \"{self.JavaList[version]}"):
                    print("\n保存成功！")
                else:
                    print("\n保存失败，需要以管理员身份运行！")
                stdout, stderr = subprocess.Popen(
                    f"setx -m \"JAVA_HOME\" \"{self.JavaList[version]}",
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                ).communicate()
                if "成功" in stdout.decode("GBK"):
                    print("\n保存成功!")
                else:
                    print("\n保存失败! 可能是未使用管理员权限启动")
                    continue
                os.environ.get("JAVA_HOME\\bin\\")

                print("\n正在备份%Path%")
                # setx改变后的%Path%是没有变量存在的，wmic可以
                stdout, stderr = subprocess.Popen(
                    f"wmic ENVIRONMENT where \"name = 'path' and username='<system>'\" get VariableValue",
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                ).communicate()
                try:
                    Path = stdout.decode("UTF-8")
                    Path = Path.replace(
                        "VariableValue                                                                                "
                        "                                                                                             "
                        "                                                                             \r\r\n",
                        "")
                    Path = Path.replace("\r\r\n\r\r\n", "")
                except UnicodeDecodeError:

                    Path = stdout.decode("GBK")
                    Path = Path.replace(
                        "VariableValue                                                                                "
                        "                                                                                             "
                        "                                                                             \r\r\n",
                        "")
                    Path = Path.replace("\r\r\n", "")
                if "%JAVA_HOME%" not in Path:
                    now_time = time.strftime("%y %a %b %d %H:%M:%S", time.localtime())
                    with open(f"{self.Backup}\\path_{now_time}.txt", "w+") as f1:
                        f1.write(Path)

                    stdout, stderr = subprocess.Popen(
                        f"`wmic ENVIRONMENT where \"name = 'a' and username='<system>'\" set VariableValue = "
                        f"\"%JAVA_HOME%\\bin\\;{Path}%\"",
                        shell=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                    ).communicate()

                    if "成功" in stdout.decode("GBK"):
                        print()

                time.sleep(2)
                exit()
            else:
                print("当前没有该Java, 若您已安装该Java, 请输入add添加Java")
                os.system("cls")


if __name__ == "__main__":
    SetJavaVersion()
