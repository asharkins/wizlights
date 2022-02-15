from pywizlight import wizlight
from enum import Enum



class Group(Enum):
    NA = 0
    LivingRoom = 1
    Bathroom = 2
    Bedroom = 3


class Subgroup(Enum):
    NA = 0
    Table = 1
    Sofa = 1

class MyWizBulb(wizlight):
    name: str
    ip: str
    mac_address: str
    group: Group = Group.NA
    subgroup: Group = Subgroup.NA
    online: bool = False
    enabled: bool = False
    details: dict = None


bulb_details = {
'a8bb5072a23a': {'name': 'tall light',  'ip': '192.168.1.83', 'group': Group.LivingRoom},
'6c2990a70f20': {'name': 'table',       'ip': '192.168.1.143', 'group': Group.LivingRoom},
'6c2990a71b79': {'name': 'mr arnold',   'ip': '192.168.1.250', 'group': Group.LivingRoom},
'6c2990a7193a': {'name': 'behind door', 'ip': '192.168.1.89', 'group': Group.LivingRoom},
'6c2990a6f076': {'name': 'shakira',     'ip': '192.168.1.119', 'group': Group.LivingRoom},
'6c2990a6f58e': {'name': 'sofa corner', 'ip': '192.168.1.198', 'group': Group.LivingRoom},
'6c2990a72810': {'name': 'valparaiso',  'ip': '192.168.1.212', 'group': Group.LivingRoom},
'a8bb50727a3a': {'name': 'short light' ,'ip': '192.168.1.214', 'group': Group.Bedroom},
'6c2990a6f60c': {'name': 'wizBathroom1','ip': '192.168.1.117'}, 'group': Group.Bathroom,
'6c2990a715dd': {'name': 'wizBathroom2','ip': '192.168.1.247', 'group': Group.Bathroom}
}