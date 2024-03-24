import pytest
from page_analyzer.url_validation import (
    url_normalization,
    url_validation
)


@pytest.mark.parametrize("url, output", [
    ("https://Test.com/", "https://test.com"),
    ("http://test.com/dir/file", "http://test.com")
])
def test_url_normalization(url, output):
    assert url_normalization(url) == output


@pytest.mark.parametrize("url, error", [
    ("http://test.com", None),
    ("http://test.com/dir/file", None),
    ("test.com", "Некорректный URL"),
    ("http://test.com/very/very/long_url/over/255/" + "text" * 60,
     "URL превышает 255 символов")
])
def test_url_validation(url, error):
    assert url_validation(url) == error
