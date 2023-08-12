def main(java_list=None):
    if java_list is None:
        java_list = {}
    global java_version
    import os
    count = 0

    for i in range(65, 91):
        if not os.path.exists(f"{chr(i)}:"):
            continue

        if os.path.exists(f"{chr(i)}:\\Program Files") and os.path.exists(f"{chr(i)}:\\Program Files (x86)"):
            p64 = f"{chr(i)}:\\Program Files\\Java"
            p32 = f"{chr(i)}:\\Program Files (x86)\\Java"
        elif os.path.exists(f"{chr(i)}:\\Program Files"):
            p64 = f"{chr(i)}:\\Program Files\\Java"
            p32 = ""
        elif os.path.exists(f"{chr(i)}:\\Program Files (x86)"):
            p64 = ""
            p32 = f"{chr(i)}:\\Program Files (x86)\\Java"
        else:
            p64 = ""
            p32 = f"{chr(i)}:\\Program Files (x86)\\Java"

        if os.path.exists(p64):
            for j in os.listdir(p64):
                if os.path.exists(f"{p64}\\{j}\\bin"):
                    if "java.exe" not in os.listdir(f"{p64}\\{j}\\bin") and "javaw.exe" not in os.listdir(
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
                            break
                        else:
                            java_version = None
                except (FileNotFoundError, IOError):
                    java_version = None
                t2 = len(java_list)
                count += 1
                java_list[f"find_{t2 + 1}"] = {"name": f"自动查找{count}", "path": f"{p64}\\{j}",
                                               "version": java_version,
                                               "attribute": attribute}
        if os.path.exists(p32):
            for j in os.listdir(p32):
                if os.path.exists(f"{p32}\\{j}\\bin"):
                    if "java.exe" not in os.listdir(f"{p64}\\{j}\\bin") and "javaw.exe" not in os.listdir(
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
                t2 = len(java_list)
                count += 1
                java_list[f"find_{t2 + 1}"] = {"name": "自动查找{count}", "path": f"{p32}\\{j}",
                                               "version": java_version, "attribute": attribute}
    return java_list


if __name__ == "__main__":
    print(main())
