from save import _formatter

# title: brand. ?G or ?GB
# link: href=""
# price: EUR 199,00
# shipping fee: EUR 18,00 / Kostenloser Versand

class data:
    
    def __init__(self, model, _date, title, link, price, fee): # all in str.
        
        self.model = model # str. "2060", "1080ti"
        self._date = _date # str.
        self.title = title # str.
        self.link = link # str.

        if price == "": self.price = 0.0 # float.            
        else: self.price = float(price[price.index("R ") + 2 :].replace(".", "").replace(",", ".")) # could be like "1.544,90"
            
        if "los" in fee or fee == "": self.fee = 0.0            
        else: self.fee = float(fee[fee.index("R ") + 2 : fee.index("V")].replace(",", ".")) # float.            

    @property
    def cost(self): # float
        
        return self.price + self.fee
    
    @property
    def gb(self): # from title. int.
        
        title = self.title.replace("gb", "GB").replace("g ", "G ")
        
        try: start = title.index("GB") - 3
        except: start  = title.index("G ") - 3
        
        if start < 0: return 0 # no g or gb mentioned.

        s = title[start : start + 3]
        integer_str = ""
        for ch in s:
            if ch.isdigit(): integer_str += ch
        
        return int(integer_str)
    
    @property       
    def distributor(self): # from title. str.
        
        l = ["asus", "inno", "palit", "giga", "zot", "msi", "gainward", "kfa2", "evga", "pny", "hp", "dell", "fdr", "powercolor", "sapp", "XFX", "asr"]
        title = self.title.lower()
        
        for ele in l:
            if ele in title: return ele
            
        return "unknown"

    @property
    def date(self): # from ._date

        return _formatter(self._date)

        
        
        
        

        
    
        
    