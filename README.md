# a2scomp
A commandline tool to make it easier to change the SMALI of an APK and automate the process of recompiling and signing APKs
## Requirements
Make sure the following tools are in your path:

* apktool
    * View this link for installation: https://ibotpeaches.github.io/Apktool/install/
* zipalign & apksigner
    * Install the Android SDK and add the Android SDK platform-tools to your path: https://developer.android.com/studio/index.html
* jadx
    * View this link for installation: https://github.com/skylot/jadx

##Guide
To view all options of the tool do:

```shell
a2scomp --help
```

Decode an APK to smali:

```shell
a2scomp --apk the_apk.apk decode
```

Build smali back to an APK:

```shell
a2scomp --smali smali-folder build
```

Zipalign an APK:

```shell
a2scomp --apk the_apk.apk zipalign
```

Sign an APK:

```shell
a2scomp --apk the_aligned_apk.apk sign
```

Building and zipaligning an APK:

```shell
a2scomp --smali smali-folder build --zipalign
```

Building, zipaligning and signing an APK:

```shell
a2scomp --smali smali-folder build --zipalign --sign
```

Zipaligning and signing an APK:

```shell
a2scomp --apk the_apk.apk zipalign --sign
```
