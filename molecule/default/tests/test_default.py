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


def test_webserver_open(host):
    assert host.socket("tcp://0.0.0.0:9100").is_listening


def test_webserver_is_webserver(host):
    command = "curl --digest -L -D - http://localhost:9100/"
    cmd = host.run(command)
    assert 'HTTP/1.1 200 OK' in cmd.stdout


def test_webserver_is_node_exporter(host):
    command = "curl http://localhost:9100/metrics"
    cmd = host.run(command)
    assert 'node_exporter_build_info' in cmd.stdout
    assert 'version="0.18.0"' in cmd.stdout
