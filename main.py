from flask import Flask, jsonify
from flask import render_template

app = Flask(__name__)


@app.route('/')
def mm():
    return render_template("index.html")

@app.route('/data')
def get_data():
    geojson_data ={
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          [
            [
              -75.68323997743963,
              5.261287383930011
            ],
            [
              -75.78345393393559,
              5.305194197423617
            ],
            [
              -75.83556519131348,
              5.261287383930011
            ],
            [
              -75.84358230783316,
              5.121563395599807
            ],
            [
              -75.9310888268268,
              5.0397517331698225
            ],
            [
              -75.80281496251196,
              4.919948942210894
            ],
            [
              -75.64648119037825,
              4.963879163942124
            ],
            [
              -75.45407039390601,
              4.923942718935848
            ],
            [
              -75.38592490348877,
              4.808113535024532
            ],
            [
              -75.2015312235362,
              5.171509272573459
            ],
            [
              -74.86080377144994,
              5.315213477684438
            ],
            [
              -74.6528321850588,
              5.497076297975198
            ],
            [
              -74.64882362679897,
              5.720480707721762
            ],
            [
              -74.7450290250351,
              5.712503460806744
            ],
            [
              -75.09778215190086,
              5.656659630020528
            ],
            [
              -75.27015015707391,
              5.437221451489535
            ],
            [
              -75.42648392920759,
              5.7045261027861045
            ],
            [
              -75.59885193438066,
              5.752388581264995
            ],
            [
              -75.56678346830196,
              5.528996426616359
            ],
            [
              -75.77121993955372,
              5.5569251275045985
            ],
            [
              -75.86341677953001,
              5.497076297975198
            ],
            [
              -75.69898792066162,
              5.386031734255539
            ],
            [
              -75.68323997743963,
              5.261287383930011
            ]
          ]
        ],
        "type": "Polygon"
      }
    }
  ]
}
    return  jsonify(geojson_data)

if __name__ == '__main__':
    #app.config(debug=True)
    app.run()
    