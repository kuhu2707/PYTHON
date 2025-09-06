import pymongo

if __name__ == "__main__":
    print("welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    
    #to see all databses
    show_db = client.list_database_names()
    print(show_db)
    
    #to see all the collections 
    col = client['kuhu']
    print(col.list_collection_names())