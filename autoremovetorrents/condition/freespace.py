import shutil
from .sortbase import ConditionWithSort

class FreeSpaceCondition(ConditionWithSort):
    def __init__(self, settings):
        ConditionWithSort.__init__(self, settings['action'])
        self._path = settings['path']
        self._min = settings['min'] * (1 << 30) # min *= 1 GiB
    
    def apply(self, torrents):
        torrents = list(torrents)
        ConditionWithSort.sort_torrents(self, torrents)
        free_space = shutil.disk_usage(self._path)[2]
        for torrent in torrents:
            if free_space < self._min:
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)
            free_space += torrent.size