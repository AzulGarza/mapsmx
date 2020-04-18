import geopandas as gpd
import os

class MapsMX:
    """
    Returns data to plot maps
    """

    def __init__(self):
        pass


        self.dict_args_file = {'state': 'ent', 'municipality': 'mun'}


    def get_geo(self, kind, add_centroids=False):

        allowed_kinds = ('state', 'municipality')

        assert kind in allowed_kinds, ValueError('kind must be one of {}'.format(', '.join(allowed_kinds)))


        kind_file = self.dict_args_file[kind]

        read_file = 'zip://mapsmx/geo/{}.zip'.format(kind_file)
        data = gpd.read_file(read_file)
        data = self.clean_cols(data, kind_file)
        data = data.set_geometry('geometry_ent')

        if add_centroids:
            data['centroid'] = data['geometry_{}'.format(kind_file)].centroid

        return data


    def clean_cols(self, df, kind):

        df_clean = df.rename(
            columns={
                'CVEGEO': 'cve_geo_{}'.format(kind),
                'NOMGEO': 'NOM_{}'.format(kind),
                'geometry': 'geometry_{}'.format(kind)
        })

        df_clean.columns = df_clean.columns.str.lower()

        return df_clean
