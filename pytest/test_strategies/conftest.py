#-*- coding:utf-8 -*-

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__))+"/../..")

import pytest
import json
from autoremovetorrents.torrent import Torrent
from autoremovetorrents.torrentstatus import TorrentStatus
from autoremovetorrents.compatibility.open import _open

@pytest.fixture(scope="module")
def test_data():
    # Load input data
    input_torrents = []
    with _open(os.path.join(os.path.realpath(os.path.dirname(__file__)),'data.json'), encoding='utf-8') as f:
        data = json.load(f)
    for torrent in data:
        torrent_obj = Torrent()
        torrent_obj.hash = torrent['hash']
        torrent_obj.name = torrent['name']
        torrent_obj.category = torrent['category']
        torrent_obj.tracker = torrent['tracker']
        torrent_obj.status = TorrentStatus(torrent['state'])
        torrent_obj.size = torrent['size']
        torrent_obj.ratio = torrent['ratio']
        torrent_obj.uploaded = torrent['uploaded']
        torrent_obj.create_time = torrent['added_on']
        torrent_obj.seeding_time = torrent['seeding_time']
        input_torrents.append(torrent_obj)

    return input_torrents

@pytest.fixture(scope="module")
def test_env():
    with _open(os.path.join(os.path.realpath(os.path.dirname(__file__)), 'environment.json'), encoding='utf-8') as f:
        env = json.load(f)
    return env