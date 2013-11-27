Nyandroid Daydream
==================

About
------
A collection of Android Daydreams based on the easter eggs of Android 4.0+, packaged into one app.

This project is a re-package of certain code, with some modifications,
from the [Android Open Source Project (AOSP)][AOSP], with the aim of allowing users of newer
versions of Android to enjoy the easter eggs of years past.

[AOSP]: https://android.googlesource.com

It includes the following easter eggs:

* Nyandroid (Android 4.0 Ice Cream Sandwitch)
* BeanFlinger (Android 4.1, 4.2, 4.3 Jelly Bean)
* DessertCase (Android 4.4 KitKat)

This app installs one app drawer shortcut and one daydream per easter egg.

It can be found on the Play Store under the name [Android Easter Egg Daydreams][applink],
published by [Zhuowei Zhang][].

[applink]: https://play.google.com/store/apps/details?id=net.zhuoweizhang.nyandroid
[Zhuowei Zhang]: https://github.com/zhuowei

Building
--------
To build the code, it can be imported into Eclipse:
(This abbreviated list of steps assumes some knowledge of Git and Android Devlopement, as well as a set-up environment.)

1. Get the code
2. Open Eclipse (with the ADT installed, download [here][SDK_Bundle])
3. File -> New -> Other
4. Select "Android Project from Existing Code"
5. Point Eclipse at the folder where you put the code, then click through the import screens
6. Run from Eclipse (See [here][BuildAndRun] for more info)

(The .gitignore file should keep Eclipse files from getting tangled up in git.)

[SDK_Bundle]: https://developer.android.com/
[BuildAndRun]: https://developer.android.com/tools/building/building-eclipse.html#RunningOnDeviceEclipse
