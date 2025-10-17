import foobarstats


def test_load(empty_stat,
              stat_empty_entry,
              entry_no_stats,
              no_stats_target,
              entries_correct_stats,
              correct_stats_target):

    target = [i for i in foobarstats.load(empty_stat)]
    assert target == [], "Empty root, no Entries, no Items"

    target = [i for i in foobarstats.load(stat_empty_entry)]
    assert target == [], "Empty Entry, no Items"

    target = [i for i in foobarstats.load(entry_no_stats)]
    assert target == no_stats_target, "Entry with Item, no playing data"

    target = [i for i in foobarstats.load(entries_correct_stats)]
    assert target == correct_stats_target, "Entry with Item, Item has playing data"

