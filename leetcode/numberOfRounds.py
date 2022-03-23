class Solution(object):
    def convert(self, time):
        time = time.split(':')
        return int(time[0])*60+int(time[1])
    def numberOfRounds(self, loginTime, logoutTime):
        """
        :type loginTime: str
        :type logoutTime: str
        :rtype: int
        """
        new_login = login = self.convert(loginTime)
        new_logout = logout = self.convert(logoutTime)
        if login%15!=0:
            new_login = login - login%15 + 15
        if logout%15!=0:
            new_logout = logout - logout%15
        if login <= logout and new_login>=new_logout: return 0
        if new_login > new_logout: total =  1440-new_login+new_logout
        else: total = new_logout - new_login
        return total//15