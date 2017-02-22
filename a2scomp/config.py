class Config:
    def __init__(self, apk, smali, keystore=None, clean=None):
        self.apk = apk
        self.smali = smali
        self.keystore = keystore
        self.clean = clean
