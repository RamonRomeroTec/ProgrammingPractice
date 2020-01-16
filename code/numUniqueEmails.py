class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        d = set()
        for email in emails:
            atindex= email.find('@')
            user, domain = email[:atindex], email[atindex:] 
            user = user.replace(".","")
            if '+' in user:
                user = user[:user.find('+')]
            mail = user+domain
            d.add(mail)
            
        return len(d)
            
        