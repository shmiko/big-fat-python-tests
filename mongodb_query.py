db.schedule.find("bookings" : {"$elemMatch" : { "date" : new ISODate("2016-08-09T10:00:00.000Z")}})
>> { "bookings" : [
			{
				"event" : "MongoDB On Site Interveiw",
				"date": ISODate("2016-08-09T10:00:00.000Z")
			}
		]
	}