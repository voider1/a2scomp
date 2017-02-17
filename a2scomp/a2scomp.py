import argparse
import sys

from apktool import decode_apk, build_apk


def test_apk(apk_path):
    decoded_apk = apk_path.split('/')[-1][:-4]

    print('Going to decode the APK...')
    decode_apk(apk_path)
    print('[+] Succesfully decoded the APK')
    print('Going to build the APK...')
    build_apk(decoded_apk)
    print('[+] Succesfully built the APK')


if __name__ == '__main__':
    apk_extension = '.apk'
    parser = argparse.ArgumentParser()
    parser.add_argument('apk')
    args = parser.parse_args()
    apk_path = args.apk

    if apk_path[-4:] != apk_extension:
        print('[-] The APK doesn\'t end in .apk, make sure it ends in .apk')
        sys.exit()

    print('Going to test the APK...')
    test_apk(apk_path)
    print('[+] The APK is succesfully tested')
