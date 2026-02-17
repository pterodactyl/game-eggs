# Numdrassl Proxy (Hytale)

Numdrassl is a high-performance proxy implementation for Hytale server networks.
It provides a centralized entry point for players and enables seamless connections between multiple backend servers (hub, survival, minigames, etc.).

This egg deploys the official Numdrassl proxy release using Java 21.

---

## Requirements

* Java 21 or newer (Java 21 LTS recommended)
* Public UDP port allocation
* Backend Hytale servers configured for proxy usage
* Firewall rules allowing UDP traffic on the configured port

---

## Server Ports

Numdrassl operates using the same transport model as Hytale and requires a single **UDP** port for gameplay traffic over **QUIC**.

| Port Type | Default |
| --------- | ------- |
| Proxy     | 5520    |

> ⚠ This server requires a **UDP allocation** in Pterodactyl.
> QUIC traffic will not function on TCP-only ports.

---

## Installation

During installation, this egg downloads the Numdrassl proxy jar from the configured release URL.

Default release:

```
https://github.com/Numdrassl/proxy/releases/download/2026.02.06-aa1b071c2-build.8/proxy-1.2.jar
```

The download URL may be modified in the server variables to update the proxy version.

---

## Startup Configuration

The server is launched using:

```
java -Xms128M -Xmx{{SERVER_MEMORY}}M -XX:+UseG1GC -XX:+ParallelRefProcEnabled -jar {{SERVER_JARFILE}}
```

---

## Variables

The following variables are available in this egg:

| Name            | Environment Variable | Default              | Description                                                                |
| --------------- | -------------------- | -------------------- | -------------------------------------------------------------------------- |
| Server Jar File | `SERVER_JARFILE`     | `proxy-1.2.jar`      | Name of the proxy jar file used at startup.                                |
| Download URL    | `DOWNLOAD_URL`       | Official release URL | Direct download link for the Numdrassl proxy jar used during installation. |

---

## Network Architecture Example

```
Players
   ↓ UDP (QUIC)
Numdrassl Proxy
   ↓
Hytale Hub
   ↓
Hytale Survival
```

---

## Security Recommendations

* Do not expose backend servers directly to the internet.
* Restrict backend access to the proxy's internal IP address.
* Use SSD/NVMe storage for optimal I/O performance.
* Monitor CPU usage — proxy performance benefits from strong single-core frequency.
