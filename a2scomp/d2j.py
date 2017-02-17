import subprocess


def dex_2_jar(apk):
    subprocess.run(['d2j-dex2jar', 'apk'])
