class AlarmClock:

    def __init__(self,):
        

        self.time_on_clock='12:00'    
        self.alarm_is_on=False
        self.alarm_time= '00:00'

    
    
    def change_time(self,time):
        self.time_on_clock=time
        print('Current Time on Clock:'),time
    
    def set_alarm_time(self,alarm):
        self.alarm_time=alarm
        print('Alarm is set for:'),alarm

    def turn_alarm_on(self,alarm_on):
         if alarm_on is False:
            print("Alarm is turned off")
         else: 
            print ("Alarm is turned on")
          

         



        
      
    




    