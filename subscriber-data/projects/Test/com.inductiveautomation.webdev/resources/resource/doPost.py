def doPost(request, session):
	
	# Log for debugging
	logger=system.util.getLogger("webdev")
	logger.info("entered Post")
	
	# Return html for API response
	return myFuncs.postReceived(request)