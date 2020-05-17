#vaghti mikhahim module ra import konim python ebteda masire feli ra migardad
#ta bebinad aya yek file hamnam vojud darad ye na
#agar nabud misaire aslie system ra migardad va agar baz ham peyda nakard error midahad

#ba har raveshi ke yek module import shavad code haye darune an ke be surate global
#hastand ejra mishavad

#baraye dastresi be var ha va tavabe an az module_name.{var_name} estefade mikonim
#ba keyworde as mitavan name module ra baraye seda zadan dar codeman taghir dahim
#import fortnite_tracker #as ft

#dar in ravesh tamae var ha va tavabe import shode va baraye dastresi ba an ha
#faghat kafist name an hara seda bezanim
#from fortnite_tracker import *

#dar in ravesh faghat yek var ya tabe ra mitavan import kard
#ke mostaghiman mitavanad seda zade shavad
#deghat konid ke dar in ravesh ham hata tamame code haye global darune file
#ejra khahad shod
#ham chenin deghat konid agar dobar az yek file import konim
#code haye darune an faghat yek bar ejra mishavad
#....
from fortnite_tracker import LAST_PLATFORM
#....
#do tabe ba in nam vojud darad ke hardo ghabele estefade khahad bud
from fortnite_tracker import getBattleRoyalStats

getBattleRoyalStats()
print("PlaTfOrmMM: " + LAST_PLATFORM)