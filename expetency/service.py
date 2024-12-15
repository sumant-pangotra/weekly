import pandas as pd
from datetime import datetime

class LifeExpetencyService:
     
    def __init__(self,online=False) -> None:
        if online:
            try:
                self.data = pd.read_csv('http://apps.who.int/gho/athena/api/GHO/WHOSIS_000002?format=csv').fillna('')
            except Exception as e:
                print(e)
                print("Using 'expetency/static/life-expetency.csv'")
                self.data = pd.read_csv('expetency/static/life-expetency.csv').fillna('')
        # http://apps.who.int/gho/athena/api/GHO/WHOSIS_000002?format=csv
        else:
            self.data = pd.read_csv('expetency/static/life-expetency.csv').fillna('')

    def getByRegion(self, region: str):
        return self.data.query(f"COUNTRY == '{region}'").to_dict('records')
    
    def getLatestByRegion(self, region: str, sex: str):
        df = self.data.query(f"COUNTRY == '{region}' & SEX == '{sex}'")
        if len(df.index) > 0:
            df = df.loc[df['YEAR'].idxmax()]
            df.to_dict()
        else:
           df = {}
        return df
    
    def getCountryCodes(self):
        return self.data.COUNTRY.unique()

    def getSexCodes(self):
        return self.data.SEX.unique()

    def get_life_expetency(self,region: str, sex: str):
        df = self.data.query(f"COUNTRY == '{region}' & SEX == '{sex}'")
        if len(df.index) > 0:
            df = df.loc[df['YEAR'].idxmax()]
            return int(df["Numeric"])
        return None

    def get_weeks_lived(self,dob_day: int,dob_month: int,dob_year: int,region: str, sex: str):
        life_expetency_years =  self.get_life_expetency(region,sex)
        life_expetency_weeks = (life_expetency_years * 365) // 7
        now = datetime.utcnow().date()
        delta = now - datetime(dob_year,dob_month,dob_day).date()
        return {"weeksLived":delta.days // 7, "totalWeeks":life_expetency_weeks}




lifeExpetencyService  = LifeExpetencyService()


if __name__ == "__main__":
    lifeExpetencyOnlineService  = LifeExpetencyService(online=True)
    print(lifeExpetencyService.get_weeks_lived(1,1,1995,"IND","MLE"))
    print(lifeExpetencyService.get_weeks_lived(1,1,1995,"IND","FMLE"))
    print(lifeExpetencyService.get_weeks_lived(1,1,1995,"IND","BTSX"))

    print(lifeExpetencyOnlineService.get_weeks_lived(1,1,1995,"IND","MLE"))
    print(lifeExpetencyOnlineService.get_weeks_lived(1,1,1995,"IND","FMLE"))
    print(lifeExpetencyOnlineService.get_weeks_lived(1,1,1995,"IND","BTSX"))