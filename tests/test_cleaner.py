from cleaner import clean


def test_multiple_spaces():
    result = clean("Hello     world")
    assert result == "Hello world"


def test_tabs():
    result = clean("Hello\t\tworld")
    assert result == "Hello world"


def test_windows_line_endings():
    result = clean("Line 1\r\nLine 2")
    assert result == "Line 1\nLine 2"


def test_empty_paragraphs():
    result = clean("Paragraph 1\n\n\nParagraph 2")
    assert result == "Paragraph 1\n\nParagraph 2"


def test_leading_and_trailing_spaces():
    result = clean("   Hello world   ")
    assert result == "Hello world"
