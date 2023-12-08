; 148/266
; 1920x1080

#include <AutoItConstants.au3>
HotKeySet("{F1}", "addWeapon")
HotKeySet("{F2}", "addFix")
HotKeySet("{F3}", "addFixRemoval")
HotKeySet("{F6}", "cleanInventory")
HotKeySet("{F7}", "gainWP")
HotKeySet("{F8}", "entWep")
HotKeySet("{F9}", "entWepHyper")
HotKeySet("{ESC}", "Terminate")

;HotKeySet("{F1}", "stdWep")

start()

Func start()
	WinActivate("DreamACE")
	While 1
		Sleep(1)
	WEnd
EndFunc

Func entWepHyper()
	addWeapon()
	addFixRemoval()
EndFunc

Func entWep()
	addWeapon()
	addFix()
EndFunc

Func stdWep()
	Sleep(10)
	MouseDown($MOUSE_CLICK_LEFT)
	Sleep(10)
EndFunc

Func autoRose()
	Sleep(10)
	MouseClick($MOUSE_CLICK_LEFT, 1166,623, 2 , 1)
	Sleep(10)
	MouseMove(1166,623)
	Sleep(10)
	MouseClick($MOUSE_CLICK_LEFT, 1326, 982, 2, 1)
EndFunc

Func stdWepRelease()
	Sleep(10)
	MouseUp($MOUSE_CLICK_LEFT)
	Sleep(10)
EndFunc

Func gainWP()
	Send("{1 down}")
EndFunc

Func addWeapon()
	Sleep(50)
	MouseClick($MOUSE_CLICK_LEFT, 920, 908, 2, 1)
	Sleep(50)
EndFunc

Func addFix()
	Sleep(50)
	MouseClick($MOUSE_CLICK_LEFT, 892, 908, 2, 1)
	Sleep(50)
	go()
EndFunc

Func addFixRemoval()
	Sleep(50)
	MouseClick($MOUSE_CLICK_LEFT, 863, 908, 2, 1)
	Sleep(50)
	go()
	;addWeapon()
	;addFix()
EndFunc

Func go()
	Sleep(50)
	MouseClick($MOUSE_CLICK_LEFT, 1270, 687, 1, 1)
	Sleep(2300)
	MouseClick($MOUSE_CLICK_LEFT, 1270, 687, 1, 1)
	Sleep(100)
	MouseMove(920, 908, 1)
	Sleep(50)
EndFunc

Func Terminate()
	Exit
EndFunc