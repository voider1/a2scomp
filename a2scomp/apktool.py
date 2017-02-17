import subprocess
import sys


def decode_apk(apk):
    try:
        subprocess.run(['apktool', 'd', '-f', '-r', apk],
                       stdout=subprocess.DEVNULL).check_returncode()
    except subprocess.CalledProcessError:
        print('[-] The APK can\'t be decoded')
        sys.exit()


def build_apk(apk_folder):
    try:
        subprocess.run(['apktool', 'b', apk_folder],
                       stdout=subprocess.DEVNULL).check_returncode()
    except subprocess.CalledProcessError:
        print('[-] The APK can\'t be rebuild after decoding')
        sys.exit()
