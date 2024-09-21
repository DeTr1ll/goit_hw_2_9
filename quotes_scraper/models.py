from mongoengine import Document, StringField, ReferenceField, ListField, connect

connect(db="HumiderCluster", host="mongodb+srv://Humider:4U7m5q80uf0UaSZo@humidercluster.5in6y.mongodb.net/?retryWrites=true&w=majority&appName=HumiderCluster")

class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField()