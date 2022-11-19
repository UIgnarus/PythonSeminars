import html_creator as hc
import xml_generator as xg
import data_provider as dp

# print(hc.create())
# print(xg.create())

data = dp.data_collection()
xg.new_create((hc.new_create(data)))
