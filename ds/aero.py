import sqlalchemy


class DataSource:
    # data source class
    def __init__(self) -> None:
        self.engine = sqlalchemy.create_engine(
            "mysql+mysqlconnector://server:donut@localhost:25060/7s"
        )

    def say_this(self, call: str) -> None:
        with self.engine.connect() as ds:
            result = ds.execute(sqlalchemy.text("select '{0}'".format(call)))
            print(result.all())
        return
