class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        a=arriveAlice.split("-")
        b=leaveAlice.split("-")
        c=arriveBob.split("-")
        d=leaveBob.split("-")

        starts1=int(a[1])
        start2=int(c[1])
        end1=int(b[1])
        end2=int(d[1])

        for i in range(int(a[0])-1):
            starts1+=days[i]
        for i in range(int(c[0])-1):
            start2 +=days[i]
        for i in range(int(b[0])- 1):
            end1 +=days[i]
        for i in range(int(d[0])-1):
            end2+=days[i]

        start=max(starts1,start2)  
        end=min(end1,end2)

        if start > end:
            return 0

        return end-start+1






    

        
        
        

        