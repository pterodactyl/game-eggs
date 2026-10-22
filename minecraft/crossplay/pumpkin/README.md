# Pumpkin

Pumpkin is a Minecraft server written in Rust with native Java and experimental Bedrock support.
It runs without a JVM and uses multiple CPU cores for parallel work.
Java and Bedrock players can share the same world without a separate proxy.

**Pumpkin is under heavy development. Expect incomplete features and bugs.**

[Pumpkin website](https://pumpkinmc.org/)
[Pumpkin GitHub](https://github.com/Pumpkin-MC/Pumpkin)

The egg sets `use_tty=false` in new configs to avoid [delayed console commands](https://github.com/Pumpkin-MC/Pumpkin/issues/3696).

## Server ports

Java uses the primary allocation. Bedrock requires an additional TCP/UDP allocation.

| Port | default | protocol |
|------|---------|----------|
| Java | 25565 | TCP |
| Bedrock | 19132 | TCP/UDP |

Bedrock LAN discovery on UDP 7551 is not exposed, and joining currently has a reported [NetherNet issue](https://github.com/Pumpkin-MC/Pumpkin/issues/3738).
