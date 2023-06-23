def doPost(request, session):
	
	# Log for debugging
	logger=system.util.getLogger("webdev")
	logger.info("entered Post")

	# Concatenate strings to build correct 'spoke address' aka which publisher gateway to send the data to
	whichSpoke = "spoke" + request["params"]["spokeNum"]
	whichServer = "publisher" + request["params"]["spokeNum"]
	
	#Build path for delete and log for debugging
	deleteTagPath = "[MQTT Engine]Edge Nodes/someData/"+whichSpoke+"/"+request["params"]["udtName"]
	logger.info(deleteTagPath)
	
	# If add is zero we go ahead and delete the given tag(s)
	if request["params"]["add"] == "0":
		system.tag.deleteTags([deleteTagPath])
	
	# Send the message and necessary parameters to the gateway
	system.util.sendMessage(whichSpoke, "message", request["params"], "CGS", remoteServers=[whichServer])
	
	if request["params"]["add"] == "0":
		system.tag.deleteTags([deleteTagPath])
	
	# Return something, somtimes nice for debugging
	return {'html': '<html><body>doPost Shoulda Worked Hopefully</body></html>'}