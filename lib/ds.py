from sqlalchemy import create_engine, text
import models


class DataSource:
    # data source class
    def __init__(self) -> None:
        self.engine = create_engine(
            "mysql+mysqlconnector://server:donut@localhost:25060/server-6"
        )
        models.Entity.metadata.create_all(self.engine)

    def say_this(self, call: str) -> None:
        with self.engine.connect() as ds:
            result = ds.execute(text("select '{0}'".format(call)))
            print(result.all())
        return
