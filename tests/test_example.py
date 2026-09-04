def test_index(client):
    """根路由返回 running"""
    resp = client.get("/")
    assert resp.status_code == 200


def test_healthy(client):
    """/healthy 返回 JSON"""
    resp = client.get("/healthy")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data is not None
