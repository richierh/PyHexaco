#! usr/bin/env python

import wx



class TentangAplikasi ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Binakarir", pos = wx.DefaultPosition, size = wx.Size( 600,350 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer31 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel26 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel26.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

        bSizer34 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel24 = wx.Panel( self.m_panel26, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer33 = wx.BoxSizer( wx.VERTICAL )

        self.m_bitmap2 = wx.StaticBitmap( self.m_panel24, wx.ID_ANY, wx.Bitmap( u"../coreapps/resources/images/binakarir.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer33.Add( self.m_bitmap2, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


        self.m_panel24.SetSizer( bSizer33 )
        self.m_panel24.Layout()
        bSizer33.Fit( self.m_panel24 )
        bSizer34.Add( self.m_panel24, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

        self.m_panel25 = wx.Panel( self.m_panel26, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel25.SetBackgroundColour( wx.Colour( 255, 200, 55 ) )

        bSizer32 = wx.BoxSizer( wx.VERTICAL )


        bSizer32.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText208 = wx.StaticText( self.m_panel25, wx.ID_ANY, u"Bandung - Indonesia", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText208.Wrap( -1 )

        self.m_staticText208.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

        bSizer32.Add( self.m_staticText208, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText209 = wx.StaticText( self.m_panel25, wx.ID_ANY, u"Email : careindonesiasolusi@gmail.com", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText209.Wrap( -1 )

        self.m_staticText209.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

        bSizer32.Add( self.m_staticText209, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText210 = wx.StaticText( self.m_panel25, wx.ID_ANY, u"Telp. 022 87241354", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText210.Wrap( -1 )

        self.m_staticText210.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

        bSizer32.Add( self.m_staticText210, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer32.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        self.m_panel25.SetSizer( bSizer32 )
        self.m_panel25.Layout()
        bSizer32.Fit( self.m_panel25 )
        bSizer34.Add( self.m_panel25, 1, wx.EXPAND |wx.ALL, 5 )


        self.m_panel26.SetSizer( bSizer34 )
        self.m_panel26.Layout()
        bSizer34.Fit( self.m_panel26 )
        bSizer31.Add( self.m_panel26, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer31 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass

