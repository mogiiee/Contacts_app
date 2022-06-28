from . import responses, database



def GetAdvancedSearchString(query):
    list_query = query.split(" ")
    base_dict = {"$or": []}
    for i in list_query:
        # defining title dict
        title_dict = {
            "first_name": {"$regex": i, "$options":"i"}
        }
        description_dict = {
            "last_name": {"$regex": i, "$options":"i"}
        }
        phone_number_dict ={
            "phone_number": {"$regex": i, "$options":"i"}
        }
        base_dict["$or"].append(title_dict)
        base_dict["$or"].append(description_dict)
        base_dict["$or"].append(phone_number_dict)

    return base_dict

def Search(query, limit, page):    
    page = int(page)
    limit = int(limit)
    if int(page) == 0:
        return responses.ResponseStruct(False, "page cannot be less than 1", None)
    skip = (page - 1) * limit

    search_term = GetAdvancedSearchString(query)
    # search
    searched = database.collection.find(search_term, {"first_name": 1,"last_name":1,"phone_number":1, "_id": 0}).limit(limit).skip(skip).sort("_id", -1)
    results = list(searched)

    # results
    if len(results) == 0:
        return responses.ResponseStruct(False, "zero results", None)
    else:
        return responses.ResponseStruct(True, "results found", results)
