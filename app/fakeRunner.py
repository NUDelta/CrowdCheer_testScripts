'''
Script for faking runners for CrowdCheer
'''

# register with parse
from parse_rest.connection import register, ParseBatcher
from parse_rest.user import User
from parse_rest.datatypes import Object, GeoPoint
batcher = ParseBatcher()
import datetime
from time import sleep
import random
import json, httplib
from settings_local import *
register(APPLICATION_ID, REST_API_KEY, master_key=MASTER_KEY)


#RunnerLocations class
class RunnerLocations(Object):
    pass
    def nowVersion(self):
        rl = RunnerLocations()
        rl.location = self.location
        rl.time = datetime.datetime.now()
        rl.user = self.user
        rl.distance = self.distance
        rl.duration = self.duration
        rl.speed = self.speed
        rl.save()

    def new(self, lat, lon, distance, duration, speed):
        self.location = GeoPoint(latitude=lat, longitude=lon)
        self.time = datetime.datetime.now()
        global u
        self.user = u
        self.distance = distance
        self.duration = duration
        self.speed = speed
        self.save()

class SpectatorLocations(Object):
    pass
    def nowVersion(self):
        sl = SpectatorLocations()
        sl.location = self.location
        sl.time = datetime.datetime.now()
        sl.user = self.user
        sl.distance = self.distance
        sl.duration = self.duration
        sl.save()

    def new(self, lat, lon, distance, duration):
        self.location = GeoPoint(latitude=lat, longitude=lon)
        self.time = datetime.datetime.now()
        global u
        self.user = u
        self.distance = distance
        self.duration = duration
        self.save()

def getRunnerQuerySet():
    runnersQuerySet = RunnerLocations.Query.all().order_by("-distance")
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
        RunnerLocations.nowVersion(rl)
        print "updated %s times" % updateNum
        print "distance : %s , duration : %s" % (rl.distance, rl.duration)
        updateNum += 1
        if (updateNum > length):
            break
        sleep(updateFrequency)

def fakeNewRunFromCSV(csvLines, updateFrequency, length, objID, username, pwd):
    '''
    use like this...
    fakeNewLocations(runnerLocations, 1, 40)
    runnerLocations is the query,
    1 is going to send the next location every 1 second,
     and will do this for 40 seconds
    '''
    u = User.login(username, pwd)
    updateNum = 0
    for line in csvLines[1:]:
        lat, lon, time, username, user_objid, dist, runT, speed = line.strip().split(",")
        rl = RunnerLocations(location=GeoPoint(latitude=float(lat), longitude=float(lon)),
                            time = datetime.datetime.now(),
                            user = u,
                            distance = float(dist),
                            duration = runT, 
                            speed = float(speed))
        rl.save()
        
        print datetime.datetime.now()
        print datetime.datetime.utcnow()

        connection = httplib.HTTPSConnection('api.parse.com', 443)
        objectPath = '/1/classes/CurrRunnerLocation/' + objID
        connection.connect()
        connection.request('PUT', objectPath, json.dumps({
            
            "time": datetime.datetime.utcnow(),
            "speed": float(speed),
            "duration": runT,
            "distance": float(dist),
            "location": {
                "__type": "GeoPoint",
                "latitude": float(lat), 
                "longitude": float(lon)
            }
        }), {
            "X-Parse-Application-Id": "QXRTROGsVaRn4a3kw4gaFnHGNOsZxXoZ8ULxwZmf",
            "X-Parse-REST-API-Key": "BCJuFgG7GVxZfnc2mVbt2dzLz4bP7qAu16xaItXB",
            "Content-Type": "application/json"
        })
        result = json.loads(connection.getresponse().read())
        print result

        print "updated %s times" % updateNum
        print "distance : %s , duration : %s" % (rl.distance, rl.duration)
        updateNum += 1
        if (updateNum > length):
            break
        sleep(updateFrequency)

