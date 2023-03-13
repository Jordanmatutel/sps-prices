import data_miner as dm
import data_mean
import model
import graph
import extended_data

dm.data_creator()
data_mean.mean_price_area()
c = model.prediction()
extended_data.extended()
graph.graph()
