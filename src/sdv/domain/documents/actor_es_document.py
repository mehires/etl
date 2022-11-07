from elasticsearch_dsl import Document, Integer, Text, Date


class ActorEsDocument(Document):
    id = Integer()
    first_name = Text()
    last_name = Text()
    last_update = Date()

    class Index:
        name = "actor"
        settings = {"number_of_shards": 2}

    def save(self, **kwargs):
        return super(ActorEsDocument, self).save(**kwargs)
