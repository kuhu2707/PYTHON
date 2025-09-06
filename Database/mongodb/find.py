import pymongo

if __name__ == "__main__":
    print("welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['kuhu']
    collection = db['samplecollection']
    
    #to find only single document - will give any one random doc
    one = collection.find_one()
    print(one)
    
    # #if want by name then - will only give one doc with name as lmn
    one=collection.find_one({'name':'lmn'})
    print(one)
    
    #to find all doc with name lmn
    all=collection.find({'name':'lmn'})
    print(all)
    
    
    #if want to print all for lmn wehave to iterate them
    all=collection.find({'name':'lmn'})
    for item in all:
        print(item)
        
    #if we want to have only specific fileds printed 
    all=collection.find({'name':'lmn'},{'name':1,'age':1,'_id':0})
    for item in all:
        print(item)
        
        
    