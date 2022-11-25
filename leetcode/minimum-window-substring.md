from collections import Counter,defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        
        dist_t = Counter(t)
        obs = defaultdict(int)
        
        cnt = len(dist_t.keys())
        
        pro = 0
        
        
        if len(s) < len(t):
            return ''
        if s == t :
            return s
        
        
        n_s = len(s)
        
        i = 0
        j = 0
        
        pos = None 
        length = float('inf')
        
        
        
        while j < n_s :
            obs[s[j]] +=1
            #if pro < cnt :
            
            if s[j] in dist_t and obs[s[j]] == dist_t[s[j]]:
                pro +=1
            
            while pro == cnt and i <= j :
        
                if length > j - i + 1 :
                    length = j - i +1
                    pos = [i,j]
                
                obs[s[i]]-=1
                if obs[s[i]] < dist_t[s[i]]  and s[i] in dist_t:
                    pro -= 1
                i+=1
            j+=1
        if pos is None :
            return ''
        
        answer=s[(pos[0]):(pos[1]+1)]
        
        
        return answer
    
    
    
'''
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        answer = ''
        
        
        dist=Counter(t)
        
        l = len(t)
        n = len(s)
        
        length = float('inf')
        
        for i in range(n):
            for j in range(i,n+1):
                tmp = s[i:j]
                os = Counter(tmp)
                flag = True
                for k in dist.keys():
                    if dist[k] > os[k] :
                        flag = False
                        break
                if flag and length > len(tmp):
                    answer = tmp
                    length = len(tmp)
                
        return answer
'''
