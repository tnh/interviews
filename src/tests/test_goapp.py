import pytest
import requests


def test_helloworld():
    resp = requests.get("http://app:8000/")
    assert resp.status_code == 200
    assert resp.text == "Hello, world."


def test_go():
    resp = requests.get("http://app:8000/go")
    assert resp.status_code == 200
    assert (
        resp.text
        == "Don't communicate by sharing memory, share memory by communicating."
    )


def test_opt():
    resp = requests.get("http://app:8000/opt")
    assert resp.status_code == 200
    assert (
        resp.text
        == "Don't communicate by sharing memory, share memory by communicating."
    )
