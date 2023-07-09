class SetJavaVersion:
    def __init__(self) -> None:
        # 初始化

        import os
        import json
        # 导入模块

        self.java_list = {}
        self.JavaVersionList = {}
        self.AppData = f"{os.environ.get('Appdata')}\\SetJavaVersion"
        self.Temp = f"{os.environ.get('Temp')}\\SetJavaVersion"
        self.CommandList = ["help", "add", "remove", "reset"]
        self.Backup = f"{self.AppData}\\Backup"
        self.start = None
        # 设置可能需要用到的全局变量

        self.admini()  # 检测是否以管理员身份运行
        self.find_java_list = self.find_java()  # 搜索Java

        print("欢迎使用Java切换器!")

        if not os.path.exists(self.AppData):  # 判断是否存在配置文件夹
            os.makedirs(self.AppData, exist_ok=True)
            os.makedirs(self.Backup, exist_ok=True)
            with open(f"{self.AppData}\\JavaPath.json", "w") as f1:
                self.java_list = {}
                f1.write("{}")
            # 不存在，创建目录和配置文件
        else:
            # 存在，检查配置文件是否存在切不为空
            if os.path.isfile(f"{self.AppData}\\JavaPath.json"):
                # 存在，读取
                with open(f"{self.AppData}\\JavaPath.json", "r+", encoding="utf-8") as f1:
                    f1_txt = f1.read().replace(" ", "")
                    if f1_txt == "{}":
                        self.java_list = {}
                    elif f1_txt == "":
                        self.java_list = {}
                        f1.write("{}")
                    else:
                        self.java_list = json.loads(f1_txt)
            else:
                with open(f"{self.AppData}\\JavaPath.json", "w") as f1:
                    self.java_list = {}
                    f1.write("{}")
            self.start = True
            self.setting_java_version()

    def find_java(self):
        import os
        find_java_list = {}
        java_version = None
        count = 0

        for i in range(65, 91):
            if not os.path.exists(f"{chr(i)}:"):
                continue
            if os.path.exists(f"{chr(i)}:\\Program Files") and os.path.exists(f"{chr(i)}:\\Program Files (x86)"):
                p64 = f"{chr(i)}:\\Program Files\\Java"
                p32 = f"{chr(i)}:\\Program Files (x86)\\Java"
            else:
                p64 = ""
                p32 = f"{chr(i)}:\\Program Files (x86)\\Java"
            if os.path.exists(p64):
                for j in os.listdir(p64):
                    if os.path.exists(f"{p64}\\{j}\\bin"):
                        if "java.exe" not in os.listdir(f"{p64}\\{j}\\bin") and "javaw" not in os.listdir(
                                f"{p64}\\{j}\\bin"):
                            continue
                        if "javac.exe" in os.listdir(f"{p64}\\{j}\\bin"):
                            attribute = "JDK x64"
                        else:
                            attribute = "JRE x64"
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
                    count += 1
                    find_java_list[f"f_{t2 + 1}"] = {"name": f"自动查找{count}", "path": f"{p64}\\{j}",
                                                     "version": java_version,
                                                     "attribute": attribute}
            if os.path.exists(p32):
                for j in os.listdir(p32):
                    if os.path.exists(f"{p32}\\{j}\\bin"):
                        if "java.exe" not in os.listdir(f"{p64}\\{j}\\bin") and "javaw" not in os.listdir(
                                f"{p64}\\{j}\\bin"):
                            break
                        if "javac.exe" in os.listdir(f"{p32}\\{j}\\bin"):
                            attribute = "JDK x32"
                        else:
                            attribute = "JRE x32"
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
                    count += 1
                    find_java_list[f"f_{t2 + 1}"] = {"name": "自动查找{count}", "path": f"{p32}\\{j}",
                                                     "version": java_version, "attribute": attribute}
        return find_java_list

    def admini(self):
        import ctypes
        import sys

        if ctypes.windll.shell32.IsUserAnAdmin():
            return
        else:
            ret = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
            if ret <= 32:
                raise Exception("无法以管理员身份运行脚本")
            sys.exit()

    def new_input(self, values, now_mode=None, w_type: type = str):
        out = input(values)
        if out == "help":
            if now_mode != "help":
                self.help()
                out = input(values)
            else:
                print("你已经在该模式中")
        elif out == "add":
            if now_mode != "add":
                self.add()
                out = input(values)
            else:
                print("你已经在该模式中")
        elif out == "remove":
            if now_mode != "remove":
                self.remove()
                out = input(values)
            else:
                print("你已经在该模式中")
        elif out == "reset":
            if now_mode != "reset":
                self.reset()
                out = input(values)
            else:
                print("你已经在该模式中")
        try:
            out = w_type(out)
        except ValueError:
            if w_type == int:
                print("\n请输入一个整数！")
            elif w_type == str:
                print("\n请输入一串文字！")
            out = self.new_input(values, w_type=w_type)
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
        移除所有该程序修改过的系统变量

    Java路径保存位置: 
        %AppData%\\SetJavaVersion

