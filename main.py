import data_miner as dm
import data_mean
import model
import data_classificator

dm.data_creator()
data_mean.mean_price_area()
data_classificator.processor()
c = model.prediction()
