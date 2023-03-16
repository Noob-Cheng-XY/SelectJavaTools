# SetJavaVersion（设置Java版本）

## 简介：

这是一个用**Python**制作的能让您快速更改您的**JAVA**版本的简易软件，让**Minecraft Mod**制作者和**JAVA**用户不再操心。

使用方法：

第一次使用时会出现引导，根据引导先输入要加多少个Java，然后输入第一个Java的版本号，再输入第一个Java的路径，以此类推，然后结束引导。之后输入Java版本号即可更换Java。

## 更新预告：

### v0.3-beta

1. 完善help及一些小命令

## 更新日志：

### 正式版：

#### v1.0

1. 对于更改JAVA_HOME时的执行模块进行更改（从 **os.system()** 更改为 **subprocess.Popen()** ）
2. 对于更改JAVA_HOME时的反馈进行更改
3. 更新了add模块
4. 修复：修复了v0.2.1-beta中的无法使用help功能的问题（那时写了个reinput函数，但没用上…)
5. 更改：以后的所有参与构建的项目文件中均不会出现未完成的内容

##### v0.2.1-beta

1. 恢复help功能

##### v0.2-beta

1. 将各个功能模块化，以便其他开发者调用
2. 更改Java路径的储存方式（现储存在%AppData%\SetJavaVersion\JavaPath.json）
3. 修复了一些~~特性~~Bug

##### v0.1-beta

1. 创建项目
2. 完成基础功能
3. 在help列表中留下了即将加入的功能使用方法，不完整且不可信  （ ~~BugJump行为~~ ）
4. 现在的Java路径储存方式为使用系统变量
