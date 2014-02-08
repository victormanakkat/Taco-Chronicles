#instaler
#By Tyler Spadgenske
import wx

class Install(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(Install, self).__init__(*args, **kwargs) 
            
        self.InitUI()
        
    def InitUI(self):    

        self.OnAboutBox()

    def OnAboutBox(self):
        
        description = """The Taco Chronicles is an Action Adventure game written in Python.
You must get to Taco Bell, without getting shot. Use the Arrow keys to move and jump, and
press space to shoot. The more you play, the higher your total score gets. The higher your
score gets, the more weapons you unlock!"""

        licence = """The Taco Chronicles is free software; you can redistribute 
it and/or modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation; either version 2 of the License, 
or (at your option) any later version.

The Taco Chronicles is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
See the GNU General Public License for more details. You should have 
received a copy of the GNU General Public License along with The Taco Chronicles; 
if not, write to the Free Software Foundation, Inc., 59 Temple Place, 
Suite 330, Boston, MA  02111-1307  USA"""


        info = wx.AboutDialogInfo()
        info.SetName('Taco Chronicles')
        info.SetVersion('1.0')
        info.SetDescription(description)
        info.SetCopyright('(C) 2014 PYWARE')
        info.SetWebSite('www.Github.com/pywareCode/Taco-Chronicles')
        info.SetLicence(licence)
        info.AddDeveloper('Tyler Spadgenske')
        info.AddArtist('Tyler Spadgenske')

        wx.AboutBox(info)


def run():
    
    ex = wx.App()
    Install(None)  
run()
