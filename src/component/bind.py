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

    def add_domain(self, domain: str, ip: str):
        ''' Add a domain to named.conf '''

        # Add zone
        named_content = iscpy.ParseISCString(
            open("/etc/named.conf", 'r').read())
        iscpy.AddZone("zone \""+domain+"\" IN {" +
                      "type master;" +
                      "file \"/var/named/"+domain+".db\";" +
                      "allow-update { none; };" +
                      "}; ", named_content)
        iscpy.WriteToFile(named_content, [], "/etc/named.conf")
        # Add reverse zone
        reversed_ip = ".".join(reversed(ip.split("."))[1:])
        named_content = iscpy.ParseISCString(
            open("/etc/named.conf", 'r').read())
        iscpy.AddZone("zone \""+reversed_ip+".in-addr.arpa\" IN {" +
                      "type master;" +
                      "file \"/var/named/"+".".join(ip.split(".")[1:])+".db\";" +
                      "allow-update { none; };" +
                      "};", named_content)
        iscpy.WriteToFile(named_content, [], "/etc/named.conf")
