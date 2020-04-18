import pytest
from mapsmx import MapsMX


def test_state_returns_data():
    try:
        MapsMX().get_geo('state')
    except BaseException:
        assert False, "Test state failed"

def test_state_w_centroids_returns_data():
    try:
        MapsMX().get_geo('state', add_centroids=True)
    except BaseException:
        assert False, "Test state with centroids failed"

def test_mun_returns_data():
    try:
        MapsMX().get_geo('municipality')
    except BaseException:
        assert False, "Test municipality failed"

def test_municipality_w_centroids_returns_data():
    try:
        MapsMX().get_geo('municipality', add_centroids=True)
    except BaseException:
        assert False, "Test municipality with centroids failed"
