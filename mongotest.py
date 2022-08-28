import pymongo

client = pymongo.MongoClient("mongodb+srv://JAISWA_B:Bikoo1996@clusterbik.2grbd0c.mongodb.net/?retryWrites=true&w=majority")

d={
    "name": "bikash",
    "email":"bikk@123",
    "surname":"jaiswal"
}

db1= client['mongotest']
coll = db1['test']
coll.insert_one(d )