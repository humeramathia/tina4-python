#
# Tina4 - This is not a 4ramework.
# Copy-right 2007 - current Tina4
# License: MIT https://opensource.org/licenses/MIT
#
# flake8: noqa: E501
import importlib

from tina4_python import Debug, Constant
from tina4_python.DatabaseResult import DatabaseResult


class Database:

    def __init__(self, _connection_string, _username="", _password=""):
        """
        Initializes a database connection
        :param _connection_string:
        """
        # split out the connection string
        # driver:host/port:schema/path

        params = _connection_string.split(":", 1)
        self.database_module = importlib.import_module(params[0])

        self.database_engine = params[0]
        self.database_path = params[1]
        self.username = _username
        self.password = _password

        if self.database_engine == "sqlite3":
            self.dba = self.database_module.connect(self.database_path)
            self.port = None
            self.host = None

        if self.database_engine == "firebird.driver":
            # <host>/<port>:<file>
            temp_params = self.database_path.split(":", 1)
            host_port = temp_params[0].split("/", 1)
            self.host = host_port[0]
            if len(host_port) > 1:
                self.port = int(host_port[1])
            else:
                self.port = 3050

            self.database_path = temp_params[1]

            self.dba = self.database_module.connect(
                self.host + "/" + str(self.port) + ":" + self.database_path,
                user=self.username,
                password=self.password
            )

        Debug("DATABASE:", self.database_module, self.host, self.port, self.database_path, self.username, Constant.TINA4_LOG_INFO)

    def fetch(self, sql, params=(), limit=10, skip=0):
        Debug("DATABASE:", self.database_module, self.host, self.port, self.database_path, self.username, Constant.TINA4_LOG_DEBUG)
        # modify the select statement for limit and skip
        if self.database_engine == "firebird.driver":
            sql = f"select first {limit} skip {skip} * from ({sql})"
        elif self.database_engine == "sqlite3":
            sql = f"select * from ({sql}) limit {skip},{limit}"

        cursor = self.dba.cursor()
        try:
            cursor.execute(sql, params)
            columns = [column[0].lower() for column in cursor.description]
            records = cursor.fetchall()
            rows = [dict(zip(columns, row)) for row in records]
            columns = [column for column in cursor.description]
            return DatabaseResult(rows, columns, None)
        except Exception as e:
            return DatabaseResult(None, [], str(e))

    def close(self):
        self.dba.close()
        pass
