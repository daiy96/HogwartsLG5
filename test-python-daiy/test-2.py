import pytest
import yaml


def add_function(a, b):
    return a + b

@pytest.mark.parametrize("a,b,expected", [(3, 3, 6), (-1, -2, -3), (1000, 1000, 2000)], ids=["int", "minus", "bigint"])
def test_add(a, b, expected):
    assert add_function(a, b) == expected


def get_data():
    with open("./data.yml") as f:
        data = yaml.safe_load(f)
    print(data)
    div_data = data["data"]
    div_ids = data["myids"]
    return [div_data, div_ids]


def div_function(c, d):
    return c / d


@pytest.mark.parametrize("c,d,expecteds", get_data()[0],
                         ids=get_data()[1])
def test_div(c, d, expecteds):
    assert div_function(c, d) == expecteds
