class SetJavaVersion:
    def __init__(self) -> None:

        import os
        import json

        self.JavaList = {}
        self.JavaVersionList = {}
        self.JavaPath = {}
        self.AppData = os.environ.get("AppData")

        print("欢迎使用Java切换器! 建议以管理员身份运行, 在可输入的地方输入help查看帮助")

        with open(f"{self.AppData}\\SetJavaVersion\\JavaPath.json", "r+") as f1:
            self.JavaPath = json.loads(f1.read(), strict = False)

        if not os.path.exists(f"{self.AppData}\\SetJavaVersion"):
            os.mkdir(f"{self.AppData}\\SetJavaVersion")
            self.FirstStart()
        elif not os.path.exists(f"{self.AppData}\\SetJavaVersion\\JavaPath.json") or self.JavaPath == "":
            print("配置文件已丢失, 请重新配置")
            self.FirstStart()
        else:
            self.SettingJavaVersion()


    def help():
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

声明: 该程序由Wen_Shao制作, 使用程序或源码时请标明出处
            """)

    def FirstStart(self):

        import json

        n1 = input("请问你要添加多少个Java: ")

        for j in range(int(n1)):
            JavaVersion = input(f"请输入第{j + 1}个Java版本号(Java8就写8, Java17就写17): ")
            VersionPath = input(f"请输入第{j + 1}个Java目录(例: C:\Program Files\Java\Jre_8u231): ")

        self.JavaPath[f"{JavaVersion}"] = VersionPath
        with open(f"{self.AppData}\\SetJavaVersion\\JavaPath.json", "w+") as f1:
            json.dump(self.JavaPath, f1, indent = 4)

        self.SettingJavaVersion()
        

    def SettingJavaVersion(self):

        import os
        import time

        version = input("请输入要切换的Java版本: ")

        print("正在更改用户变量...")
        os.system(f"setx \"JAVA_HOME\" \"{self.JavaPath[version]}")

        print("\n")

        print("正在更改系统变量...")
        os.system(f"setx -m \"JAVA_HOME\" \"{self.JavaPath[version]}")

        time.sleep(2)
        exit()

if __name__ == "__main__":
    SetJavaVersion()