finalResult = []
for records in results:
	for record in records:	
	    data_to_send = {
	            'title': record['title'],
	            'website': record['link'],
	            'description': record['snippet'],
	    }
	    finalResult.append(data_to_send)
	finalResult.append(data_to_send)
#######

firstFinalResult = []
finalResult = []
for records in results:
    for record in records:	
	    data_to_send = {
	            'title': record['title'],
	            'website': record['link'],
	            'description': record['snippet'],
	    }
	    all_data_to_send = firstFinalResult.append(data_to_send)
	finalResult.append(all_data_to_send)

