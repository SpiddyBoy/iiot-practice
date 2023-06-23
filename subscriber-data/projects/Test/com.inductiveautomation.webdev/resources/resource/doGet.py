def doGet(request, session):
	
	# Log that we made it here for debugging
	logger=system.util.getLogger("webdev")
	logger.info("receieved")
	
	# Get values from the request
	#udtType = request["udtType"]
	#spokeNum = request["spokeNum"]
	#udtName = request["udtName"]
	
	# Log values for debugging
	#logger.info(udtType)
	#logger.info(spokeNum)
	#logger.info(udtName)
	
	#whichSpoke = "spoke" + request["spokeNum"]
	#whichServer = "publisher" + request["spokeNum"]
	
	#system.util.sendMessage(whichSpoke, "message", request, "CGS", remoteServers=[whichServer])
	
	return {'html': '<html><body>Shoulda Worked Hopefully</body></html>'}