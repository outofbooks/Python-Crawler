import wx

ID_NEW_URL = wx.NewId()
ID_NEW_DATA = wx.NewId()
ID_NEW_NOTE = wx.NewId()

def send_event(notify, result):
    wx.PostEvent(notify, result)

class NewUrlEvent(wx.PyEvent):
    """
    Event class for a new URL
    """
    def __init__(self, url):
        wx.PyEvent.__init__(self)
        self.SetEventType(ID_NEW_URL)
        self.url = url


class NewURLDataEvent(wx.PyEvent):
    """
    Event class for new data about a given url
    """
    def __init__(self, url, data):
        wx.PyEvent.__init__(self)
        self.SetEventType(ID_NEW_DATA)
        self.url = url
        self.data = data


class NewNoteEvent(wx.PyEvent):
    """
    Event for a new note!
    """
    def __init(self, url, note):
        wx.PyEvent.__init__(self)
        self.SetEventType(ID_NEW_NOTE)
        self.url = url
        self.note = note
