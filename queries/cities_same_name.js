db.getCollection('cities').aggregate(
{"$match":{"name":{"$exists":true}}},
{"$match": {"name": {"$nin":["NULL","None",""]}}},
{"$group": {"_id":"$name","count":{"$sum":1}}},
{"$project":{"name":1,"count":1}},
{"$sort":{"count":-1}},
{"$limit":1}
)
