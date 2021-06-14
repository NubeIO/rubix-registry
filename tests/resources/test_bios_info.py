import unittest

from registry.models.model_bios_info import BiosInfoModel
from registry.resources.resource_bios_info import put_bios_info, get_bios_info_dict


class TestUtils(unittest.TestCase):

    def test_put_bios_info(self):
        bios_info = put_bios_info(BiosInfoModel(port=1615))
        print(bios_info)

    def test_get_bios_info(self):
        bios_info = get_bios_info_dict()
        print(bios_info)
