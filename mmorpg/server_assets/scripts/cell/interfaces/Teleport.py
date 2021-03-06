# -*- coding: utf-8 -*-
import KBEngine
import SpaceContext
from KBEDebug import * 

class Teleport:
	def __init__(self):
		pass
		
	def teleportSpace(self, spaceUType, position, direction, context):
		"""
		defined.
		传送到某场景
		"""
		assert self.base != None
		self.lastSpaceUType = self.spaceUType
		self.getSpaces().teleportSpace(self.base, spaceUType, position, direction, SpaceContext.createContext(self, spaceUType))

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onTeleportSpaceCB(self, spaceCellMailbox, spaceUType, position, direction):
		"""
		defined.
		baseapp返回teleportSpace的回调
		"""
		DEBUG_MSG("Teleport::onTeleportSpaceCB: %i spaceID=%s, spaceUType=%i, pos=%s, dir=%s." % \
					(self.id, spaceCellMailbox.id, spaceUType, position, direction))
		
		self.getCurrSpaceBase().onLeave(self.id)
		self.teleport(spaceCellMailbox, position, direction)
		
	def onTeleportSuccess(self, nearbyEntity):
		"""
		KBEngine method.
		"""
		DEBUG_MSG("Teleport::onTeleportSuccess: %s" % (nearbyEntity))
		self.getCurrSpaceBase().onEnter(self.base)
		self.spaceUType = self.getCurrSpace().spaceUType
		
	def onDestroy(self):
		"""
		entity销毁
		"""
		self.getSpaces().logoutSpace(self.id, self.getCurrSpaceBase().id)
