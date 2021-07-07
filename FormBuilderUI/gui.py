# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class CalculatorFrame
###########################################################################

class CalculatorFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Damage Calculator", pos = wx.DefaultPosition, size = wx.Size( 800,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.leftside_movename1 = wx.StaticText( self, wx.ID_ANY, u"(Move 1)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.leftside_movename1.Wrap( -1 )

		bSizer2.Add( self.leftside_movename1, 0, wx.ALL, 5 )

		self.leftside_movename2 = wx.StaticText( self, wx.ID_ANY, u"(Move 2)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.leftside_movename2.Wrap( -1 )

		bSizer2.Add( self.leftside_movename2, 0, wx.ALL, 5 )

		self.leftside_movename3 = wx.StaticText( self, wx.ID_ANY, u"(Move 3)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.leftside_movename3.Wrap( -1 )

		bSizer2.Add( self.leftside_movename3, 0, wx.ALL, 5 )

		self.leftside_movename4 = wx.StaticText( self, wx.ID_ANY, u"(Move 4)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.leftside_movename4.Wrap( -1 )

		bSizer2.Add( self.leftside_movename4, 0, wx.ALL, 5 )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Pokemon Infos" ), wx.VERTICAL )

		sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Name" ), wx.VERTICAL )

		self.leftmonname = wx.TextCtrl( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Lucario", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer10.Add( self.leftmonname, 0, wx.ALL, 5 )


		sbSizer1.Add( sbSizer10, 1, wx.EXPAND, 5 )

		sbSizer101 = wx.StaticBoxSizer( wx.StaticBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Ability" ), wx.VERTICAL )

		self.leftmonability = wx.TextCtrl( sbSizer101.GetStaticBox(), wx.ID_ANY, u"Adaptability", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer101.Add( self.leftmonability, 0, wx.ALL, 5 )


		sbSizer1.Add( sbSizer101, 1, wx.EXPAND, 5 )

		sbSizer102 = wx.StaticBoxSizer( wx.StaticBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Item" ), wx.VERTICAL )

		self.leftmonitem = wx.TextCtrl( sbSizer102.GetStaticBox(), wx.ID_ANY, u"Choice Band", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer102.Add( self.leftmonitem, 0, wx.ALL, 5 )


		sbSizer1.Add( sbSizer102, 1, wx.EXPAND, 5 )

		sbSizer103 = wx.StaticBoxSizer( wx.StaticBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Move 1" ), wx.VERTICAL )

		self.leftmonmove1 = wx.TextCtrl( sbSizer103.GetStaticBox(), wx.ID_ANY, u"Close Combat", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer103.Add( self.leftmonmove1, 0, wx.ALL, 5 )


		sbSizer1.Add( sbSizer103, 1, wx.EXPAND, 5 )

		sbSizer104 = wx.StaticBoxSizer( wx.StaticBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Move 2" ), wx.VERTICAL )

		self.leftmonmove2 = wx.TextCtrl( sbSizer104.GetStaticBox(), wx.ID_ANY, u"Bullet Punch", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer104.Add( self.leftmonmove2, 0, wx.ALL, 5 )


		sbSizer1.Add( sbSizer104, 1, wx.EXPAND, 5 )

		sbSizer105 = wx.StaticBoxSizer( wx.StaticBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Move 3" ), wx.VERTICAL )

		self.leftmonmove3 = wx.TextCtrl( sbSizer105.GetStaticBox(), wx.ID_ANY, u"Earthquake", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer105.Add( self.leftmonmove3, 0, wx.ALL, 5 )


		sbSizer1.Add( sbSizer105, 1, wx.EXPAND, 5 )

		sbSizer106 = wx.StaticBoxSizer( wx.StaticBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Move 4" ), wx.VERTICAL )

		self.leftmonmove4 = wx.TextCtrl( sbSizer106.GetStaticBox(), wx.ID_ANY, u"Extreme Speed", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer106.Add( self.leftmonmove4, 0, wx.ALL, 5 )


		sbSizer1.Add( sbSizer106, 1, wx.EXPAND, 5 )

		sbSizer1062 = wx.StaticBoxSizer( wx.StaticBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Level" ), wx.VERTICAL )

		self.leftmonlevel = wx.TextCtrl( sbSizer1062.GetStaticBox(), wx.ID_ANY, u"76", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1062.Add( self.leftmonlevel, 0, wx.ALL, 5 )


		sbSizer1.Add( sbSizer1062, 1, wx.EXPAND, 5 )


		bSizer2.Add( sbSizer1, 1, wx.EXPAND, 5 )


		bSizer7.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.output = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer3.Add( self.output, 1, wx.ALL|wx.EXPAND, 5 )

		sbSizer111 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Weather" ), wx.VERTICAL )

		self.weather = wx.TextCtrl( sbSizer111.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer111.Add( self.weather, 0, wx.ALL, 5 )


		bSizer3.Add( sbSizer111, 0, wx.EXPAND, 5 )

		sbSizer1111 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Terrain" ), wx.VERTICAL )

		self.terrain = wx.TextCtrl( sbSizer1111.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1111.Add( self.terrain, 0, wx.ALL, 5 )


		bSizer3.Add( sbSizer1111, 0, wx.EXPAND, 5 )


		bSizer7.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.rightside_movename1 = wx.StaticText( self, wx.ID_ANY, u"(Move 1)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rightside_movename1.Wrap( -1 )

		bSizer21.Add( self.rightside_movename1, 0, wx.ALL, 5 )

		self.rightside_movename2 = wx.StaticText( self, wx.ID_ANY, u"(Move 2)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rightside_movename2.Wrap( -1 )

		bSizer21.Add( self.rightside_movename2, 0, wx.ALL, 5 )

		self.rightside_movename3 = wx.StaticText( self, wx.ID_ANY, u"(Move 3)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rightside_movename3.Wrap( -1 )

		bSizer21.Add( self.rightside_movename3, 0, wx.ALL, 5 )

		self.rightside_movename4 = wx.StaticText( self, wx.ID_ANY, u"(Move 4)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rightside_movename4.Wrap( -1 )

		bSizer21.Add( self.rightside_movename4, 0, wx.ALL, 5 )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Pokemon Infos" ), wx.VERTICAL )

		sbSizer107 = wx.StaticBoxSizer( wx.StaticBox( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Name" ), wx.VERTICAL )

		self.rightmonname = wx.TextCtrl( sbSizer107.GetStaticBox(), wx.ID_ANY, u"Gengar", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer107.Add( self.rightmonname, 0, wx.ALL, 5 )


		sbSizer11.Add( sbSizer107, 1, wx.EXPAND, 5 )

		sbSizer1011 = wx.StaticBoxSizer( wx.StaticBox( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Ability" ), wx.VERTICAL )

		self.rightmonability = wx.TextCtrl( sbSizer1011.GetStaticBox(), wx.ID_ANY, u"Levitate", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1011.Add( self.rightmonability, 0, wx.ALL, 5 )


		sbSizer11.Add( sbSizer1011, 1, wx.EXPAND, 5 )

		sbSizer1021 = wx.StaticBoxSizer( wx.StaticBox( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Item" ), wx.VERTICAL )

		self.rightmonitem = wx.TextCtrl( sbSizer1021.GetStaticBox(), wx.ID_ANY, u"Life Orb", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1021.Add( self.rightmonitem, 0, wx.ALL, 5 )


		sbSizer11.Add( sbSizer1021, 1, wx.EXPAND, 5 )

		sbSizer1031 = wx.StaticBoxSizer( wx.StaticBox( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Move 1" ), wx.VERTICAL )

		self.rightmonmove1 = wx.TextCtrl( sbSizer1031.GetStaticBox(), wx.ID_ANY, u"Energy Ball", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1031.Add( self.rightmonmove1, 0, wx.ALL, 5 )


		sbSizer11.Add( sbSizer1031, 1, wx.EXPAND, 5 )

		sbSizer1041 = wx.StaticBoxSizer( wx.StaticBox( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Move 2" ), wx.VERTICAL )

		self.rightmonmove2 = wx.TextCtrl( sbSizer1041.GetStaticBox(), wx.ID_ANY, u"Earth Power", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1041.Add( self.rightmonmove2, 0, wx.ALL, 5 )


		sbSizer11.Add( sbSizer1041, 1, wx.EXPAND, 5 )

		sbSizer1051 = wx.StaticBoxSizer( wx.StaticBox( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Move 3" ), wx.VERTICAL )

		self.rightmonmove3 = wx.TextCtrl( sbSizer1051.GetStaticBox(), wx.ID_ANY, u"Sludge Bomb", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1051.Add( self.rightmonmove3, 0, wx.ALL, 5 )


		sbSizer11.Add( sbSizer1051, 1, wx.EXPAND, 5 )

		sbSizer1061 = wx.StaticBoxSizer( wx.StaticBox( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Move 4" ), wx.VERTICAL )

		self.rightmonmove4 = wx.TextCtrl( sbSizer1061.GetStaticBox(), wx.ID_ANY, u"Shadow Ball", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1061.Add( self.rightmonmove4, 0, wx.ALL, 5 )


		sbSizer11.Add( sbSizer1061, 1, wx.EXPAND, 5 )

		sbSizer10621 = wx.StaticBoxSizer( wx.StaticBox( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Level" ), wx.VERTICAL )

		self.rightmonlevel = wx.TextCtrl( sbSizer10621.GetStaticBox(), wx.ID_ANY, u"76", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer10621.Add( self.rightmonlevel, 0, wx.ALL, 5 )


		sbSizer11.Add( sbSizer10621, 1, wx.EXPAND, 5 )


		bSizer21.Add( sbSizer11, 1, wx.EXPAND, 5 )


		bSizer7.Add( bSizer21, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )

		self.CalculateButton = wx.Button( self, wx.ID_ANY, u"Calculate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.CalculateButton, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.CalculateButton.Bind( wx.EVT_BUTTON, self.calculate )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def calculate( self, event ):
		event.Skip()


