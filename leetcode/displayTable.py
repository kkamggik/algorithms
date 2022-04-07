class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        table = defaultdict(collections.Counter)
        meal = set()
        for name, num, menu in orders:
            meal.add(menu)
            table[num][menu] += 1
        foods = sorted(meal)
        res = [['Table'] + [food for food in foods]]
        for t in sorted(table, key=int):
            res.append([t]+[str(table[t][food]) for food in foods])
        return res