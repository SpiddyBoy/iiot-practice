def msgHandler(payload):
	
	# Print for debugging
	logger=system.util.getLogger("messageHandleLog")
	logger.info("message received on 1!")
	
	# Create tag path
	baseTagPath = "[default]PLCData"
	deleteTagPath = "[default]PLCData/%s" % payload["udtName"]
	
	# Create tag with info from the payload
	tag = {
		"name": payload["udtName"],
		"typeId": payload["udtType"],
		"tagType" : "UdtInstance"
		}
	
	# Collision policy "a" means we don't do anything if the given tag already exists
	collisionPolicy = "a"
	
	# If add is true, then we add this tag to the path, if false, we delete this tag from the path
	if	payload["add"] == "1":	
		system.tag.configure(baseTagPath, [tag], collisionPolicy)
	else:
		system.tag.deleteTags([deleteTagPath])
	
	logger.info(deleteTagPath)
	
	# Force refresh to see new tag changes in subscriber
	system.tag.writeAsync("[MQTT Transmission]Transmission Control/Refresh", [1])
	
	# Adding new comment!

	# Adding comment from VSCode!

	# Will this comment show up too?