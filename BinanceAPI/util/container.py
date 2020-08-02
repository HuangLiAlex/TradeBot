class Stick:

    def __init__(self):
        self.Time = None
        self.Open = None
        self.High = None
        self.Low = None
        self.Close = None
        self.Stick = None
        self.Trend = None
        
    @classmethod
    def fromJson(cls, Time, Open, High, Low, Close):
        cls.Time = Time
        cls.Open = Open
        cls.High = High
        cls.Low  = Low
        cls.Close = Close
        
        if(float(Close) > float(Open)):
            cls.Trend = 'up'
        else:
            cls.Trend = 'down'
            
        cls.Stick = {
                        'Time': cls.Time,
                        'Open': cls.Open,
                        'High': cls.High,
                        'Low' : cls.Low,
                        'Close': cls.Close,
                        'Trend': cls.Trend
                    }
        return cls.Stick
    
    @classmethod
    def fromFragment(cls, Time, Open, Close):
        cls.Time = Time
        cls.Open = Open
        cls.Close = Close

        if(float(Close) > float(Open)):
            cls.High = Close
            cls.Low  = Open
            cls.Trend = 'up'
        else:
            cls.High = Open
            cls.Low  = Close
            cls.Trend = 'down'
            
        cls.Stick = {
                        'Time': cls.Time,
                        'Open': cls.Open,
                        'High': cls.High,
                        'Low' : cls.Low,
                        'Close': cls.Close,
                        'Trend': cls.Trend
                    }
        return cls.Stick