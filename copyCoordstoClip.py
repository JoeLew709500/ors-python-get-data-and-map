layer = iface.activeLayer()
features = layer.getFeatures()

coords = []
for feature in features:
    geom = feature.geometry()
    if geom.type() == QgsWkbTypes.PointGeometry:
        point = geom.asPoint()
        coords.append(f"[{point.x()}, {point.y()}]")
        
coords_str = ", ".join(coords)
QApplication.clipboard().setText(coords_str)
print("Coordinates copied to clipboard!")
