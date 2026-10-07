# The Mythical Man-Month, 2027

*stormcos: an operating system, Kubernetes, storage and networking stack written by one person and a fleet of AI coding sessions.*

**63 repositories · 601,887 lines of shipped code · 90.7% Rust**

Counted from each repository's own source (`git ls-files`): code lines only (no blanks, no comments), **excluding tests**: test directories, fixtures and test data, benches, examples, vendored code, docs, and Rust's inline `#[cfg(test)]` modules. Build and deploy scripts count as each project's own code. Snapshot: 2026-10-07.

| Area | Repository | What it is | Main language | Rust | Code lines |
|---|---|---|---|---:|---:|
| product | [stormcos](https://github.com/glennswest/stormcos) | stormcos — the platform's one operating system. An image-based node OS | Shell | 6% | 7,486 |
| qa | [stormcos_qa](https://github.com/glennswest/stormcos_qa) | stormcos QA: test standard, runner (auto-files issues), and must-gather; tombstones failed images | Rust | 84% | 7,507 |
| boot | [stormbootx](https://github.com/glennswest/stormbootx) | A UEFI NVMe/TCP boot extension: boot a machine from a remote image with no kernel, no initramfs and no PXE | Rust | 95% | 9,100 |
| boot | [stormnic-e1000e](https://github.com/glennswest/stormnic-e1000e) | Rust no_std UEFI SNP driver for Intel e1000e (82574L, 82579, I217–I219), loaded by stormbootx | — | — | 0 |
| boot | [stormnic-i40e](https://github.com/glennswest/stormnic-i40e) | Rust no_std UEFI SNP driver for Intel i40e (X710, XL710, XXV710, X722), loaded by stormbootx | — | — | 0 |
| boot | [stormnic-igb](https://github.com/glennswest/stormnic-igb) | Rust no_std UEFI SNP driver for Intel igb (i350, i210/i211, 82576/82580), loaded by stormbootx | — | — | 0 |
| boot | [stormnic-ixgbe](https://github.com/glennswest/stormnic-ixgbe) | Rust no_std UEFI SNP driver for Intel 82599/X540/X552 10G, loaded by stormbootx | Rust | 100% | 4,333 |
| boot | [stormnic-mlx4](https://github.com/glennswest/stormnic-mlx4) | Rust no_std UEFI SNP driver for Mellanox ConnectX-3, loaded by stormbootx | Rust | 98% | 3,648 |
| boot | [stormnic-mlx5](https://github.com/glennswest/stormnic-mlx5) | Rust no_std UEFI SNP driver for Mellanox mlx5 (ConnectX-4/4 Lx/5/6), loaded by stormbootx | — | — | 0 |
| boot | [stormnic-realtek](https://github.com/glennswest/stormnic-realtek) | Rust no_std UEFI SNP driver for Realtek RTL8111/8168, RTL8125, RTL8126, loaded by stormbootx | — | — | 0 |
| boot | [stormnic-virtio](https://github.com/glennswest/stormnic-virtio) | Rust no_std UEFI SNP driver for virtio-net (modern, virtio 1.x), loaded by stormbootx | Rust | 97% | 2,597 |
| boot | [stormuefi](https://github.com/glennswest/stormuefi) | Read-only stormblock asset reader for UEFI — descriptor + extent map, resolved before the kernel exists | Rust | 94% | 1,693 |
| control-plane | [fastetcd](https://github.com/glennswest/fastetcd) | Rust, wire-compatible replacement for etcd v3. Multi-node Raft. Targets realtime / low-overhead environments. | Rust | 99% | 18,825 |
| control-plane | [rustkube](https://github.com/glennswest/rustkube) | K8s API-compatible container orchestrator in Rust | Rust | 98% | 31,703 |
| control-plane | [stormcert](https://github.com/glennswest/stormcert) | Certificate plane for the Storm platform - issue, renew, deliver, reload, verify. Rust. | Rust | 100% | 9,744 |
| control-plane | [stormlb](https://github.com/glennswest/stormlb) | Rust API/ingress VIP load balancer for the Storm stack — health-checked L4 + VRRP (L2) / BGP-anycast (L3). The pre-cluster control-plane LB. | Rust | 100% | 2,940 |
| network | [flowsdn](https://github.com/glennswest/flowsdn) | flowsdn is a Rust networking stack for stormcos, implementing a CNI plugin and | Rust | 99% | 46,307 |
| network | [network-operator](https://github.com/glennswest/network-operator) | Cluster Network Operator for the rustkube/stormcos stack — manages the Cilium CNI lifecycle from a Network CR (install/upgrade/reconcile/status). CNO-equivalent, in Rust. | Rust | 98% | 3,556 |
| network | [stormcoredns](https://github.com/glennswest/stormcoredns) | CoreDNS reimplemented in Rust: Corefile, plugin chain, and the full plugin set | Rust | 100% | 14,635 |
| network | [stormcos-cilium](https://github.com/glennswest/stormcos-cilium) | Cilium for stormcos: pinned by digest, converted to goldens, and tested | Shell | 0% | 660 |
| node | [cadvisor](https://github.com/glennswest/cadvisor) | Container metrics exporter (cadvisor-compatible) for the rustkube stack, in Rust | Rust | 97% | 5,303 |
| node | [rustkube-node](https://github.com/glennswest/rustkube-node) | Node level of rustkube (Rust Kubernetes): kubelet, kube-proxy, cni | Rust | 99% | 28,740 |
| node | [stormcast](https://github.com/glennswest/stormcast) | The emit half of the storm log path: one wire format, never blocking. | Rust | 100% | 407 |
| node | [stormimds](https://github.com/glennswest/stormimds) | Instance Metadata Service — the endpoint a guest asks who it is | Rust | 100% | 1,791 |
| node | [stormipmi](https://github.com/glennswest/stormipmi) | Bare-metal host management for stormcos: Redfish/IPMI power, discovery, PXE-free NVMe/TCP install, always-on SOL console — a rustkube operator | Rust | 100% | 11,132 |
| node | [stormpump](https://github.com/glennswest/stormpump) | The node's execution engine — start and stop, in milliseconds. PID1 and CRI-O replacement for stormcos. | Rust | 100% | 23,035 |
| node | [stormrdp](https://github.com/glennswest/stormrdp) | The server side of RDP, in Rust: VM consoles, Linux desktops and Windows | Rust | 84% | 7,069 |
| node | [stormvm](https://github.com/glennswest/stormvm) | First-class VMs on stormcos: the VM object, the hypervisor drivers, and everything a VM needs that stormpump and stormblock do not own. | Rust | 100% | 10,605 |
| node | [vmcloud-image-operator](https://github.com/glennswest/vmcloud-image-operator) | The cloud-image catalogue and golden lifecycle for a stormcos cluster. On a | Rust | 100% | 5,109 |
| storage | [fio.dos.rs](https://github.com/glennswest/fio.dos.rs) | Async userspace file I/O into FAT12/FAT16/FAT32 — read and write files with no kernel, no mount, no loop device | Rust | 100% | 1,525 |
| storage | [fio.ext4.rs](https://github.com/glennswest/fio.ext4.rs) | Async userspace file I/O into ext2/ext3/ext4 — read and write files with no kernel, no mount, no loop device | Rust | 100% | 3,282 |
| storage | [fio.xfs.rs](https://github.com/glennswest/fio.xfs.rs) | Async userspace file I/O into XFS — read and write files with no kernel, no mount, no loop device | Rust | 100% | 4,558 |
| storage | [mkfs.dos.rs](https://github.com/glennswest/mkfs.dos.rs) | Async FAT12/FAT16/FAT32 formatter and checker in pure Rust — a from-scratch reimplementation of mkfs.fat and fsck.fat | Rust | 100% | 3,040 |
| storage | [mkfs.ext4.rs](https://github.com/glennswest/mkfs.ext4.rs) | Async, parallel ext2/ext3/ext4 formatter and checker in pure Rust — a from-scratch reimplementation of mke2fs and e2fsck | Rust | 100% | 11,420 |
| storage | [mkfs.xfs.rs](https://github.com/glennswest/mkfs.xfs.rs) | Async XFS formatter and checker in pure Rust — a from-scratch reimplementation of mkfs.xfs and xfs_repair -n | Rust | 100% | 3,311 |
| storage | [stormblock](https://github.com/glennswest/stormblock) | Pure Rust enterprise block storage engine — NVMe-oF/TCP + iSCSI targets with software RAID | Rust | 91% | 77,685 |
| storage | [stormblock-csi](https://github.com/glennswest/stormblock-csi) | A CSI driver and a wandering-RAID1 operator for StormBlock, in Rust. A | Rust | 99% | 7,188 |
| storage | [stormblock-registry](https://github.com/glennswest/stormblock-registry) | An OCI registry that turns each pushed image into a golden: a sealed | Rust | 99% | 23,649 |
| storage | [stormdrive](https://github.com/glennswest/stormdrive) | Physical drive management for one storage node. stormdrive knows what the | Rust | 91% | 15,435 |
| storage | [stormstorage](https://github.com/glennswest/stormstorage) | The storage control plane across Storm nodes and clusters. | Rust | 93% | 8,782 |
| platform | [baremetalservices](https://github.com/glennswest/baremetalservices) | Bootable image to handle hardware discovery, and configuration | Go | 0% | 2,520 |
| platform | [stormcluster](https://github.com/glennswest/stormcluster) | stormcos day-2 cluster operator: discover peers, form a cluster (masters/workers), join and split nodes (a split node reverts to SNO) | Rust | 100% | 6,228 |
| platform | [stormupdate](https://github.com/glennswest/stormupdate) | stormcos updater: watch the release catalog and upgrade a running cluster to the next release, every level (OS pallets, kernel, goldens, Kubernetes), node by node with drain, health gates and rollback | Rust | 100% | 4,172 |
| options | [irondirectory](https://github.com/glennswest/irondirectory) | A FIPS-compliant, Active Directory–compatible identity provider written in | Rust | 99% | 9,429 |
| options | [irondirectory-operator](https://github.com/glennswest/irondirectory-operator) | stormcos operator for irondirectory: instances, drives, fleet | Rust | 100% | 1,320 |
| options | [nextnfs](https://github.com/glennswest/nextnfs) | High-performance, standalone NFSv4.0/4.1 server over a real filesystem, written in Rust. Runs as a static musl binary… | Rust | 95% | 18,715 |
| options | [nextnfs-operator](https://github.com/glennswest/nextnfs-operator) | stormcos operator for nextnfs: instances, drives, fleet | Rust | 100% | 1,304 |
| options | [rocketsmbd](https://github.com/glennswest/rocketsmbd) | High-performance smbd replacement in Rust: io_uring end-to-end, zero-copy file-to-socket | Rust | 91% | 7,975 |
| options | [rocketsmbd-operator](https://github.com/glennswest/rocketsmbd-operator) | stormcos operator for rocketsmbd: instances, drives, fleet | Rust | 100% | 1,921 |
| options | [stormcos-options](https://github.com/glennswest/stormcos-options) | stormcos operator for stormcos: instances, drives, fleet | Rust | 97% | 1,698 |
| ui | [stormcentral](https://github.com/glennswest/stormcentral) | StormCOS mission control: component issues and releases, and a Claude session per project | Rust | 84% | 39,018 |
| ui | [stormconsole](https://github.com/glennswest/stormconsole) | StormCOS web console — pluggable OpenShift-style console built on stormd and stormview | Rust | 54% | 30,859 |
| ui | [stormrfb](https://github.com/glennswest/stormrfb) | RFB (RFC 6143) in Rust — sans-I/O codec, a client for stormconsole and a server for the Rust VMM's display | Rust | 67% | 4,120 |
| ui | [stormview](https://github.com/glennswest/stormview) | The storm view contract and UI system: one shape every storm daemon | Svelte | 10% | 1,925 |
| tooling | [buildbox2](https://github.com/glennswest/buildbox2) | The build environment as a golden: dev's toolchains on Fedora 44, one VM per build | Shell | 0% | 344 |
| tooling | [minismbd](https://github.com/glennswest/minismbd) | Admin/boot-media SMB server: read-only, client allowlist, SMB1+SMB2, time-boxed — spun off rocketsmbd | Rust | 100% | 6,112 |
| tooling | [sc](https://github.com/glennswest/sc) | One binary for a StormCOS fleet, covering three surfaces an operator should | Rust | 98% | 2,867 |
| tooling | [stormd](https://github.com/glennswest/stormd) | A container init for scratch images: one static binary that is PID 1, | Rust | 92% | 13,349 |
| infra | [dellsw](https://github.com/glennswest/dellsw) | Configuration and operational notes for Dell EMC ONIE-based switches in the home lab. | Shell | 0% | 632 |
| not yet in an area | [sectionsystems](https://github.com/glennswest/sectionsystems) | sectionsystems: StormCOS operator that verifies each node against the manifest it carries, at boot and at unpredictable intervals; serves sc verify and a status endpoint | Rust | 100% | 2,289 |
| not yet in an area | [storminstall](https://github.com/glennswest/storminstall) | StormCOS installer: author install-config.yaml (TUI), write it into the boot ISO's config volume, download the ISO and sc, and watch the first node's install — Linux, macOS, Windows | Rust | 97% | 4,325 |
| not yet in an area | [stormpanel](https://github.com/glennswest/stormpanel) | stormpanel: a graphical node status panel drawn directly on the console with KMS/DRM — temperatures, CPU, memory, disks, network, power, storage and cluster health, for servers and laptops | Rust | 100% | 4,047 |
| not yet in an area | [stormraid](https://github.com/glennswest/stormraid) | stormraid: high-performance RAID for pve and stormcos: writes at RAID0 speed with ECC written alongside the data, asynchronous ECC verification, and three-level bit-rot checking | Rust | 81% | 18,918 |

| | **Total** | | | **90.7%** | **601,887** |

## By language (shipped code)

| Language | Code lines | Share |
|---|---:|---:|
| Rust | 545,998 | 90.7% |
| Shell | 22,541 | 3.7% |
| Svelte | 16,111 | 2.7% |
| Python | 8,969 | 1.5% |
| JavaScript | 3,898 | 0.6% |
| Go | 2,025 | 0.3% |
| CSS | 1,503 | 0.2% |
| HTML | 842 | 0.1% |

The five newest NIC-driver repositories (stormnic-igb, -e1000e, -i40e, -mlx5, -realtek) were created on 2026-10-07 and hold no code yet.
