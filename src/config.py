class Config:
    def __init__(
        self,
        db_username: str = "root",
        db_password: str = "root",
        db_host: str = "localhost",
        db_name: str = "sakila",
        db_port: int = 3307,
        echo_sql: bool = True,
    ):
        self.db_username = db_username
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.db_name = db_name
        self.db_echo_sql = echo_sql
