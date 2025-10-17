from datetime import datetime
from io import BytesIO

import pytest

from foobarstats.models import TrackStat


@pytest.fixture()
def empty_stat() -> BytesIO:
    return BytesIO("""<PlaybackStatistics Version="3.0" Mapping="C653739F-14B3-4EF2-819B-A3E2883230AE">
</PlaybackStatistics>""".encode('utf-8'))

@pytest.fixture()
def stat_empty_entry():
    return BytesIO("""<PlaybackStatistics Version="3.0" Mapping="C653739F-14B3-4EF2-819B-A3E2883230AE">
  <Entry ID="59fed92825ecb76d" Count="0" Added="133922363049820270" AddedFriendly="2025-01-01 12:00:00" >
    </Entry>
</PlaybackStatistics>""".encode('utf-8'))


@pytest.fixture()
def entry_no_stats() -> BytesIO:
    return BytesIO("""<PlaybackStatistics Version="3.0" Mapping="C653739F-14B3-4EF2-819B-A3E2883230AE">
  <Entry ID="59fed92825ecb76d" Count="0" Added="133922363049820270" AddedFriendly="2024-01-01 12:00:00" >
<Item Path="/filepath/Track.flac"></Item>  </Entry>
</PlaybackStatistics>""".encode('utf-8'))

@pytest.fixture()
def no_stats_target() -> list[TrackStat]:
    added = datetime(2024, 1,1,12,0,0)
    return [TrackStat(Path="/filepath/Track.flac", Subsong=None, Count=0, Added=added, FirstPlayed=None, LastPlayed=None)]

@pytest.fixture()
def entries_correct_stats() -> BytesIO:
    return BytesIO("""<PlaybackStatistics Version="3.0" Mapping="C653739F-14B3-4EF2-819B-A3E2883230AE">
  <Entry ID="d12c59be0b98de6d" Count="14" FirstPlayed="133684470727504690" FirstPlayedFriendly="2024-01-01 12:00:0" LastPlayed="134017270777327040" LastPlayedFriendly="2025-01-01 12:00:00" Added="133684472245531140" AddedFriendly="2024-01-01 12:00:00" >
<Item Subsong="1" Path="/filepath/Album.cue"></Item>  </Entry>
</PlaybackStatistics>""".encode('utf-8'))

@pytest.fixture()
def correct_stats_target() -> list[TrackStat]:
    added = datetime(2024, 1,1,12,0,0)
    last = datetime(2025, 1,1,12,0,0)
    return [TrackStat(Path="/filepath/Album.cue", Subsong=1, Count=14, Added=added, FirstPlayed=added, LastPlayed=last)]
