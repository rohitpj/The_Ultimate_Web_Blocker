# Website-Blocker
Just a normal website blocker but you have to solve a leetcode problem to unblock websites. Additional feature where you put some files up as collateral, they are encrypted and only decrypted when the blocking time has elapsed. If you must you can uncomment lines 54 & 55 in file_encryption.py to temporarily delete the original files so if you feel tempted to close the program you need to decrypt them yourself :).

Quick disclaimer, please, PLEASE do not use file_encryption if you haven't reviewed the code yourself and tested with sm random file, it seems good here but I have no idea how it will go on other platforms or devices and I will feel bad if your files are lost.

Will need to run as admin, edit websites you want to block in source code since it won't be happening much and I still have no idea how to unit test.
