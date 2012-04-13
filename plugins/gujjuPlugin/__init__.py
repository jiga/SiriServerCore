#!/usr/bin/python
# -*- coding: utf-8 -*-


from plugin import *
from siriObjects.systemObjects import ResultCallback
import uuid

lang_mode = ''

class gujjuPlugin(Plugin):
    
    @register("en-US", ".*How.*life.*")
    def meaningOfLife(self, speech, language, matchedRegex):
        if language == 'gu-IN':
            #answer = self.ask(u"Willst du das wirklich wissen?")
            #self.say(u"Du hast \"{0}\" gesagt!".format(answer))
            self.say("bau oondu chhe bhalaa maanas!!")
        else:
            self.say("arey poonchhO nahee.... ")
            self.say("maaaru toh garoo dookhee gayuu.. bolee bolee ney! ")
        self.complete_request()

    @register("en-US", ".*How.*you.*")
    def gujjuGreetings(self, speech, language, matchedRegex):
        if language == 'gu-IN':
            #answer = self.ask(u"Willst du das wirklich wissen?")
            #self.say(u"Du hast \"{0}\" gesagt!".format(answer))
            self.say("bau oondu chhe bhalaa maanas!!")
        else:
            self.say(u"હું મઝામાં છું.",u"hoo mazhaamaa chhhu.")
            answer = self.ask(u"તમે કેમ છો?",u"tamae kame chhho?")
            self.say(answer)
            self.say(u"મને કહેવા માટે આભાર.",u"manae kayhvvaa maatey, aabhhhaaar!")
            #self.say("I shouldn't tell you!")
        self.complete_request()

    @register("en-US", "(.*Hello.*)|(.*Hi.*Siri.*)|(Hi)|(Hey)")
    @register("gu-IN", ".*(Kem Chho|)( Siri)?.*")
    def st_hello(self, speech, language):
        global lang_mode
        if language == 'gu-IN':
            self.say(u"majhaamaa")
        else:
            if lang_mode == 'gujju':
                display_text = u'\u0a9c\u0aaf \u0ab6\u0acd\u0ab0\u0ac0 \u0a95\u0acd\u0ab0\u0abf\u0ab7\u0acd\u0aa3\u0abe '+self.user_name()+"!"
                speak_text = u"Jay Shree Krishnaa {0}!".format(self.user_name)
                self.say(display_text, speak_text)
            else:
                self.say(u"Greetings {0}!".format(self.user_name()))
            #self.say(u"જય શ્રી ક્રિષ્ણા!", u"Jay Shree Krishnaa!")
            #self.say(display_text, u"Jay Shree Krishnaa "+self.user_name+"!")
            #self.say('',self.user_name())
            #self.say(u"Jaya Shriri Krishnaa {0}!".format(self.user_name()), u"જય શ્રી કૃષ્ણ Jaya Shiri Krishnaa {0}!".format(self.user_name()))
        self.complete_request()
        
    @register("en-US", ".*Speak.*Gujarati.*")
    def speakGujju(self, speech, language, matchedRegex):
        global lang_mode
        if language == 'gu-IN':
            #answer = self.ask(u"Willst du das wirklich wissen?")
            #self.say(u"Du hast \"{0}\" gesagt!".format(answer))
            self.say("bau oondu chhe bhalaa maanas!!")
        else:
            self.say(u"બરાબર, હવે ગુજરાતી બોલું છું.",u"baraabur, hvey Gujarati boluu chhhoo.")
            lang_mode = 'gujju'
            #self.say("I shouldn't tell you!")
        self.complete_request()
    
    @register("en-US", "(.*Good.*Bye.*)|(See.*you.*)|(.*Speak.*English.*)")
    def speakEnglish(self, speech, language, matchedRegex):
        global lang_mode
        if language == 'gu-IN':
            #answer = self.ask(u"Willst du das wirklich wissen?")
            #self.say(u"Du hast \"{0}\" gesagt!".format(answer))
            self.say("bau oondu chhe bhalaa maanas!!")
        else:
            if lang_mode == 'gujju':
                self.say(u"આવજો!",u"Aavjo!")
                lang_mode = ''
            else:
                self.say(u"Bye Bye!")
            self.say("now speaking English")
        self.complete_request()
        
    @register("en-US", ".*location.*test.*")
    def locationTest(self, speech, language):
        location = self.getCurrentLocation(force_reload=True)
        self.say(u"lat: {0}, long: {1}".format(location.latitude, location.longitude))
        self.complete_request()
          
