import pymongo

if __name__ == "__main__":
    print("welcome to pymongo")
    
    #connection to monogdb
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    
#creating databse
    db = client['kuhu']
    
    #creating connections
    collection = db['samplecollection']
    
    #inserting document - for single doc
    # student={'name':'kuhu','age':22,'course':'ai'}
    # collection.insert_one(student)
    
    #for many doc
    students=[
        {'name':'abc','age':23,'course':'ml'},
        {'name':'xyz','age':24,'course':'dl'},
        {'name':'pqr','age':25,'course':'ai'},
        {'name':'lmn','age':26,'course':'dl'},
        {'name':'lmn','age':26,'course':'dl'},
        {'name':'lmn','age':26,'course':'dl'}
    ]
    collection.insert_many(students)