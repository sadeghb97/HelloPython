import threading
from fortnite_tracker import getBattleRoyalStats
from functools import partial

class FortniteProcess(threading.Thread) :

    def __init__(self, platform, epic_nickname, callback):
        threading.Thread.__init__(self)
        self.platform = platform
        self.epic_nickname = epic_nickname
        self.callback = callback
        self.setName(epic_nickname)

    def run(self) :
        getBattleRoyalStats(self.platform, self.epic_nickname)
        self.callback()

callback = lambda name : print(f"{name} Finished!")
fp1 = FortniteProcess("psn", "uihyufdxd", partial(callback, "uihyufdxd"))
fp2 = FortniteProcess("psn", "foxxxy_97", partial(callback, "foxxxy_97"))
fp3 = FortniteProcess("psn", "cgfcfgcfcfcfg", partial(callback, "cgfcfgcfcfcfg"))

print("Strating ...")
fp1.start()
fp2.start()
fp3.start()
print("Started ...")

fp1.join()
fp2.join()
fp3.join()
print("Program finished!")