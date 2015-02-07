__author__ = 'tyan'
import os
from django.contrib.gis.utils import LayerMapping
from .models import ChinaCity
# Auto-generated `LayerMapping` dictionary for ChinaCity model
chinacity_mapping = {
    'id_0' : 'ID_0',
    'iso' : 'ISO',
    'name_0' : 'NAME_0',
    'id_1' : 'ID_1',
    'name_1' : 'NAME_1',
    'id_2' : 'ID_2',
    'name_2' : 'NAME_2',
    'nl_name_2' : 'NL_NAME_2',
    'varname_2' : 'VARNAME_2',
    'type_2' : 'TYPE_2',
    'engtype_2' : 'ENGTYPE_2',
    'geom' : 'MULTIPOLYGON',
}



world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/china/CHN_adm2.shp'))

def run(verbose=True):
    lm = LayerMapping(ChinaCity, world_shp, chinacity_mapping,
                      transform=False, encoding='UTF-8')

    lm.save(strict=False, verbose=verbose)