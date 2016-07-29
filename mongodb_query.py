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