def fakeNewCheerFromCSV(csvLines, updateFrequency, length, objID, username, pwd):
    '''
    use like this...
    fakeNewLocations(runnerLocations, 1, 40)
    runnerLocations is the query,
    1 is going to send the next location every 1 second,
     and will do this for 40 seconds
    '''
    u = User.login(username, pwd)
    updateNum = 0
    for line in csvLines[1:]:
        lat, lon, time, username, user_objid, dist, runT = line.strip().split(",")
        sl = SpectatorLocations(location=GeoPoint(latitude=float(lat), longitude=float(lon)),
                            time = datetime.datetime.now(),
                            user = u,
                            distance = float(dist),
                            duration = runT)
        sl.save()
        
        connection = httplib.HTTPSConnection('api.parse.com', 443)
        objectPath = '/1/classes/CurrSpectatorLocation/' + objID
        connection.connect()
        connection.request('PUT', objectPath, json.dumps({
            
            "duration": runT,
            "distance": float(dist),
            "location": {
                "__type": "GeoPoint",
                "latitude": float(lat), 
                "longitude": float(lon)
            }
        }), {
            "X-Parse-Application-Id": "QXRTROGsVaRn4a3kw4gaFnHGNOsZxXoZ8ULxwZmf",
            "X-Parse-REST-API-Key": "BCJuFgG7GVxZfnc2mVbt2dzLz4bP7qAu16xaItXB",
            "Content-Type": "application/json"
        })
        result = json.loads(connection.getresponse().read())
        print result

        print "updated %s times" % updateNum
        print "distance : %s , duration : %s" % (sl.distance, sl.duration)
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

######  THIS STUFF IS FOR SIMILARITY TABLES ###########
#birthday similarity class
class Birthday_Similarity(Object):
    def __init__(self, this_user, other_user, motivation_primer):
        super(Object, self).__init__()
        self.this_user = this_user
        self.other_user = other_user
        self.motivation_primer = motivation_primer
# determine zodiac sign
class zodiac_sign:
    def __init__(self, sign, start_month, start_day, end_month, end_day):
        self.sign = sign
        self.start_month = start_month
        self.start_day = start_day
        self.end_month = end_month
        self.end_day = end_day

signs = [zodiac_sign("Aries", 3, 21, 4, 19),
        zodiac_sign("Taurus", 4, 20, 5, 20),
        zodiac_sign("Gemini", 5, 21, 6, 20),
        zodiac_sign("Cancer", 6, 21, 7, 22),
        zodiac_sign("Leo", 7, 23, 8, 22),
        zodiac_sign("Virgo", 8, 23, 9, 22),
        zodiac_sign("Libra", 9, 23, 10, 22),
        zodiac_sign("Scorpio", 10, 23, 11, 21),
        zodiac_sign("Sagittarius", 11, 22, 12, 21),
        zodiac_sign("Capricorn", 12, 22, 1, 19),
        zodiac_sign("Aquarius", 1, 20, 2, 18),
        zodiac_sign("Pisces", 2, 19, 3, 20)]

seasonsByNumber = {1 : "Winter",
           2 : "Winter",
           3 : "Spring",
           4 : "Spring",
           5 : "Spring",
           6 : "Summer",
           7 : "Summer",
           8 : "Summer",
           9 : "Fall",
           10 : "Fall",
           11 : "Fall",
           12 : "Winter"}

seasonsByMonth = {'January' : "Winter",
           'February' : "Winter",
           'March' : "Spring",
           'April' : "Spring",
           'May' : 'Spring',
           'June' : 'Summer',
           'July' : 'Summer',
           'August' : 'Summer',
           'September' : 'Fall',
           'October' : 'Fall',
           'November' : 'Fall',
           'December' : 'Winter'}

seasonsByNumber = {'January' : 1,
           'February' : 2,
           'March' : 3,
           'April' : 4,
           'May' : 5,
           'June' : 6,
           'July' : 7,
           'August' : 8,
           'September' : 9,
           'October' : 10,
           'November' : 11,
           'December' : 12}

def zodiac_from_bday(birth_month, birth_day):
    for sign in signs:
        if (birth_month == sign.start_month) and (birth_day >= sign.start_day):
            return sign.sign
        if (birth_month == sign.end_month) and (birth_day <= sign.end_day):
            return sign.sign
    return None # algorithm failed

def getAllUsers():
    import json,httplib
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/users', '', {
           "X-Parse-Application-Id": APPLICATION_ID,
           "X-Parse-REST-API-Key": REST_API_KEY
         })
    users = json.loads(connection.getresponse().read())['results']
    return users



