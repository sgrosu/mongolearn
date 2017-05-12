db.getCollection('tweets').aggregate([   
{"$group": {"_id": "$user.screen_name","countlist" : {"$push": "$text"}}},
{"$project": {"_id" : "$user.screen_name", "count": {"$size": "$countlist"},"tweet_texts": "$countlist"}},
{"$sort": {"count": -1}},
{"$limit": 5}
])
