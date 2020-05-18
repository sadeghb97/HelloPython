import _thread
import fortnite_tracker

processes_count = 0

def callback() :
    global processes_count
    processes_count -= 1

def doStatsProcess(platform, epic_nickname) :
    global processes_count
    processes_count += 1
    _thread.start_new_thread(
        fortnite_tracker.getBattleRoyalStats, (platform, epic_nickname, callback))

doStatsProcess("psn", "uihyufdxd")
doStatsProcess("psn", "foxxxy_97")
doStatsProcess("psn", "cgfcfgcfcfcfg")

print("Running ...")
while processes_count > 0 : pass