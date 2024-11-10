class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        #input = matches
        #output = 
        loss_count = {}

        for winner, loser in matches:
            if winner not in loss_count:
                loss_count[winner] = 0  # winners have zero losses initially
            if loser in loss_count:
                loss_count[loser] += 1  # increment loss count for losers
            else:
                loss_count[loser] = 1   # first time a player loses

        no_loss = []
        one_loss = []

        for player, losses in loss_count.items():
            if losses == 0:
                no_loss.append(player)
            elif losses == 1:
                one_loss.append(player)

        no_loss.sort()
        one_loss.sort()

        return [no_loss, one_loss]