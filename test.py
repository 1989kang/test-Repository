from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage

device = MonkeyRunner.waitForConnection()

MonkeyRunner.sleep(3)

device.shell('am force-stop com.shangrong.jieme')

MonkeyRunner.sleep(3)

device.startActivity(component=monkey'com.shangrong.jieme/com.shangrong.jieme.TestActivity')

MonkeyRunner.sleep(10)

device.press('KEYCODE_DPAD_UP','DOWN_AND_UP')

MonkeyRunner.sleep(2)

device.press('KEYCODE_DPAD_RIGHT','DOWN_AND_UP')

MonkeyRunner.sleep(5)

device.sleep('KEYCODE_DPAD_CENTER','DOWN_AND_UP')

MonkeyRunner.sleep(10)

device.press('KEYCODE_DPAD_DOWN','DOWN_AND_UP')

MonkeyRunner.sleep(3)

device.press('KEYCODE_BACK','DOWN_AND_UP')

MonkeyRunner.sleep(3)

result=device.takeSnapshot()

result.writeToFile('./pic001.png','png')
