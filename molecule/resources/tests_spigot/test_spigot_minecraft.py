import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_minecraft_service_group_exists(host):
    f = host.group("spigot")
    assert f.exists


def test_minecraft_service_user_exists(host):
    f = host.user("spigot")
    assert f.group == 'spigot'


def test_server_dir_exists(host):
    f = host.file('/opt/minecraft/server/current')
    assert f.exists
    assert f.is_directory
    assert f.is_symlink
    assert f.linked_to == '/opt/minecraft/server/releases/1.9'


def test_server_jar_exists(host):
    f = host.file('/opt/minecraft/server/releases/1.9/spigot-1.9.jar')
    assert f.exists
    assert f.is_file
    assert f.user == 'spigot'
    assert f.group == 'spigot'


def test_server_symlink_exists(host):
    f = host.file('/opt/minecraft/server/shared/spigot.jar')
    assert f.is_symlink
    assert f.linked_to == '/opt/minecraft/server/releases/1.9/spigot-1.9.jar'


def test_eula_exists_exists(host):
    f = host.file('/opt/minecraft/server/shared/eula.txt')
    assert f.content == "eula=true"
    assert f.user == 'spigot'
    assert f.group == 'spigot'