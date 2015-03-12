'''
Script for faking runners from Scott
'''

# register with parse
from parse_rest.connection import register, ParseBatcher
from parse_rest.user import User
from parse_rest.datatypes import Object, GeoPoint
batcher = ParseBatcher()
import datetime
from time import sleep
from settings_local import *
register(APPLICATION_ID, REST_API_KEY, master_key=MASTER_KEY)

#RunnerLocation class
class RunnerLocation(Object):
    pass
    def nowVersion(self):
        rl = RunnerLocation()
        rl.location = self.location
        rl.time = datetime.datetime.now()
        rl.user = self.user
        rl.distance = self.distance
        rl.runTime = self.runTime
        rl.save()

    def new(self, lat, lon, distance, runTime):
        self.location = GeoPoint(latitude=lat, longitude=lon)
        self.time = datetime.datetime.now()
        global u
        self.user = u
        self.distance = distance
        self.runTime = runTime
        self.save()

def getRunnerQuerySet():
    runnersQuerySet = RunnerLocation.Query.all().order_by("-distance")
    return runnersQuerySet

def fakeNewRun(querySet, updateFrequency, length):
    '''
    use like this...
    fakeNewLocations(runnerLocations, 1, 40)
    runnerLocations is the query,
    1 is going to send the next location every 1 second,
     and will do this for 40 seconds
     '''
    updateNum = 0
    for rl in querySet:
        RunnerLocation.nowVersion(rl)
        print "updated %s times" % updateNum
        print "distance : %s , runTime : %s" % (rl.distance, rl.runTime)
        updateNum += 1
        if (updateNum > length):
            break
        sleep(updateFrequency)

def fakeOneLocation(exampleLoc, lat, lon):
    '''
    use like this...
    fakeOneLocation(getRunnerQuerySet()[0], 42.0588, -122.3334)
    '''
    exampleLoc.location = GeoPoint(latitude=lat, longitude=lon)
    exampleLoc.time = datetime.datetime.now()
    exampleLoc.save()
