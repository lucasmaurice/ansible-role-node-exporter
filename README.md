
## Ansible Role: prometheus-node-exporter [![Build Status](https://travis-ci.org/lucasmaurice/ansible-role-node-exporter.svg?branch=master)](https://travis-ci.org/lucasmaurice/ansible-role-node-exporter)


An Ansible role that installs Prometheus Node Exporter on Ubuntu|Debian|Redhat-based machines.

## Requirements

All needed packages will be installed with this role.

## Role Variables

Available variables are listed below, along with default values (see defaults/main.yml):

```yaml
---
# Node exporter default user and group
NODE_EXPORTER_USER: prometheus
NODE_EXPORTER_GROUP: prometheus

# Node exporter base configurations
NODE_EXPORTER_DIST_DIR: /tmp/exporters/dist
NODE_EXPORTER_BIN_DIR: /usr/sbin

# Node exporter version
NODE_EXPORTER_VERSION: 0.18.0

# https://github.com/prometheus/node_exporter#enabled-by-default
NODE_EXPORTER_ENABLED_COLLECTORS: []

# https://github.com/prometheus/node_exporter#disabled-by-default
NODE_EXPORTER_DISABLED_COLLECTORS: []

NODE_EXPORTER_CONFIG_FLAGS:
  'web.listen-address': '0.0.0.0:9100'
  'log.level': 'info'
```

- `NODE_EXPORTER_USER`: User used for install and run Node Exporter.

- `NODE_EXPORTER_GROUP`: Group used for install and run Node Exporter.

- `NODE_EXPORTER_DIST_DIR`: Temp path used for installation.

- `NODE_EXPORTER_BIN_DIR`: The path where install Node Exporter.

- `NODE_EXPORTER_VERSION`: The version of Node Exporter to install.

- `NODE_EXPORTER_ENABLED_COLLECTORS`: Collectors that are disabled by default to enable. [List of disabled collectors](https://github.com/prometheus/node_exporter#disabled-by-default)

- `NODE_EXPORTER_DISABLED_COLLECTORS`: Collectors that are enabled by default to disable. [List of enabled collectors](https://github.com/prometheus/node_exporter#enabled-by-default)

- `NODE_EXPORTER_CONFIG_FLAGS`: The welcome word.

Example Playbook
----------------

This is an example of how to use this role:

```yaml
- hosts: servers
	roles:
		- role: undergreen.prometheus-node-exporter
			prometheus_node_exporter_version: 0.17.0
			prometheus_node_exporter_enabled_collectors:
				- conntrack
				- cpu
				- diskstats
				- entropy
				- filefd
				- filesystem
				- loadavg
				- mdadm
				- meminfo
				- netdev
				- netstat
				- stat
				- textfile
				- time
				- vmstat
			prometheus_node_exporter_config_flags:
				'web.listen-address': '0.0.0.0:9100'
				'log.level': 'info'
```

## Note:

Due to [prometheus/node_exporter#640](https://github.com/prometheus/node_exporter/pull/640) and [prometheus/node_exporter#639](https://github.com/prometheus/node_exporter/pull/639) changes, this role can only support the minimum version 0.15 of node_exporter.

## License

WTFPL
