from vks_intelligence.tools.telegram_tool import format_digest


def test_format_digest_splits_single_long_line():
    messages = format_digest("x" * 9000, "", "", 3900)

    assert len(messages) == 3
    assert all(len(message) <= 3900 for message in messages)
