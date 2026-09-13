# IT Home Lab — NexaTech GmbH

## About This Project

This is my personal IT Home Lab, which I am building to gain practical experience in system administration, networking, security, and automation.

The lab simulates a small company environment for a fictional company called **NexaTech GmbH**.

The main goal of this project is to learn by building, configuring, testing, and troubleshooting real IT infrastructure.

---

## Goals

Through this project, I want to gain practical experience with:

* Linux administration
* Windows administration
* Networking and TCP/IP
* DNS and DHCP
* Users, groups, and permissions
* Firewalls and basic security
* Monitoring
* Backup
* IT troubleshooting
* Python automation
* Git and GitHub
* Technical documentation

---

## Lab Overview

The lab is built on a Windows 11 Pro host using Hyper-V for virtualization.

The current environment includes an Ubuntu Server virtual machine that provides the first infrastructure services for the lab.

```text
Windows 11 Pro
      │
      │ Hyper-V
      ▼
Linux Server
Ubuntu Server
      │
      ├── SSH
      ├── UFW Firewall
      └── BIND9 DNS
```

The lab will be expanded gradually as I learn and implement additional technologies.

---

## Technologies & Topics

### Operating Systems

* Windows 11
* Ubuntu Server

### Virtualization

* Hyper-V

### Networking

* TCP/IP
* IPv4
* Subnets
* Routing
* DNS
* DHCP

### Linux

* Users and groups
* File permissions
* SSH
* Services
* Package management
* Firewall

### Automation

* Python
* Bash

### Tools

* Git
* GitHub
* PowerShell

---

## Current Status

### Completed

* [x] Hyper-V environment
* [x] Ubuntu Server installation
* [x] Basic network configuration
* [x] SSH remote administration
* [x] Linux users and groups
* [x] Linux permissions
* [x] UFW firewall
* [x] BIND9 DNS
* [x] Internal DNS zone
* [x] Initial infrastructure documentation

### Next

* [ ] Windows Client VM
* [ ] Client ↔ Server communication
* [ ] DHCP
* [ ] Additional DNS records
* [ ] Monitoring
* [ ] Backup
* [ ] Security hardening
* [ ] Python automation

---

## Repository Structure

```text
it-home-lab/
│
├── docs/
│   └── infrastructure.md
│
├── network/
│
├── servers/
│
├── scripts/
│
├── screenshots/
│
└── README.md
```

The repository structure will grow as the lab becomes more complex.

---

## Documentation

Detailed technical documentation is available in the `docs/` directory.

* [Infrastructure Documentation](docs/infrastructure.md)

---

## Why I Am Building This

I am building this project as practical preparation for an IT Ausbildung in Germany, especially for:

* Fachinformatikerin für Systemintegration
* Fachinformatikerin für Anwendungsentwicklung

The project is intended to demonstrate not only what technologies I have used, but also how I approach configuration, troubleshooting, documentation, and automation.

---

## Project Status

🚧 **In development**

This project will continue to evolve as I learn and add new components to the lab.
