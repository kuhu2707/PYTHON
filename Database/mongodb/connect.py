import pymongo

if __name__ == "__main__":
    print("welcome to pymongo")
    
    #connection to monogdb
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    
