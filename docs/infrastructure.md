# IT Home Lab — NexaTech GmbH

## About This Project

This is my personal IT Home Lab, which I am building to gain practical experience in system administration, networking, security, and automation.

The lab simulates a small company environment for a fictional company called **NexaTech GmbH**.

I am using this project to learn by actually building, configuring, testing, and troubleshooting IT infrastructure instead of only studying the theory.

---

## What I Want to Learn

The main topics I am practicing in this lab are:

* Linux administration
* Windows administration
* Networking and TCP/IP
* DNS and DHCP
* Users, groups, and permissions
* Firewall and basic security
* Monitoring
* Backup
* IT troubleshooting
* Python automation
* Git and GitHub
* Technical documentation

---

## Current Lab

The lab currently consists of a Windows 11 Pro host running a Linux server as a virtual machine using Hyper-V.

```text
Windows 11 Pro
      │
      │ Hyper-V
      ▼
Linux Server
Ubuntu Server 26.04.1
      │
      ├── SSH
      ├── UFW Firewall
      └── BIND9 DNS
```

### Linux Server

* Hostname: `linux-server`
* OS: Ubuntu Server 26.04.1
* RAM: 4 GB
* vCPUs: 4
* Disk: 50 GB
* IP: `192.168.100.17`
* Network: `192.168.100.0/24`

---

## What I Have Done So Far

### 1. Linux Server

I installed and configured an Ubuntu Server virtual machine on Hyper-V.

I also learned how to check the server's network configuration, routing, memory usage, and running services.

---

## 2. Networking

The lab uses two separate virtual networks created with Hyper-V.

### External Network

The Linux Server is connected to the `HomeLab-External` virtual switch.

```text
Network:        192.168.100.0/24
Linux Server:   192.168.100.17
Gateway:        192.168.100.1
```

The server uses a static IP address on the external network.

The IP address is reserved on the home router based on the server's MAC address to prevent IP conflicts with the router's DHCP pool.

### Internal Network

A separate isolated network was created for communication between lab machines.

```text
Network:        10.10.10.0/24
Linux Server:   10.10.10.1
Windows Client: 10.10.10.100
```

The Linux Server provides DHCP for this internal network.

The DHCP server assigns addresses from:

```text
10.10.10.100 - 10.10.10.200
```

The Linux Server also provides DNS for the internal network.

### Interface Mapping

The network interfaces are identified by their MAC addresses to avoid depending on the interface names assigned by Linux.

```text
MAC ...:00 → HomeLab-External → 192.168.100.17
MAC ...:03 → HomeLab-Internal → 10.10.10.1
```

This approach ensures that the network roles remain consistent even if Linux assigns different interface names after a reboot.

### Network Validation

The network was tested step by step using:

```bash
ip -br addr
ip route
ping -c 4 192.168.100.1
```

The Windows Client was also tested against the Linux Server:

```text
Windows Client → 10.10.10.1
Windows Client → 192.168.100.17
```

DNS resolution was tested with:

```powershell
nslookup linux-server.nexatech.local
```

These tests helped me understand the relationship between:

* Network interfaces
* MAC addresses
* IP addresses
* Subnets
* Default gateways
* Routing
* DHCP
* DNS
* Internal and external networks

### Troubleshooting Example

After a reboot, the Linux interface names no longer matched the expected configuration.

Instead of assuming that `eth0` and `eth1` always represent the same physical/virtual adapters, I compared their MAC addresses and identified the correct network roles.

The Netplan configuration was then updated to match interfaces by MAC address.

This demonstrated an important troubleshooting principle:

> Verify the actual network state before changing the configuration.

---

### 3. SSH

I installed OpenSSH Server so that I can administer the Linux server remotely from Windows.

```bash
sudo systemctl enable --now ssh
systemctl is-active ssh
```

I can connect from Windows using SSH instead of working directly on the server console.

---

### 4. Users, Groups and Permissions

I created an administrator group and a user for practicing Linux access control.

```text
Group: it-admins
User: admin1
```

I also created:

```text
/srv/it-admins
```

