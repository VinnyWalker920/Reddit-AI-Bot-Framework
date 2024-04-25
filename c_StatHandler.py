import time, sys
import os, random

class StatHandler():

    def __init__(self, TotalPost, CooldownTime):

        self.statTemplateBasic = """Progress: {ProgressPercent}% | {CompletedPosts} posts out of {TotalPosts}\nEstimated Time Remaining: {Time}\nCurrent Phase: {Phase}"""
        self.statTemplateCooldown = """Progress: {ProgressPercent}% | {CompletedPosts} posts out of {TotalPosts}\nEstimated Time Remaining: {Time}\nCurrent Phase: {Phase} - Time Remaining {Cooldown}"""

        self.Cooldown = CooldownTime
        self.ProgressPercent = 0
        self.CompletedPosts = 0
        self.TotalPosts = TotalPost
        self.Time = "No Estimation Currently"
        self.Phase = 0
        self.Phases = ["Pulling Posts", "Generating Response", "Posting Response", "Cooldown"]
        self.EstTimeList = []

        self.TimeStart = None
        self.TimeEnd = None

    def _Avg(self,L):
        total = 0
        for i in L:
            total + i
        return total/len(L)
    
    def reprint(self):
        # Clear the terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        # Print the updated output
        NewPrint = self.statTemplateBasic.format(
            ProgressPercent=self.ProgressPercent,
            CompletedPosts=self.CompletedPosts,
            TotalPosts=self.TotalPosts,
            Time=self.Time,
            Phase=self.Phase,
        )
        print(NewPrint)

    def reprintCooldown(self, TimeRemaining):
        # Clear the terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        # Print the updated output
        NewPrint = self.statTemplateCooldown.format(
            ProgressPercent=self.ProgressPercent,
            CompletedPosts=self.CompletedPosts,
            TotalPosts=self.TotalPosts,
            Time=self.Time,
            Phase=self.Phase,
            Cooldown = TimeRemaining
        )
        print(NewPrint)

    def _RefreshStats(self):
        self.ProgressPercent = (self.CompletedPosts/self.TotalPosts) * 100
        self.Time = self._format_time((self.Cooldown * (self.TotalPosts - self.CompletedPosts) ) + random.randint(10, 45))
        
    def _format_time(self,seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return "{:02d} hours, {:02d} minutes, {:02d} seconds".format(hours, minutes, seconds)

    def CompletePost(self):
        self.CompletedPosts = self.CompletedPosts + 1
        self._RefreshStats()

    def ChangePhase(self,Phase:int):
        self.Phase = self.Phases[Phase]
        self._RefreshStats()
        self.reprint()

    def StartCooldown(self):
        self.Phase = self.Phases[3]
        TimeRem = self.Cooldown
        self._RefreshStats()
        for i in range(self.Cooldown):
            self.reprintCooldown(TimeRem)
            TimeRem = TimeRem - 1
            time.sleep(1)
    
    def StartTimer(self):
        self.TimeStart = time.time()

    def EndTimer(self):
        self.EstTimeList.append(time.time() - self.TimeStart)
        self._RefreshStats()
        
