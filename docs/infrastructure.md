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


### DHCP Troubleshooting

After a server reboot, the DHCP service failed to start.

The issue was caused by the DHCP server being configured to use the wrong network interface.

The Linux network configuration had changed so that:

* `eth0` → HomeLab-Internal → `10.10.10.1`
* `eth1` → HomeLab-External → `192.168.100.17`

However, `/etc/default/isc-dhcp-server` was still configured with:

```text
INTERFACESv4="eth1"
```

The configuration was corrected to:

```text
INTERFACESv4="eth0"
```

After restarting the service, DHCP became active again.

The Windows Client was then tested using DHCP and successfully received:

* IPv4 address: `10.10.10.100`
* Subnet mask: `255.255.255.0`
* Default gateway: `10.10.10.1`

This demonstrated the importance of verifying the actual network interface mapping after changes to a virtualized network environment.

### DNS Records

The internal DNS zone `nexatech.local` is hosted on the Linux Server using BIND9.

Current DNS records include:

* `linux-server.nexatech.local` → `192.168.100.17`
* `dns.nexatech.local` → CNAME → `linux-server.nexatech.local`

The CNAME record provides an alias for the Linux Server.

### DNS Validation

DNS resolution was tested from both the Linux Server and the Windows Client.

The Windows Client successfully resolved:

```text
dns.nexatech.local
        ↓
linux-server.nexatech.local
        ↓
192.168.100.17
```

This confirmed that the internal DNS server and the CNAME record are working correctly.

## Network Troubleshooting

The lab network was validated step by step from the Windows Client to the Linux Server.

### Validation Steps

1. **IP Configuration**

   The Windows Client received:

   * IPv4: `10.10.10.100`
   * Subnet Mask: `255.255.255.0`
   * Default Gateway: `10.10.10.1`

2. **Network Connectivity**

   The Linux Server was reachable from the Windows Client using ICMP:

   ```text
   Windows Client → 10.10.10.1
   ```

3. **DNS Resolution**

   The Windows Client successfully resolved:

   ```text
   linux-server.nexatech.local → 192.168.100.17
   ```

4. **TCP Connectivity**

   TCP port 22 was tested from the Windows Client:

   ```powershell
   Test-NetConnection linux-server.nexatech.local -Port 22
   ```

   The result was:

   ```text
   TcpTestSucceeded : True
   ```

5. **SSH Authentication**

   The Windows Client successfully connected to the Linux Server using SSH:

   ```text
   ssh admin1@linux-server.nexatech.local
   ```

### Troubleshooting Approach

The network was tested from the lower layers to the application/service layer:

```text
IP Configuration
        ↓
Network Connectivity
        ↓
DNS Resolution
        ↓
TCP Port Connectivity
        ↓
Service / Authentication
```

This approach helps isolate network and service problems systematically instead of changing multiple configurations at the same time.

## Backup

The Linux Server configuration is backed up to:

```text
/var/backups/nexatech/
```

The backup contains important infrastructure configuration files from:

* `/etc/bind/`
* `/etc/dhcp/`
* `/etc/netplan/`

The configuration files are stored in a compressed archive:

```text
nexatech-configs.tar.gz
```

### Backup Security

The backup directory is restricted to the `root` user:

```text
drwx------
```

This prevents regular users from accessing or modifying the backup files.

### Restore Test

The backup archive was extracted into a temporary directory without modifying the active system configuration.

The following files were successfully restored:

* BIND9 configuration
* DHCP configuration
* Netplan configuration

### Integrity Check

A SHA-256 checksum was generated for the backup archive using:

```bash
sudo sha256sum /var/backups/nexatech/nexatech-configs.tar.gz
```

This checksum can be used to verify that the backup file has not been modified or corrupted.

## SSH Security Hardening

SSH access to the Linux Server was hardened using key-based authentication.

### Initial Configuration

The initial SSH configuration allowed password authentication:

```text
PermitRootLogin prohibit-password
PasswordAuthentication yes
PubkeyAuthentication yes
```

This meant that the `admin1` account could authenticate using a password over SSH.

### SSH Key Authentication

An Ed25519 SSH key pair was generated on the Windows Client.

The public key was added to the `admin1` account on the Linux Server:

```text
~/.ssh/authorized_keys
```

The SSH key was tested successfully before disabling password authentication.

The private key remains on the Windows Client and is not stored in the Git repository.

### Hardening Changes

SSH was configured with:

```text
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
```

This prevents:

* Direct SSH login as `root`
* Password-based SSH authentication

SSH access remains available through public-key authentication.

### Validation

The SSH configuration was validated with:

```bash
sudo sshd -t
```

The effective SSH configuration was checked with:

```bash
sudo sshd -T | grep -E '^(permitrootlogin|passwordauthentication|pubkeyauthentication)'
```

The final configuration confirmed:

```text
permitrootlogin no
passwordauthentication no
pubkeyauthentication yes
```

A new SSH connection from the Windows Client was then tested successfully using the Ed25519 private key.

### Troubleshooting Approach

The SSH hardening was performed in a safe order:

```text
Create SSH Key
      ↓
Install Public Key
      ↓
Test Key Authentication
      ↓
Validate SSH Configuration
      ↓
Disable Password Authentication
      ↓
Test New SSH Connection
```

Password authentication was not disabled until key-based authentication had been verified.

This reduces the risk of losing remote access during SSH hardening.


## Firewall Hardening

The Linux Server uses UFW (Uncomplicated Firewall) to control incoming network traffic.

### Default Policy

Incoming traffic is denied by default:

```text
Default: deny (incoming)
Default: allow (outgoing)
```

Only required services are explicitly allowed.

### Allowed Services

The internal lab network is:

```text
10.10.10.0/24
```

SSH and DNS access are restricted to this network:

```text
10.10.10.0/24 → TCP 22 → SSH
10.10.10.0/24 → Port 53 → DNS
```

This prevents unrestricted access from other networks.

### Validation

The firewall configuration was verified with:

```bash
sudo ufw status verbose
```

The final configuration showed:

```text
22/tcp → ALLOW IN → 10.10.10.0/24
53     → ALLOW IN → 10.10.10.0/24
```

Connectivity was then tested from the Windows Client using:

```powershell
Test-NetConnection 10.10.10.1 -Port 22
Test-NetConnection 10.10.10.1 -Port 53
```

Both tests succeeded.

### Security Principle

The firewall follows the principle of least privilege:

Only the network traffic required for the lab services is allowed, while other incoming traffic remains blocked by the default policy.