and configured it so that members of the `it-admins` group can access it.

I practiced:

* Creating users
* Creating groups
* Adding users to groups
* Changing ownership
* Changing permissions
* Using `setgid`
* Testing access with a different user

---

### 5. Firewall

I configured UFW as the Linux firewall.

Before enabling the firewall, I allowed SSH access so that I would not lock myself out of the server.

```bash
sudo ufw allow ssh
sudo ufw enable
sudo ufw status
```

This also helped me understand that a working network connection does not automatically mean that a service is reachable.

---

### 6. Internal DNS

I installed BIND9 and created an internal DNS zone for the lab.

```text
nexatech.local
```

The current DNS record is:

```text
linux-server.nexatech.local
        ↓
192.168.100.17
```

The configuration files are:

```text
/etc/bind/named.conf.local
/etc/bind/db.nexatech.local
```

I validated the configuration with:

```bash
sudo named-checkconf
sudo named-checkzone nexatech.local /etc/bind/db.nexatech.local
```

And tested DNS resolution with:

```bash
dig @127.0.0.1 linux-server.nexatech.local
```

---

## My Troubleshooting Approach

One of the main things I want to learn from this project is **how to troubleshoot systematically**.

For example, if a client cannot reach a server, I don't want to immediately change random settings.

I want to check the problem layer by layer:

```text
Is the server running?
        ↓
Does the network interface work?
        ↓
Does the server have an IP address?
        ↓
Is the gateway reachable?
        ↓
Does external connectivity work?
        ↓
Does DNS work?
        ↓
Does the hostname resolve?
        ↓
Is the service running?
        ↓
Is the required port accessible?
        ↓
Does the firewall allow the connection?
        ↓
Are permissions/authentication correct?
```

This is one of the most important skills I am practicing with this project.

---

## Current Status

### Completed

* [x] Hyper-V setup
* [x] Ubuntu Server
* [x] Basic networking
* [x] SSH remote administration
* [x] Linux users and groups
* [x] Linux permissions
* [x] UFW firewall
* [x] BIND9
* [x] Internal DNS zone
* [x] DNS testing
* [x] Basic project documentation

### Next

* [ ] Windows Client VM
* [ ] Client ↔ Server communication
* [ ] DHCP
* [ ] More DNS records
* [ ] Monitoring
* [ ] Backup
* [ ] Security hardening
* [ ] Python automation

---

## Why I Am Building This

I am building this project as practical preparation for an IT Ausbildung in Germany, especially for:

* Fachinformatikerin für Systemintegration
* Fachinformatikerin für Anwendungsentwicklung

The project will continue to grow as I learn more about infrastructure, automation, programming, and troubleshooting.

## DHCP Configuration

A separate internal Hyper-V network was created for the lab environment.

### Internal Network

- Virtual Switch: `HomeLab-Internal`
- Network: `10.10.10.0/24`
- Linux Server (`eth1`): `10.10.10.1`

### DHCP Server

The Linux Server runs `isc-dhcp-server` on `eth1`.

## DHCP Configuration

A separate internal Hyper-V network was created for the lab environment.

### Internal Network

* Virtual Switch: `HomeLab-Internal`
* Network: `10.10.10.0/24`
* Linux Server (`eth1`): `10.10.10.1`

### DHCP Server

The Linux Server runs `isc-dhcp-server` on `eth1`.

DHCP configuration:

* DHCP range: `10.10.10.100 - 10.10.10.200`
* Subnet mask: `255.255.255.0`
* Default gateway: `10.10.10.1`
* DNS server: `10.10.10.1`

### Windows Client

The Windows Client successfully received its network configuration from the Linux DHCP server.

Example:

```text
IPv4 Address:    10.10.10.100
Subnet Mask:     255.255.255.0
Default Gateway: 10.10.10.1
```

### Validation

The following tests were performed successfully:

* DHCP address assignment
* DHCP lease renewal
* Windows Client → Linux Server ping
* DNS query from Windows Client to Linux Server

This confirms that the internal DHCP and DNS infrastructure is operational.
