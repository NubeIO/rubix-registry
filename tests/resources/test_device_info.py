import unittest

from registry.models.model_device_info import DeviceInfoModel
from registry.resources.resource_device_info import put_device_info, get_device_info, get_device_info_dict


class TestUtils(unittest.TestCase):

    def test_put_device_info(self):
        device_info = put_device_info(DeviceInfoModel(client_id="client_id"))
        print(device_info)

    def test_get_device_info(self):
        device_info = get_device_info_dict()
        print(device_info)
