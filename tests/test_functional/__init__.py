# -*- coding: utf-8 -*-
import pytest

from flask import app


def test_index(self):
    tester = app.test_client(self)
    response = tester.get("/")
    assert response.status_code == 200
