import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_binary_file_exist(host):
    f = host.file('/usr/sbin/node_exporter')
    assert f.exists
    assert f.user == 'prometheus'
    assert f.group == 'prometheus'


def test_service_file_exist(host):
    f = host.file('/etc/systemd/system/node_exporter.service')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_service_running(host):
    service = host.service('node_exporter')
    assert service.is_running
