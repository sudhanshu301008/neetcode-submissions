class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        n = len(temps)
        stck = []
        result = [0]*n
        for i,t in enumerate(temps):
            while stck and stck[-1][0] < t:
                stck_t,stck_i = stck.pop()
                result[stck_i] = i - stck_i
            stck.append((t,i))
        return result






        