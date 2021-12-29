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
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Option Calculator", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		main_listChoices = []
		self.main_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, main_listChoices, wx.LB_EXTENDED )
		bSizer1.Add( self.main_list, 1, wx.EXPAND|wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Level" ), wx.VERTICAL )

		self.level = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.level, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( sbSizer1, 0, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Path to Team / Pokemon" ), wx.VERTICAL )

		self.team = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.team, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( sbSizer2, 0, wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Sort by user", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button11, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button111 = wx.Button( self, wx.ID_ANY, u"Sort by damage", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button111, 0, wx.ALL|wx.EXPAND, 5 )

		self.useriv = wx.CheckBox( self, wx.ID_ANY, u"Maxed IVs (User)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.useriv, 0, wx.ALL, 5 )

		self.userev = wx.CheckBox( self, wx.ID_ANY, u"Maxed EVs (User)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.userev, 0, wx.ALL, 5 )

		self.enemyiv = wx.CheckBox( self, wx.ID_ANY, u"Maxed IVs (Enemy)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.enemyiv, 0, wx.ALL, 5 )

		self.enemyev = wx.CheckBox( self, wx.ID_ANY, u"Maxed EVs (Enemy)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.enemyev, 0, wx.ALL, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"\n\nPlease Note:\n\nThis does not consider user\nabilities, items, as well as\ntarget ability / items.\nThe same goes for weather\nand terrain effects.\n\nSome calculations may also\nbe off by around 1% due to\nrounding errors.\n\n> Jan-Okke", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.start )
		self.m_button11.Bind( wx.EVT_BUTTON, self.sort_user )
		self.m_button111.Bind( wx.EVT_BUTTON, self.sort_damage )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def start( self, event ):
		event.Skip()

	def sort_user( self, event ):
		event.Skip()

	def sort_damage( self, event ):
		event.Skip()


