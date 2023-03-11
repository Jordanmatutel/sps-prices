import data_miner as dm
import data_classificator as dc
import model

dm.data_creator()
dc.mean_price_area()
c = model.prediction()
