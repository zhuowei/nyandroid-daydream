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
* RocketLauncher (Android 4.0 Ice Cream Sandwitch)
* BeanFlinger (Android 4.1, 4.2, 4.3 Jelly Bean)
* DessertCase (Android 4.4 KitKat)

This app installs one app drawer shortcut and one daydream per easter egg.

It can be found on the Play Store under the name [Android Easter Egg Daydreams][applink],
published by [Zhuowei Zhang][].

[applink]: https://play.google.com/store/apps/details?id=net.zhuoweizhang.nyandroid
[Zhuowei Zhang]: https://github.com/zhuowei

Trivia
------
Daydreams are essentially Android screensavers, that can be made interactive, and run when docked/charging. In the Android code, you'll see references to Screensavers, Sleep Mode Apps, and other names as well as Daydreams, the last is the name that was given to the feature at release.

Daydreams were added in Android 4.2, Jelly Bean maintenance release 1, but were actually in development for over a year, since before 4.0/ICS. 
Nyandroid and RocketLauncher were two early proto-daydreams that shipped with 4.0 even though the screensaver feature did not. RocketLauncher and "Android Dreams" were [discovered in November 2011][rocketDiscovered], with an [interesting commit][predictLeak] that predicted exactly what happened.

Daydreams are actually a sort-of-replacement for "dock mode" apps from Ecliar, that function rather differently, but still allow apps to take over the screen. Simply put, the way that Car Home worked confused users, and it was decided that a screensaver could fill some of the gaps left if that feature was removed. See the excellent [Google I/O 2013 Talk: Androids Do Daydream][AndroidsDoDaydream] for more information. (That's where much of the information in this section came from. It also mentions Android's blink tag, for the interested.)

[predictLeak]: https://github.com/CyanogenMod/android_packages_apps_Settings/commit/d1d9fc3ac9f2b6f2f2b8d042ed4e6180d0ac904f
[rocketDiscovered]: http://www.androidpolice.com/2011/11/30/another-ics-easter-egg-weird-star-wars-like-light-speed-launcher-found-hidden-in-the-depths-of-ice-cream-sandwich/
[AndroidsDoDaydream]: https://www.youtube.com/watch?v=h_kcDkwoTr0

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


Alternatively, use the ant build tool: (See [here][buildCMD] for more info)

* Install ant
* You may need to run "android update project --path ./"
* Run ant from project directory to get options
* To get going quickly, run "ant debug" and then "ant installd"


[SDK_Bundle]: https://developer.android.com/
[BuildAndRun]: https://developer.android.com/tools/building/building-eclipse.html#RunningOnDeviceEclipse
[buildCMD]: https://developer.android.com/tools/building/building-cmdline.html