

def test_calculate_returns_bar(flask_test_client):
    # When
    subject = flask_test_client.get('/calculate')

    # Then
    assert subject.status_code == 200
