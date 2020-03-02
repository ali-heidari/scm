from component.base_component import BaseComponent


class MySQL(BaseComponent):
    '''
    MySQL component handles all MySQL commands
    '''

    def __init__(self, root_pass):
        ''' Init MySQL instance with provided root_pass '''
        super().__init__()
        self._root_pass = root_pass

    def init(self):
        self.run_command(
            "/opt/lampp/bin/mysqladmin --user=root password \"" + self._root_pass+"\"")

    def create_user(self, username, password):
        ''' Creates a user and gives all privileges '''

        self.run_command("/opt/lampp/bin/mysql -u root -p" + self._root_pass + " -e \"CREATE USER '" + username + "'@'localhost IDENTIFIED BY '" +
                         password + "'; GRANT ALL PRIVILEGES ON database_name.* TO '" + username + "'@'localhost';flush privileges;\"")

    def create_database(self, username, password, db_name):
        ''' Creates a database with given user '''

        self.run_command("/opt/lampp/bin/mysql -u "+username +
                         " -p" + password+" -e \"CREATE DATABASE "+db_name+";\"")
