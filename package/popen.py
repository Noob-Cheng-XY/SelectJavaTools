def main(command: str) -> tuple:
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
