# NexaTech IT Home Lab

A self-built IT infrastructure lab designed to practice system administration, networking, security, monitoring, backup, and automation in a realistic company-style environment.

## Project Overview

This project simulates the IT infrastructure of a fictional company called **NexaTech GmbH**.

The lab is built on a Windows 11 Pro host using Hyper-V and contains a Linux server and Windows client connected through separate external and internal networks.

The goal is to build, configure, secure, monitor, troubleshoot, and automate a small IT environment from the ground up.

## Architecture

```text
Windows 11 Pro Host
        │
        ▼
     Hyper-V
        │
        ├── Linux Server
        │      ├── DNS (BIND9)
        │      ├── DHCP
        │      ├── SSH
        │      ├── UFW Firewall
        │      ├── Backup
        │      └── Python Monitoring
        │
        └── Windows Client

External Network
192.168.100.0/24
        │
        └── Internet / Physical Network

Internal Lab Network
10.10.10.0/24
        │
        ├── Linux Server: 10.10.10.1
        └── Windows Client: DHCP
```

## Technologies

* Windows 11 Pro
* Hyper-V
* Ubuntu Server
* Linux system administration
* TCP/IP networking
* DHCP
* DNS / BIND9
* SSH
* SSH key authentication
* UFW
* Bash / Linux command line
* Python
* psutil
* systemd
* Git
* GitHub

## Implemented Features

### Infrastructure

* Created a virtualized IT lab using Hyper-V
* Configured separate External and Internal virtual networks
* Installed and configured Ubuntu Server
* Configured static networking and routing
* Configured DHCP for the internal network

### DNS

Configured BIND9 as the internal DNS server.

Internal domain:

```text
nexatech.local
```

Example hostname:

```text
linux-server.nexatech.local
```

DNS configuration was validated using `named-checkconf`, `named-checkzone`, and `dig`.

### Linux Administration

Created dedicated users and groups:

```text
admin1
it-admins
```

Configured Linux file ownership and permissions using groups, `chmod`, and setgid directories.

### SSH Security

Configured SSH key-based authentication and hardened the SSH server by:

* Disabling password authentication
* Disabling direct root login
* Allowing public-key authentication

### Firewall

Configured UFW with a default-deny incoming policy.

Only required services and trusted network sources are allowed.

### Backup

Created configuration backups for important infrastructure components including:

* BIND9
* DHCP
* Netplan

Backup files are stored under:

```text
/var/backups/nexatech/
```

Restore testing and SHA-256 verification were also performed.

### Automated Monitoring

A Python-based health monitoring script checks:

* CPU usage
* Memory usage
* Disk usage
* SSH service
* DNS service
* DHCP service

The script uses thresholds to report:

```text
OK
WARNING
CRITICAL
```

Example:

```text
CPU Usage    : 0.3% [OK]
Memory Usage : 15.7% [OK]
Disk Usage   : 33.7% [OK]

SSH          : OK
DNS          : OK
DHCP         : OK

Overall Status: HEALTHY
```

The monitoring script also writes results to a log file.

### Automated Execution

The health check is integrated with `systemd`.

A `systemd service` executes the Python monitoring script, while a `systemd timer` runs it automatically every five minutes.

The monitoring workflow is:

```text
systemd timer
      ↓
health-check.service
      ↓
health_check.py
      ↓
System & Service Checks
      ↓
health_check.log
```

Failure detection was tested by intentionally stopping the SSH service. The monitoring system correctly detected the failure and recorded:

```text
CRITICAL | SSH FAIL
```

## Repository Structure

```text
it-home-lab/
├── docs/
│   └── infrastructure.md
├── network/
├── servers/
├── scripts/
│   └── health_check.py
├── screenshots/
└── README.md
```

## What I Practiced

This project provided hands-on practice with:

* Virtualization
* Linux administration
* Network configuration
* DHCP and DNS
* User and permission management
* SSH security
* Firewall configuration
* Backup and restore concepts
* Monitoring
* Python automation
* systemd services and timers
* Git and GitHub
* Technical documentation
* Troubleshooting

## Project Status

**Completed**

The core infrastructure, networking, security, backup, monitoring, automation, and documentation components of the lab have been implemented and tested.

## Next Step

The next project will build on this foundation by focusing more deeply on **IT automation with Python**, with an emphasis on practical system administration and infrastructure tasks.
