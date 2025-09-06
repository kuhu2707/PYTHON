import pymongo

if __name__ == "__main__":
    print("welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['kuhu']
    collection = db['samplecollection']
    
    
    #to update something in the collection -for one only
    prev={'name':'abc'}
    new={'$set':{'name':'pihu'}}
    collection.update_one(prev,new)
    
    #to update many
    prev={'name':'JAYDEEP'}
    new={'$set':{'name':'RAJAT'}}
    collection.update_many(prev,new)
    
    #to see how many docs we have modified
    prev={'name':'lmn'}
    new={'$set':{'name':'JAYDEEP'}}
    upd = collection.update_many(prev,new)
    print(upd.modified_count)
    

    