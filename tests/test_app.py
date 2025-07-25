from lambda import app

def test_handler_returns_200():
    result = app.handler({}, {})
    assert result["statusCode"] == 200
