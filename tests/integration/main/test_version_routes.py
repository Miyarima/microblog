"""
Test routes for routes for previewing the currently running version of microblog
"""
# pylint: disable=redefined-outer-name,unused-argument

def test_version_page(client):
    """
    Test that correct info and post are displayed on user profile.
    """
    response = client.get("/version")
    assert response.status_code == 200
    assert b"This website is currently running" in response.data
