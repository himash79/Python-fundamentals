# The IP addresses when translated to human readable formats or words become known as domain names.
# The translation of domain names to IP address is managed by the python module dnspython.
# This module also provides methods to find out CNAME and MX records.

# In the below program we find the ip address for the domain using the dns.resolver method.
# Usually this mapping between IP address and domain name is also known as 'A' record.

# A CNAME record also known as Canonical Name Record is a type of record in the Domain Name System
# (DNS) used to map a domain name as an alias for another domain. CNAME records always point to
# another domain name and never directly to an IP address. In the query method below we specify the
# CNAME parameter to get the CNAME value.

# A MX record also called mail exchanger record is a resource record in the Domain Name System that
# specifies a mail server responsible for accepting email messages on behalf of a recipient's domain.
# It also sets the preference value used to prioritizing mail delivery if multiple mail servers are available.
# Similar to above programs we can find the value for MX record using the 'MX' parameter in the query method.

print('Finding "A" record ===================')
# import dnspython as dns
import dns.resolver

result = dns.resolver.resolve('tutorialspoint.com', 'A')
for ipval in result:
    print('IP', ipval.to_text())

print('Finding CNAME value ===================')
result = dns.resolver.resolve('mail.google.com', 'CNAME')
for cnameval in result:
    print(' cname target address:', cnameval.target)

print('Finding MX record ===================')
result = dns.resolver.query('mail.google.com', 'MX')
for exdata in result:
    print(' MX Record:', exdata.exchange.text())