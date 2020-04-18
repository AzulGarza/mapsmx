[![Build](https://github.com/FedericoGarza/mapsmx/workflows/Python%20package/badge.svg?branch=master)](https://github.com/FedericoGarza/mapsmx/tree/master)
[![PyPI version fury.io](https://badge.fury.io/py/mapsmx.svg)](https://pypi.python.org/pypi/mapsmx/)
[![Downloads](https://pepy.tech/badge/mapsmx)](https://pepy.tech/project/mapsmx)
[![Python 3.5+](https://img.shields.io/badge/python-3.5+-blue.svg)](https://www.python.org/downloads/release/python-350+/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/FedericoGarza/covidmx/blob/master/LICENSE)

# mapsmx

Create maps of Mexico easily with python.

# How to install

```console
pip install mapsmx
```

# How to use

State geometries.

```python
state = MapsMX().get_geo('state')
```

State geometries with centroids.

```python
state_w_centroids = MapsMX().get_geo('state', add_centroids=True)
```

Municipality geometries.

```python
muns = MapsMX().get_geo('municipality')
```

Municipality geometries with centroids.

```python
muns_w_centroids = MapsMX().get_geo('municipality', add_centroids=True)
```

# Data
- shp files downloaded from https://www.inegi.org.mx/temas/mg/default.html#Descargas.
