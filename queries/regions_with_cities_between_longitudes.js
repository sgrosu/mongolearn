db.getCollection('cities').aggregate(
{"$match":{"country":{"$eq":"India"}}},
{"$match":{"lon":{"$gte":75,"$lte":80}}},
{"$unwind":"$isPartOf"},
{"$group": {"_id":"$isPartOf", "citilist":{"$push": {"name":"$name"}}}},
{"$project":{"_id":"$_id", "count": {"$size":"$citilist"}}},
{"$sort":{"count":-1}},
{"$limit":1}

)