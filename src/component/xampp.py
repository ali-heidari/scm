from component.base_component import BaseComponent
from component.mysql import MySQL
from component.wordpress import Wordpress


class XAMPP(BaseComponent):
    '''
    XAMPP component handles all XAMPP commands
    '''
    mysql_instance: MySQL = None
    wordpress_instance: Wordpress = None

    def __init__(self, version, mysql_root):
        ''' Init XAMPP instance with specified version '''
        super().__init__()
        self._version = version
        self._mysql_root = mysql_root

    def init(self):
        self.install()
        self.mysql_instance = MySQL(self._mysql_root)

    def install(self):
        '''  Since XAMPP is not provided with yum, need to be installed manually using *.run file '''

        run_file = "xampp-linux-x64-" + self._version+"-0-installer.run"
        self.run_command(
            "curl https://www.apachefriends.org/xampp-files/" + self._version+"/"+run_file)
        self.run_command("chmod 755 " + run_file)
        self.run_command("./"+run_file)

    def init_wordpress(self, db_user, db_pass):
        ''' Init a wordpress '''
        
        self.wordpress_instance = Wordpress()
        self.mysql_instance.create_user(db_user,db_pass)
        self.mysql_instance.create_database(db_user,db_pass,"wp_db")

    def set_access(self):
        ''' Set access of documents such as htdocs '''
        
        # Create user group for xampp
        self.run_command("groupadd xamppusers")
        # Add current user to xamppusers
        self.run_command("usermod -a -G xamppusers $(whoami)")
        # Give permission to htdocs folder for xamppusers group
        self.run_command("cd /opt/lampp && chown root.xamppusers htdocs && chmod 775 htdocs")

