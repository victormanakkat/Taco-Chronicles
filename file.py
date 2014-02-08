#file class
#By Tyler Spadgenske

import pickle, sys

class File():
    def __init__(self):
        pass

    def read(self):
        try:
            self.data = pickle.load( open( "data.p", "rb" ))
        except:
            print 'File Not found.'
            self.data = {'highscore': 0, 'totalscore': 0, 'firstRun': True, 'lockedGuns':{'9mm':False, 'shotgun':True, 'AK-47':True, 'bazooka':True,
                                                                                           'flamethrower':True}} 
            pickle.dump(self.data, open( "data.p", "wb" ) )
            print 'New File Added.'

        self.data = pickle.load(open('data.p', 'rb'))
        self.highscore = self.data['highscore']
        self.totalscore = self.data['totalscore']
        self.firstRun = self.data['firstRun']
        self.lockedGuns = self.data['lockedGuns']

        return self.highscore, self.totalscore, self.firstRun, self.lockedGuns
        
    def write(self, highscore, totalscore, firstRun, lockedGuns):
        self.data = {'highscore': highscore, 'totalscore': totalscore, 'firstRun': firstRun, 'lockedGuns':lockedGuns }
        pickle.dump(self.data, open( "data.p", "wb" ) )

    def printFile(self):
        self.data = pickle.load( open( "data.p", "rb" ))
        print 'Total Score: ', self.data['totalscore']
        print 'High Score: ', self.data['highscore']
        print 'First Program Run: ', self.data['firstRun']
        print 'Weapons Unlocked: ', self.data['lockedGuns']

if __name__ == '__main__':
    f = File()
    f.printFile()
        
