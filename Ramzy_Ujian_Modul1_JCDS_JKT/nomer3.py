class Statistic:
    
    # regular method
    def mean(self,first):
        jumlah = 0
        for i in first:
            jumlah += i
            mean = jumlah/len(first)
            return mean
            
    # regular method
    def median(self, second):
         
        n = len(second) 
        second.sort() 
        if n % 2 == 0: 
            median1 = second[n//2] 
            median2 = second[n//2 - 1] 
            median = (median1 + median2)/2
        else: 
            median = second[n//2] 
        return median
       
    def mode(self, third):
        n_num = [1, 2, 3, 4, 5, 5] 
        n = len(n_num) 
  
        data = Counter(n_num) 
        get_mode = dict(data) 
        mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
        if len(mode) == n: 
            get_mode = "No mode found"
        else: 
            get_mode = "Mode is / are: " + ', '.join(map(str, mode))
        return get_mode
        
     def std(self):
       
std = Statistic().mean([])
