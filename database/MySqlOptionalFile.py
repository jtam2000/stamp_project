import myloginpath
import os


class MySqlOptionalFile:

    def __init__(self,
                 optional_file: str = '~/.mylogin.cnf',
                 file_section: str = 'client',
                 use_db: str = 'stamps'):

        self.__option_file = os.path.expanduser(optional_file)
        self.__option_file_section = file_section
        self.__login_db = use_db

        self.__conf = myloginpath.parse(login_path=self.__option_file_section,
                                        path=self.__option_file)

        # put in a default db if the optional file does not have one
        self.__conf.update(database=self.__conf.get("database") or use_db)

    def get_config(self):
        return self.__conf
