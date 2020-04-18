import geopandas as gpd
import pkgutil
from mapsmx.utils import get_file_name

class MapsMX:
    """
    Returns data to plot maps
    """

    def __init__(self):

        self.dict_args_file = {'state': 'ent', 'municipality': 'mun'}

    def get_geo(self, kind, add_centroids=False):

        allowed_kinds = ('state', 'municipality')

        assert kind in allowed_kinds, \
            ValueError(
                'kind must be one of {}'.format(', '.join(allowed_kinds))
            )

        kind_file = self.dict_args_file[kind]

        data = self.read_data(kind_file, add_centroids)

        return data

    def read_data(self, kind, add_centroids):

        #data = pkgutil.get_data(__name__, "geo/{}.zip".format(kind))
        #print("data:", repr(data))
        read_file = get_file_name(__name__,  "geo/{}.zip".format(kind))
        read_file = 'zip://{}'.format(read_file)

        data = gpd.read_file(read_file)
        data = self.clean_cols(data, kind)
        data = data.set_geometry('geometry_{}'.format(kind))

        if add_centroids:
            data['centroid'] = data['geometry_{}'.format(kind)].centroid

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
