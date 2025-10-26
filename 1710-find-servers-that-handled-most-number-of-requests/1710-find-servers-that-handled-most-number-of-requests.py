class Solution(object):

    import heapq #min heap
    import bisect #binary search 

    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        #i -= index 
        #i % k = avaliable server
        # k = #number of servers

        avail = list(range(k))
        busy = []

        #each request that handled per
        handled = [0] * k 
        
        for i, (t, d) in enumerate(zip(arrival, load)):
            
            #request take time to finsih
            finish_time = t + d

            #track the busynes and releade and finished servers
            while busy and busy[0][0] <= t:
                
                #poping until the next jpb ends after valuet 
                free_t, sid = heapq.heappop(busy)   
                
                #put the server that i pfreed 
                bisect.insort(avail, sid)
            
            #no avaliability 
            if not avail:
                continue
            
            base = i % k 

            pos = bisect.bisect_left(avail, base)
            
            #server >= base, none >= base + wrap
            if pos == len(avail):
                pos = 0

            #server asssignmet 
            sid = avail.pop(pos)
            handled[sid] += 1
            
            #server is now busy until the finish time 
            heapq.heappush(busy, (finish_time, sid))
        
        max_handled = max(handled) if handled else 0
        return [i for i, c in enumerate(handled) if c == max_handled]