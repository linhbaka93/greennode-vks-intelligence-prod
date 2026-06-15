from vks_intelligence.tools.telegram_tool import (
    format_telegram_html_messages,
    markdown_to_telegram_html,
)


def test_markdown_source_link_renders_as_named_html_link():
    html = markdown_to_telegram_html(
        "- [RSS] [Vietnam.vn](https://vietnam.vn/example) (2026-06-02) - Tin moi"
    )

    assert '<a href="https://vietnam.vn/example">Vietnam.vn</a>' in html
    assert "[RSS]" in html


def test_bare_url_is_compacted_to_domain_link():
    html = markdown_to_telegram_html(
        "Social fetch failed (https://www.facebook.com/greennode23): login wall"
    )

    assert '<a href="https://www.facebook.com/greennode23">facebook.com</a>' in html
    assert "https://www.facebook.com/greennode23):" not in html


def test_headings_are_presented_without_dropping_body_content():
    html = markdown_to_telegram_html(
        "# GreenNode VKS Intelligence — Daily Brief\n\n"
        "## Tin đã xác nhận\n\n"
        "- Ý quan trọng vẫn được giữ.\n"
        "## Phân tích chi tiết\n\n"
        "**Daily Intelligence Agent:** phân tích đầy đủ."
    )

    assert "<b>📌 GreenNode VKS Intelligence — Daily Brief</b>" in html
    assert "<b>✅ Tin đã xác nhận</b>" in html
    assert "Ý quan trọng vẫn được giữ." in html
    assert "<b>🧠 Phân tích chi tiết</b>" in html
    assert "<b>Daily Intelligence Agent:</b> phân tích đầy đủ." in html


def test_html_message_split_preserves_all_bullets():
    markdown = "# Report\n\n" + "\n".join(
        f"- Finding {idx:02d}: nội dung cần giữ nguyên." for idx in range(20)
    )

    chunks = format_telegram_html_messages(markdown, max_chars=500)
    joined = "\n".join(chunks)

    assert len(chunks) > 1
    assert all(len(chunk) <= 500 for chunk in chunks)
    for idx in range(20):
        assert f"Finding {idx:02d}" in joined
