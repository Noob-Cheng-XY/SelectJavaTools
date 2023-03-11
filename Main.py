class SetJavaVersion:
    def __init__(self) -> None:

        import os
        import json

        self.JavaList = {}
        self.JavaVersionList = {}
        self.AppData = os.environ.get("AppData")

        print("欢迎使用Java切换器! 请以管理员身份运行, 在可输入的地方输入help查看帮助")

        with open(f"{self.AppData}\\SetJavaVersion\\JavaPath.json", "r+") as f1:
            self.JavaList = json.loads(f1.read(), strict = False)

        if not os.path.exists(f"{self.AppData}\\SetJavaVersion"):
            os.mkdir(f"{self.AppData}\\SetJavaVersion")
            self.FirstStart()
        elif not os.path.exists(f"{self.AppData}\\SetJavaVersion\\JavaPath.json") or self.JavaList == "":
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

        self.JavaList[f"{JavaVersion}"] = VersionPath
        with open(f"{self.AppData}\\SetJavaVersion\\JavaPath.json", "w+") as f1:
            json.dump(self.JavaList, f1, indent = 4)

        self.SettingJavaVersion()
        
    def GetNowJava(self):
        import os
        try:
            if os.environ.get("JAVA_HOME") != None:
                NowJavaPath = os.environ.get("JAVA_HOME")
        finally:
            t1 = 0
            for NowJavaVersion in self.JavaList.keys():
                if self.JavaList[NowJavaVersion] == NowJavaPath:
                    print(f"当前Java为{NowJavaVersion}, 位于{NowJavaPath}")
                    continue
                else:
                    t1 += 1
        if t1 == len(self.JavaList):
            print("当前JAVA变量不正常, 请立即更换!")

    def SettingJavaVersion(self):

        import os
        import time

        self.GetNowJava()
        
        while True:
            try:
                version = str(input("请输入要切换的Java版本: "))
                self.JavaList[version]
            except:
                print("当前没有该Java, 若您已安装该Java, 请输入add添加Java")
            else:
                print("正在更改用户变量...")
                os.system(f"setx \"JAVA_HOME\" \"{self.JavaList[version]}")

                print("\n")

                print("正在更改系统变量...")
                os.system(f"setx -m \"JAVA_HOME\" \"{self.JavaList[version]}")

                time.sleep(2)
                exit()

if __name__ == "__main__":
    SetJavaVersion()