from cleaner import clean


def run_test(name, input_text, expected_output):
    result = clean(input_text)

    if result == expected_output:
        print(f"PASS: {name}")
    else:
        print(f"FAIL: {name}")
        print(f"Input:    {repr(input_text)}")
        print(f"Expected: {repr(expected_output)}")
        print(f"Got:      {repr(result)}")
        print()


run_test(
    "Multiple Spaces",
    "Hello     world",
    "Hello world"
)

run_test(
    "Tabs",
    "Hello\t\tworld",
    "Hello world"
)

run_test(
    "Windows Line Endings",
    "Line 1\r\nLine 2",
    "Line 1\nLine 2"
)

run_test(
    "Empty Paragraphs",
    "Paragraph 1\n\n\nParagraph 2",
    "Paragraph 1\n\nParagraph 2"
)

run_test(
    "Leading and Trailing Spaces",
    "   Hello world   ",
    "Hello world"
)