import pytest
from page_analyzer.parser import get_parse


@pytest.fixture
def mock_connect(mocker):
    mock_conn = mocker.MagicMock()
    mock_curs = mocker.MagicMock()
    mock_conn.cursor.return_value = mock_curs
    return mocker.patch("page_analyzer.db_requests.connect", return_value=mock_conn)


@pytest.fixture
def mock_get_url(mocker):
    return mocker.patch("page_analyzer.db_requests.get_url", return_value="https://test.com")


@pytest.fixture
def mock_requests_get(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = ("<html><head><title>Test Title</title></head><body>"
                          "<h1>Test H1</h1><meta name='description' "
                          "content='Test Description'></body></html>")
    return mocker.patch("requests.get", return_value=mock_response)


def test_get_parse(mock_get_url, mock_requests_get, mock_connect):
    status_code, h1, title, description = get_parse("https://test.com", "id")
    assert status_code == 200
    assert h1 == "Test H1"
    assert title == "Test Title"
    assert description == "Test Description"
