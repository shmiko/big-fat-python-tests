db.schedule.find("bookings" : {"$elemMatch" : { "date" : new ISODate("2016-08-09T10:00:00.000Z")}})
>> { "bookings" : [
			{
				"event" : "MongoDB On Site Interveiw",
				"date": ISODate("2016-08-09T10:00:00.000Z")
			}
		]
	}
	
	db.schedule.insert(
   { "bookings" : [
			{
				"event" : "MongoDB On Site Interveiw",
				"date": ISODate("2016-08-09T10:00:00.000Z")
			}
		]
	}
)

db.schedule.find()
{ "_id" : ObjectId("579af1b356bf8dd7f454ae3e"), "bookings" : [ { "event" : "MongoDB On Site Interveiw", "date" : ISODate("2016-08-09T10:00:00Z") } ] }

db.restaurants.insert(
   {
      "address" : {
         "street" : "2 Avenue",
         "zipcode" : "10075",
         "building" : "1480",
         "coord" : [ -73.9557413, 40.7720266 ]
      },
      "borough" : "Manhattan",
      "cuisine" : "Italian",
      "grades" : [
         {
            "date" : ISODate("2014-10-01T00:00:00Z"),
            "grade" : "A",
            "score" : 11
         },
         {
            "date" : ISODate("2014-01-16T00:00:00Z"),
            "grade" : "B",
            "score" : 17
         }
      ],
      "name" : "Vella",
      "restaurant_id" : "41704620"
   }
)

db.restaurants.insert(
   {
      "address" : {
         "street" : "2 Avenue",
         "zipcode" : "10075",
         "building" : "1480",
         "coord" : [ -73.9557413, 40.7720266 ]
      },
      "borough" : "Manhattan",
      "cuisine" : "Italian",
      "grades" : [
         {
            "date" : ISODate("2014-10-01T00:00:00Z"),
            "grade" : "A",
            "score" : 11
         },
         {
            "date" : ISODate("2014-01-16T00:00:00Z"),
            "grade" : "B",
            "score" : 17
         }
      ],
      "name" : "Vella",
      "restaurant_id" : "41704620"
   }
)

