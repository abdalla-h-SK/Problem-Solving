# 1507
# my solution ->
 
class Solution(object):
    def reformatDate(self, date):
        date = date.split()
        months_dict = {
            "Jan": "1", "Feb": "2", "Mar": "3", "Apr": "4", "May": "5", "Jun": "6",
            "Jul": "7", "Aug": "8", "Sep": "9", "Oct": "10", "Nov": "11", "Dec": "12"
        }     
        day = ''
        for i in date[0]:
            if i.isdigit():
                day += i
            else:
                break
        
        return '{}-{}-{}'.format(date[2], months_dict[date[1]].zfill(2), day.zfill(2))