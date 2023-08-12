"""
This Python package is developed for SelectJavaTools and uses the same license as SelectJavaTools (GNU General Public License v3.0).
这个Python包是为SelectJavaTools制作的，并使用了与SelectJavaTools相同的协议（GNU General Public License v3.0）。
"""

version = "0.1.0"

# 初始化

from os import environ
from get_admini import main as get_admini
from find_java import main as find_java
import config

# 导入模块

CommandList = ["help", "add", "remove", "reset"]
PATH = {"AppData": f"{environ.get('AppData')}\\SelectJavaTools", "Temp": f"{environ.get('Temp')}\\SelectJavaTools",
        "Backup": f"{environ.get('AppData')}\\SelectJavaTools\\Backup"}
# 设置可能需要用到的变量
