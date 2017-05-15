db.getCollection('cities').aggregate(
{"$unwind":"$isPartOf"},
{"$group": {"_id":{"country":"$country","province":"$isPartOf"},"average":{"$avg": "$population"}}},
{"$project":{"country":"$_id.country","province":"$_id.province","average":1}},
{"$unwind":"$_id"},
{"$group":{"_id":"$country","avgRegionalPopulation":{"$avg":"$average"}}}

)