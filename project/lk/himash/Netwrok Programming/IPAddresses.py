# IP Address (Internet Protocol) is a fundamental networking concept that provides address
# assignation capability in a network. The python module ipaddress is used extensively to validate
# and categorize IP address to IPV4 and IPV6 type. It can also be used to do comparison of the IP
# address values as well as IP address arithmetic for manipulating the ip addresses.

# The u prefix in the code snippet ipaddress.IPv4Address(u'192.168.0.1')
# indicates that the string literal is a Unicode string. This is necessary for Python 3,
# which uses Unicode by default.
# Prior to Python 3, string literals were by default ASCII strings.
# This meant that they could only contain characters from the ASCII character set.
# Unicode strings, on the other hand, can contain characters from any language.

import ipaddress

print('Validate Ipv4 IP address ================')
print (ipaddress.ip_address(u'192.168.0.255'))
#invalid IPV4 address
# print (ipaddress.ip_address(u'192.168.0.256'))

print('Validate Ipv6 IP address ================')
print (ipaddress.ip_address(u'FFFF:9999:2:FDE:257:0:2FAE:112D'))
#invalid IPV6 address
# print (ipaddress.ip_address(u'FFFF:10000:2:FDE:257:0:2FAE:112D'))

print('Check type of IP address ================')
print(type(ipaddress.ip_address(u'192.168.0.255')))
print(type(ipaddress.ip_address(u'2001:db8::')))
print(ipaddress.ip_address(u'192.168.0.255').reverse_pointer)
print(ipaddress.ip_network(u'192.168.0.0/28'))

print('Compare IP address ================')
print(ipaddress.IPv4Address(u'192.168.0.2') > ipaddress.IPv4Address(u'192.168.0.1'))
print(ipaddress.IPv4Address(u'192.168.0.2') == ipaddress.IPv4Address(u'192.168.0.2'))
print(ipaddress.IPv4Address(u'192.168.0.2') != ipaddress.IPv4Address(u'192.168.0.1'))

print('Arithmetic operations with IP address ================')
print(ipaddress.IPv4Address(u'192.168.0.2') + 1)
print(ipaddress.IPv4Address(u'192.168.0.253') - 3)
# Increases the previous octet by value 1.
print(ipaddress.IPv4Address(u'192.168.10.253') + 3)
# Throws Value error
# print(ipaddress.IPv4Address(u'255.255.255.255') + 1)
