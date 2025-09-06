import pymongo

if __name__ == "__main__":
    print("welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['kuhu']
    collection = db['samplecollection']
    
    #to delete single 
    rec={'name':'KUHU1'}
    collection.delete_one(rec)
    
    #to delete many
    rec={'name':'pqr'}
    de = collection.delete_many(rec)
    print(de.deleted_count)