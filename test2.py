from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice

device = MonkeyRunner.waitForConnection()

device .installPackage('F:\\app-release2.apk')

MonkeyRunner.sleep(3.0)

runComponent="com.dajinrong.nongxinjie/.activity.MainActivity"