def bDaySims(users):
    # test methods
    usersForSimilarity = []
    for i in range(len(users)):
        try:
            print users[i]['birthMonth']
            sign = zodiac_from_bday(seasonsByNumber[users[i]['birthMonth']], users[i]['birthDay'])
            if sign == None:
                print "No sign for %s/%s" % (users[i]['birthMonth'], users[i]['birthDay'])
            users[i]['sign'] = sign
            users[i]['season'] = seasonsByMonth[users[i]['birthMonth']]
            usersForSimilarity.append(users[i])
        except KeyError as ke:
            print "problem with key : %s" % ke.message

    bday_similarities = []
    match_count = 0
    total = 0
    for this_user in usersForSimilarity:
        for other_user in usersForSimilarity:
            total += 1
            primer = None
            if (this_user['birthDay'] == other_user['birthDay']) and (this_user['birthMonth'] == other_user['birthMonth']):
                primer = "You and %s have the same birth day!" % other_user['name']
                match_count += 1
            elif (this_user['sign'] == other_user['sign']):
                primer = "You and %s are both %s!" % (other_user['name'], other_user['sign'])
                match_count += 1
            elif (this_user['birthMonth'] == other_user['birthMonth']):
                primer = "You and %s are both born in %s" % (other_user['name'], other_user['birthMonth'])
                match_count += 1
            elif (this_user['season'] == other_user['season']):
                primer = "You and %s are both born in the %s" % (other_user['name'], other_user['season'])
                match_count += 1
            bday_similarities.append(Birthday_Similarity(this_user['objectId'], other_user['objectId'], primer))
    print "%s probability of match" % (float(match_count)/float(total))
    print "total : %s, match_count : %s" % (total, match_count)

    # Given that we have a 30 requests per second Parse request limit, we need to be careful how we upload data
    # We will need to upload in batches of 30 and wait one second in between.
    # If the limit is hit, then we will need to make it wait one minute before continuing.
    from time import sleep
    from parse_rest.core import ResourceRequestBadRequest

    request_limit = 30 # We currently have a 30 requests per second Parse request limit
    batches = [bday_similarities[x:x+request_limit] for x in xrange(0, len(bday_similarities), request_limit)]
    print "%s batches : %s minutes to upload" % (len(batches), len(batches)/60.)

    count = 0
    for batch in batches:
        count += 1
        print "Uploading batch #%s out of %s" % (count, len(batches))
        try:
            batcher.batch_save(batch)
            sleep(1)
        except ResourceRequestBadRequest:
            print "Probably reached limit, waiting 1 minute"
            sleep(60)

####### Question SIMILARITIES ########

questionPrimerDict = {
    "q_one" : ['%s is a White Sox fan too!', '%s is a Cubs fan too!'],
    "q_two" : ['%s is another Nike runner too!', '%s is another Reebok too!'],
    "q_three" : ['%s is a coffee drinker too!', '%s is a tea drinker too!'],
    "q_four" : ['%s is also a dog person!', '%s is also a cat person!'],
    "q_five" : ['%s prefers it hot too', '%s prefers it cold too!']
}

def userSimilarities(this_user, other_user):
    question_fields = ['q_one','q_two','q_three','q_four','q_five']
    sames = []
    primer = None
    for i in range(len(question_fields)):
        if this_user.has_key(question_fields[i]) and other_user.has_key(question_fields[i]):
            if this_user[question_fields[i]] == other_user[question_fields[i]]:
                sames.append(questionPrimerDict[question_fields[i]][this_user[question_fields[i]]])
    if len(sames) > 0:
        primer = random.choice(sames) % other_user['name']
    return primer

# q_similarity class
class QuestionSimilarity(Object):
    def __init__(self,this_user,other_user,primer):
        super(Object, self).__init__()
        self.this_user = this_user
        self.other_user = other_user
        self.primer = primer

def computeQuestionSimilarities(users):
    q_similarities = []

    from random import choice
    for this_user in users:
        for other_user in users:
            primer = userSimilarities(this_user, other_user)
            q_sim = QuestionSimilarity(this_user['objectId'], other_user['objectId'], primer)
            q_similarities.append(q_sim)

    request_limit = 30 # We currently have a 30 requests per second Parse request limit
    batches = [q_similarities[x:x+request_limit] for x in xrange(0, len(q_similarities), request_limit)]
    print "%s batches : %s minutes to upload" % (len(batches), len(batches)/60.)

    count = 0
    for batch in batches:
        count += 1
        print "Uploading batch #%s out of %s" % (count, len(batches))
        try:
            batcher.batch_save(batch)
            sleep(1)
        except ResourceRequestBadRequest:
            print "Probably reached limit, waiting 1 minute"
            sleep(60)
