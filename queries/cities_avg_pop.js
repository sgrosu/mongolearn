db.getCollection('cities').aggregate([
{"$match":{"isPartOf":{"$exists": true}}},
{"$group": {"_id": "$isPartOf","citylist": {"$push":"$population"}}},

{"$project": {"id": "$isPartOf", "average": {"$avg":"$citylist"}}}
])