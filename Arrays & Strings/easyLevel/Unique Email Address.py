# 929
# my soluiton ->

class Solution(object):
    def numUniqueEmails(self, emails):
        n = len(emails)
        for i in range(n):
            emails[i] = emails[i].split('@')
            
            emails[i][0] = ''.join(emails[i][0].split('+')[0].split('.'))
        
            emails[i] = '@'.join(emails[i])
        
        return len(set(emails))