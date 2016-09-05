from __future__ import unicode_literals

from helium import Element, Sensor


def test_elements(elements, first_element):
    assert len(elements) > 0
    assert first_element.id is not None


def test_timeseries(first_element):
    timeseries = first_element.timeseries()
    assert timeseries is not None


def test_metadata(first_element):
    metadata = first_element.metadata()
    assert metadata is not None


def test_meta(first_element):
    assert first_element.meta is not None


def test_include(client):
    elements = Element.all(client, include=[Sensor])
    for element in elements:
        sensors = element.sensors()
        included_sensors = element.sensors(use_included=True)
        assert set(sensors) == set(included_sensors)
