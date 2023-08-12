def get_json(PATH, file_name):
    import os
    import json
    if not os.path.exists(PATH["AppData"]):  # 判断是否存在配置文件夹
        os.mkdir(PATH["AppData"])
        with open(f"{PATH['AppData']}\\JavaPath.json", "w") as f1:
            out = {}
            f1.write("{}")
        # 不存在，创建目录和配置文件
    else:
        # 存在，检查配置文件是否存在切不为空
        if os.path.isfile(f"{PATH['AppData']}\\JavaPath.json"):
            # 存在，读取
            with open(f"{PATH['AppData']}\\{file_name}", "r+", encoding="utf-8") as f1:
                f1_txt = f1.read().replace(" ", "")
                if f1_txt == "{}":
                    out = {}
                elif f1_txt == "":
                    out = {}
                    f1.write("{}")
                else:
                    out = json.loads(f1_txt)
        else:
            with open(f"{PATH['AppData']}\\JavaPath.json", "w") as f1:
                out = {}
                f1.write("{}")

    return out