声明: 该程序由程虚员制作, 使用程序或源码时请开源
            """)

    def add(self):

        import json
        import os

        if not self.start:
            os.system("cls")

        n1 = self.new_input("请问你要添加多少个Java: ", "add")

        for i in range(int(n1)):
            java_name = self.new_input(f"请输入您要导入的第{i + 1}个Java版本名称(自定义, 啥都行): ", "add")
            java_path = self.new_input(f"请输入您要导入的第{i + 1}个Java目录: ", "add")
            if java_path[-1] == "\\":
                java_path = java_path[:-1]
            if java_path[-4:] == "\\bin":
                java_path = java_path[:-4]
            if "javac" in os.listdir(f"{java_path}\\bin"):
                attribute = "JDK"
            else:
                attribute = "JRE"
            self.java_list["自定义1"] = {"name": java_name, "path": java_path, "attribute": attribute}
        with open(f"{self.AppData}\\JavaPath.json", "w+", encoding="utf-8") as f1:
            json.dump(self.java_list, f1, indent=4)

    def remove(self):
        import os

        os.system("cls")
        print("开发中, 敬请期待,")

    def reset(self):
        import os

        os.system("cls")
        print("开发中, 敬请期待,")

    def now_java(self):
        import os
        if os.environ.get("JAVA_HOME") is not None:
            now_java_path = os.environ.get("JAVA_HOME")
        else:
            print("当前JAVA变量不正常, 请立即更换!")
            return
        t1 = 0
        for i in self.java_list:
            if self.java_list[i]["path"] == now_java_path:
                print(f"当前Java为 {self.find_java_list[i]['name']} , 位于 {now_java_path}")
                break
            else:
                t1 += 1
        for j in self.find_java_list:
            if self.find_java_list[j]["path"] == now_java_path:
                print(f"当前Java为 {self.find_java_list[j]['name']} , 位于 {now_java_path}")
                break
            else:
                t1 += 1
        if t1 == len(self.java_list) + len(self.find_java_list):
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
        import sys
        from tabulate import tabulate
        import threading

        class Thread(threading.Thread):
            def __init__(self, target, args=()):
                super().__init__()
                self.target = target
                self.args = args
                self.result = None

            def run(self):
                self.result = self.target(*self.args)
                super().run()

        self.now_java()

        if not self.start:
            os.system("cls")

        headers = ["序号", "名称", "路径", "属性"]
        data = []

        count = 0
        for i in self.find_java_list:
            count += 1
            data.append([count, self.find_java_list[i]["name"], self.find_java_list[i]["path"],
                         self.find_java_list[i]["attribute"]])
        for i in self.java_list:
            count += 1
            data.append([count, self.java_list[i]["name"], self.java_list[i]["path"], self.java_list[i]["attribute"]])

        print(tabulate(data, headers=headers, tablefmt="grid"))

        num = int(self.new_input("请输入要切换的Java序号: ", w_type=int))

        if num > len(self.find_java_list):
            num -= len(self.find_java_list)

        while True:
            for i in self.find_java_list:
                if str(num) in self.find_java_list[i]["name"]:
                    T1 = Thread(target=self.popen, args=(f"setx -m \"JAVA_HOME\" \"{self.find_java_list[i]['path']}",))
                    T1.start()
                    print("\n")
                    while True:
                        if T1.result is None:
                            for j in range(7):
                                print(f"\r正在更改%JAVA_HOME%{'.' * j}{' ' * (6 - j)}", end="")
                                time.sleep(0.5)
                        else:
                            out, err = T1.result
                            break


                    if "JDK" in self.find_java_list[i]["attribute"]:
                        T2 = Thread(target=self.popen, args=(
                        f"wmic ENVIRONMENT where \"name = 'java_class' and username='<system>'\" set VariableValue = \"%JAVA_HOME%\\lib\\dt.jar;%JAVA_HOME%\\lib\\tools.jar\"",))
                        T2.start()
                        print("\n")
                        while True:
                            if T2.result is None:
                                for j in range(7):
                                    print(f"\r正在更改java_class{'.' * j}{' ' * (6 - j)}", end="")
                                    time.sleep(0.5)
                            else:
                                out, err = T2.result
                                break
                    else:
                        T2 = Thread(target=self.popen, args=(f"setx -m \"java_class\" \"\"",))
                        T2.start()
                        print("\n")
                        while True:
                            if T2.result is None:
                                for j in range(7):
                                    print(f"\r正在删除java_class{'.' * j}{' ' * (6 - j)}", end="")
                                    time.sleep(0.5)
                            else:
                                out, err = T2.result
                                break

                    T3 = Thread(target=self.popen, args=("wmic ENVIRONMENT where \"name = 'path' and username='<system>'\" get VariableValue",))
                    T3.start()
                    print("\n")
                    while True:
                        if T3.result is None:
                            for j in range(7):
                                print(f"\r正在检查%path%是否符合条件{'.' * j}{' ' * (6 - j)}", end="")
                                time.sleep(0.5)
                        else:
                            out, err = T3.result
                            break
                    path = out.replace(
                        "VariableValue                                                                                "
                        "                                                                                             "
                        "                                                                             ",
                        "")
                    path = path.replace("\r\r\n", "")
                    if "%JAVA_HOME%\\bin\\" not in path:
                        T4 = Thread(target=self.popen, args=(
                            "wmic ENVIRONMENT where \"name = 'path' and username='<system>'\" get VariableValue",))
                        T4.start()
                        print("\n")
                        while True:
                            if T2.result is None:
                                for j in range(7):
                                    print(f"\r正在修改%path%{'.' * j}{' ' * (6 - j)}", end="")
                                    time.sleep(0.5)
                            else:
                                out, err = T4.result
                                break
                    else:
                        print("\n%path%符合条件")

                    print("\n修改成功！")

                    time.sleep(2)
                    sys.exit()
            print("\n当前没有该Java, 若您已安装该Java, 请输入add添加Java")
            os.system("cls")


if __name__ == "__main__":
    SetJavaVersion()
