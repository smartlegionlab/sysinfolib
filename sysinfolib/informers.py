# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import getpass
import platform
import socket

import psutil
import requests


class ExternalIpGetter:
    def __init__(self, api_url='https://api.ipify.org'):
        self.url = api_url

    def get_external_ip(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            return f'Error! Failed to determine external IP. {e}'


class InternalIpGetter:
    def __init__(self, ip='8.8.8.8', port=80):
        self.ip = ip
        self.port = port

    def get_internal_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect((self.ip, self.port))
            internal_ip = s.getsockname()[0]
        except socket.error:
            internal_ip = 'Error! Failed to determine internal IP.'
        finally:
            s.close()
        return internal_ip


class IpInformer:
    _external = ExternalIpGetter()
    _internal = InternalIpGetter()

    @classmethod
    def get_external_ip(cls):
        return cls._external.get_external_ip()

    @classmethod
    def get_internal_ip(cls):
        return cls._internal.get_internal_ip()


class MemoryInfoGetter:

    @staticmethod
    def get_memory_info():
        return psutil.virtual_memory()

    @staticmethod
    def get_total_memory():
        return psutil.virtual_memory().total

    @staticmethod
    def get_available_memory():
        return psutil.virtual_memory().available

    @staticmethod
    def get_used_memory():
        return psutil.virtual_memory().used


class NetworkInfoGetter:
    @staticmethod
    def get_network_interfaces():
        return psutil.net_if_addrs()


class DiskInfoGetter:
    @staticmethod
    def get_disk_partitions():
        return psutil.disk_partitions()

    @staticmethod
    def get_disk_usage():
        disk_usage = {}
        for partition in psutil.disk_partitions():
            usage = psutil.disk_usage(partition.mountpoint)
            disk_usage[partition.device] = {
                'total': usage.total,
                'used': usage.used,
                'free': usage.free
            }
        return disk_usage


class SystemInfoGetter:

    @staticmethod
    def get_system_user_name():
        return getpass.getuser()

    @staticmethod
    def get_system_name():
        return platform.system()

    @staticmethod
    def get_node_name():
        return platform.node()

    @staticmethod
    def get_release_info():
        return platform.release()

    @staticmethod
    def get_version_info():
        return platform.version()

    @staticmethod
    def get_platform_info():
        return platform.platform()

    @staticmethod
    def get_machine_info():
        return platform.machine()

    @staticmethod
    def get_processor_info():
        return platform.processor()

    @staticmethod
    def get_cpu_info():
        return platform.processor()

    @staticmethod
    def get_disk_info():
        return psutil.disk_partitions()

    @staticmethod
    def get_memory_info():
        return psutil.virtual_memory()

    @staticmethod
    def get_network_interfaces():
        return psutil.net_if_addrs()

    @staticmethod
    def get_system_load():
        return psutil.getloadavg()

    @staticmethod
    def get_python_version():
        return platform.python_version()


class UserInfoGetter:
    def __init__(self, api_url='https://ipinfo.io/json'):
        self.api_url = api_url
        self.data: dict = self.__init()

    def __init(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            data: dict = response.json()
            del data['readme']
        else:
            data: dict = {
                'ip': '',
                'hostname': '',
                'city': '',
                'region': '',
                'country': '',
                'loc': '',
                'org': '',
                'postal': '',
                'timezone': ''
            }
        return data

    def get_ip_address(self):
        return self.data['ip']

    def get_hostname(self):
        return self.data['hostname']

    def get_city(self):
        return self.data['city']

    def get_region(self):
        return self.data['region']

    def get_country(self):
        return self.data['country']

    def get_loc(self):
        return self.data['loc']

    def get_org(self):
        return self.data['org']

    def get_postal(self):
        return self.data['postal']

    def get_timezone(self):
        return self.data['timezone']

    def all_user_info(self):
        return self.data


class SystemInformer:
    ip = IpInformer()
    memory = MemoryInfoGetter()
    network = NetworkInfoGetter()
    disk = DiskInfoGetter()
    system = SystemInfoGetter()
    user = UserInfoGetter()
