
import folium
import pandas


def draw_basic_map():
    _map = folium.Map(location=[38.58, -99.09], zoom_start=6, titles="Mapbox Bright")
    fg = folium.FeatureGroup(name="My Map")
    _map.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker",
                                 icon=folium.Icon(color='green')))
    fg.add_child(folium.Marker(location=[38.0, -99.3], popup="Hi I am other Marker",
                               icon=folium.Icon(color='blue')))
    _map.add_child(fg)
    _map.save("map1.html")


class Volcanoes:
    html_name = "volcanoes_display.html"
    filename = 'volcano.txt'
    geo_data_filename = "world.json"
    _marker_html = """
    <h4>Volcano Name: %s </h4>
    <h5>Height: %d m</h5>
    """

    def read_coordinate_data(self):
        df = pandas.read_csv(self.filename)
        x = df.loc[:, ['LAT', 'LON', 'ELEV', 'NAME']]
        return list(x.values)

    def add_geo_json_data(self):
        _data = folium.GeoJson(data=open(self.geo_data_filename, 'r', encoding='utf-8-sig').read(),
                               style_function=lambda x: {'fillColor': 'green'
                               if x['properties']['POP2005'] < 100000000 else 'orange'
                               if 100000000 <x['properties']['POP2005'] < 200000000 else 'red'})
        return _data

    @staticmethod
    def color_generator(elev):
        if elev <= 1000:
            resp = "green"
        elif 1000 < elev <= 3000:
            resp = "orange"
        else:
            resp = "red"
        return resp

    def draw_on_map(self):
        _map = folium.Map(location=[38.58, -99.09], zoom_start=6, titles="Mapbox Bright")
        fg = folium.FeatureGroup(name="Volcano Markers")
        for item in self.read_coordinate_data():
            ifr = folium.IFrame(html=self._marker_html % (item[3], item[2]), width=200, height=200)
            # fg.add_child(folium.Marker(location=[item[0], item[1]], popup=folium.Popup(ifr),
            #                            icon=folium.Icon(color=self.color_generator(item[2]))))
            cm = folium.CircleMarker(location=(item[0], item[1]), popup=folium.Popup(ifr),
                                     radius=6, tooltip=folium.Tooltip("%s" % item[3]),
                                     fill_color=self.color_generator(item[2]), color='grey',
                                     fill_opacity=0.7)
            fg.add_child(cm)

        fgp = folium.FeatureGroup(name="Population")
        fgp.add_child(self.add_geo_json_data())
        _map.add_child(fg)
        _map.add_child(fgp)
        _map.add_child(folium.LayerControl())
        _map.save(self.html_name)


if __name__ == '__main__':
    m = Volcanoes()
    m.draw_on_map()




