import pandas as pd

class LifeExpetencyService:
     
    def __init__(self) -> None:
        # http://apps.who.int/gho/athena/api/GHO/WHOSIS_000002?format=csv
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


lifeExpetencyService  = LifeExpetencyService()