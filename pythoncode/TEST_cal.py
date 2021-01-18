import pytest
import yaml

from pythonProject.pythoncode.cal import Cal


def get_datas():
    with open("./datas.yml") as f:
        datas = yaml.safe_load(f)
        add_datas = datas["add"]
        sub_datas = datas["sub"]
        mul_datas = datas["mul"]
        div_datas = datas["div"]
        return [add_datas, sub_datas, mul_datas, div_datas]


class ca:
    def setup_class(self):
        self.ca = Cal()
        print("\n开始计算")

    def teardown_class(self):
        print("\n结束计算")


@pytest.mark.parametrize("a, b, expect", get_datas()[0])
def add_fun(self, a, b, expect):
    result = self.cal.add(a, b)
    assert result == expect


@pytest.mark.parametrize("a, b, expect", get_datas()[1])
def sub_fun(self, a, b, expect):
    result = self.cal.sub(a, b)
    assert result == expect


@pytest.mark.parametrize("a, b, expect", get_datas()[2])
def mul_fun(self, a, b, expect):
    result = self.cal.mul(a, b)
    assert result == expect


@pytest.mark.parametrize("a, b, expect", get_datas()[3])
def div_fun(self, a, b, expect):
    result = self.cal.div(a, b)
    assert result == expect
