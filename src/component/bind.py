from component.base_component import BaseComponent
import iscpy
import string


class BIND(BaseComponent):
    '''
    BIND component handles all BIND commands and DNS works
    '''

    def __init__(self):
        ''' Init BIND instance '''

        super().__init__()

    def init(self):
        self.run_command("yum -y install bind bind-utils")

    def set_default(self):
        ''' Sets the default settings '''

        # Backup named.conf
        self.run_command("cp /etc/named.conf /etc/named-backup-by-scm.conf")
        # Set named.conf settings
        named_content = iscpy.ParseISCString(
            open("/etc/named.conf", 'r').read())
        named_content["options"]["listen-on port 53"]["any"] = "True"
        named_content["options"]["allow-query"]["any"] = "True"
        iscpy.WriteToFile(named_content, [], "/etc/named.conf")

    def create_reversed_zone_content(self,  domain: str):
        ''' Create a reversed zone content for zone file '''

        return ''' @   IN  SOA     ns1.{domain}. root.{domain}. (
                                                1001    ;Serial
                                                3H      ;Refresh
                                                15M     ;Retry
                                                1W      ;Expire
                                                1D      ;Minimum TTL
                                                )

;Name Server Information
@ IN  NS      ns1.{domain}.

;Reverse lookup for Name Server
10        IN  PTR     ns1.{domain}.

;PTR Record IP address to HostName
100      IN  PTR     www.{domain}.
150      IN  PTR     mail.{domain}. '''.format(domain=domain)

    def create_zone_content(self,  domain: str, ip: str):
        ''' Create a zone content for zone file '''

        return ''' @   IN  SOA     ns1.{domain}. root.{domain}. (
                                                1001    ;Serial
                                                3H      ;Refresh
                                                15M     ;Retry
                                                1W      ;Expire
                                                1D      ;Minimum TTL
                                                )

;Name Server Information
@      IN  NS      ns1.{domain}.

;IP address of Name Server
ns1 IN  A       {ip}

;Mail exchanger
{domain}. IN  MX 10   mail.{domain}.

;A - Record HostName To IP Address
www     IN  A       {ip}
mail    IN  A       {ip}

;CNAME record
ftp     IN CNAME        www.{domain}. '''.format(domain=domain, ip=ip)

    def create_zone(self, name: str):
        ''' Create a zone content for named.conf as dictionary to use with iscpy.AddZone '''

        return {
            "zone \"%s\" IN " % name: {
                "type": "master",
                "file": "/var/named/%s.db" % name,
                "allow-update": "{ none; }"
            }
        }

    def add_domain(self, domain: str, ip: str):
        ''' Add a domain to named.conf and create zone files '''

        # Add zone
        named_content = iscpy.ParseISCString(
            open("/etc/named.rfc1912.zones", 'r').read())

        named_content = iscpy.AddZone(
            self.create_zone(domain), named_content)
        # Add reverse zone
        reversed_ip = ".".join(list(reversed(ip.split(".")))[1:])
        named_content = iscpy.AddZone(
            self.create_zone(reversed_ip+".in-addr.arpa"), named_content)
        iscpy.WriteToFile(named_content, [],
                          "/etc/named.rfc1912.zones")
        # Add zone file
        with open("/var/named/"+domain+".db", 'w') as file:
            file.write(self.create_zone_content(domain, ip))
        # Add reverse zone file
        with open("/var/named/"+reversed_ip+".in-addr.arpa"+".db", 'w') as file:
            file.write(self.create_reversed_zone_content(domain))

    def restart(self):
        ''' Restart the named service '''
        self.run_command("systemctl restart named")
        self.run_command("systemctl enable named")
