#!/usr/bin/env python3
import fileinput, subprocess
filename = "/etc/sysctl.conf"
class kernel():
  def replacevalue(a ,b):
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
      for line in file:
        print(line.replace(a, b), end='')
  def network():
    net = kernel.replacevalue
    net("net.ipv4.ip_forward = 1", "net.ipv4.ip_forward = 0")# Controls IP packet forwarding
    net("net.ipv4.conf.default.accept_source_route = 1", "net.ipv4.conf.default.accept_source_route = 0")# Do not accept source routing
    net("kernel.sysrq = 1", "kernel.sysrq = 0")# Controls the System Request debugging functionality of the kernel
    net("kernel.core_uses_pid = 0", "kernel.core_uses_pid = 1")# Controls whether core dumps will append the PID to the core filename. Useful for debugging multi-threaded applications
    net("net.ipv4.tcp_syncookies = 0", "net.ipv4.tcp_syncookies = 1")# Turn on SYN-flood protections
    net("net.ipv4.tcp_synack_retries = \* ", "net.ipv4.tcp_synack_retries = 5")# Controls the use of TCP syncookies. Turn on SYN-flood protections
    net("net.ipv4.conf.all.send_redirects = 1", "net.ipv4.conf.all.send_redirects = 0")# Send redirects, if router, but this is just server. So no routing allowed.
    net("net.ipv4.conf.default.send_redirects = 1", "net.ipv4.conf.default.send_redirects = 0")
    net("net.ipv4.conf.all.accept_source_route = 1", "net.ipv4.conf.all.accept_source_route = 0")# Accept packets with SRR option? No
    # Accept Redirects? No, this is not router
    net("net.ipv4.conf.all.accept_redirects = 1", "net.ipv4.conf.all.accept_redirects = 0")
    net("net.ipv4.conf.all.secure_redirects = 1", "net.ipv4.conf.all.secure_redirects = 0")
    net("net.ipv4.conf.all.log_martians = 0", "net.ipv4.conf.all.log_martians = 1")
    net("net.ipv4.conf.default.accept_source_route = 1", "net.ipv4.conf.default.accept_source_route = 0")
    net("net.ipv4.conf.default.accept_redirects = 1", "net.ipv4.conf.default.accept_redirects = 0")
    net("net.ipv4.conf.default.secure_redirects = 1", "net.ipv4.conf.default.secure_redirects = 0")# Ignore all ICMP ECHO and TIMESTAMP requests sent to it via broadcast/multicast
    net("net.ipv4.icmp_echo_ignore_broadcasts = 0", "net.ipv4.icmp_echo_ignore_broadcasts = 1 ")# Prevent against the common 'syn flood attack'
    net("net.ipv4.tcp_syncookies = 0", "net.ipv4.tcp_syncookies = 1")# Enable source validation by reversed path, as specified in RFC1812
    net("net.ipv4.conf.all.rp_filter = 0", "net.ipv4.conf.all.rp_filter = 1")# Controls source route verification
    net("net.ipv4.conf.default.rp_filter = 0", "net.ipv4.conf.default.rp_filter = 1 ")# Number of Router Solicitations to send until assuming no routers are present. This is host and not router
    net("net.ipv6.conf.default.router_solicitations = 1", "net.ipv6.conf.default.router_solicitations = 0") # Accept Router Preference in RA?
    net("net.ipv6.conf.default.accept_ra_rtr_pref = 1", "net.ipv6.conf.default.accept_ra_rtr_pref = 0 ")# Learn Prefix Information in Router Advertisement
    net("net.ipv6.conf.default.accept_ra_pinfo = 1 ", "net.ipv6.conf.default.accept_ra_pinfo = 0 ")# Setting controls whether the system will accept Hop Limit settings from a router advertisement
    net("net.ipv6.conf.default.accept_ra_defrtr = 1", "net.ipv6.conf.default.accept_ra_defrtr = 0 ")#router advertisements can cause the system to assign a global unicast address to an interface
    net("net.ipv6.conf.default.autoconf = 1 ", "net.ipv6.conf.default.autoconf = 0 ")#how many neighbor solicitations to send out per address?
    net("net.ipv6.conf.default.dad_transmits = 1 ", "net.ipv6.conf.default.dad_transmits = 0 ")# How many global unicast IPv6 addresses can be assigned to each interface?
    net("net.ipv6.conf.default.max_addresses = 0 ", "net.ipv6.conf.default.max_addresses = 1 ")
    net("kernel.exec-shield = 0", "kernel.exec-shield = 2")
    net("kernel.randomize_va_space = 0","kernel.randomize_va_space = 1")
    net("kernel.randomize_va_space = 1", "kernel.randomize_va_space = 2") # TCP and memory optimization
    net("net.ipv4.tcp_rmem = \* ", "net.ipv4.tcp_rmem = 4096 87380 8388608")
    net("net.ipv4.tcp_wmem = \*", "net.ipv4.tcp_wmem = 4096 87380 8388608") # increase Linux auto tuning TCP buffer limits
    net("net.core.rmem_max = \*", "net.core.rmem_max = 8388608")
    net("net.core.wmem_max =\*", "net.core.wmem_max = 8388608")
    net("net.core.netdev_max_backlog = \*", "net.core.netdev_max_backlog = 5000")
    net("net.ipv4.tcp_window_scaling = 0", "net.ipv4.tcp_window_scaling = 1") # increase system file descriptor limit
    net("net.ipv4.icmp_ignore_bogus_error_responses=0", "net.ipv4.icmp_ignore_bogus_error_responses=1")
  def physical():
     phy = kernel.replacevalue
     phy("kernel.panic= \8", "kernel.panic=10")
     phy("kernel.randomize_va_space=1","kernel.randomize_va_space=2")
     phy("fs.protected_hardlinks=0", "fs.protected_hardlinks=1")
     phy("fs.protected_symlinks=0", "fs.protected_symlinks=1")

kernel.network()
kernel.physical()
subprocess.call(['sysctl','-p'], shell=False)

