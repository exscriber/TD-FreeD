from FreeD import D1 as Camera, DA as Lens

# msg = '209 255 1 142 196 255 109 182 0 0 0 0 0 0 0 0 0 0 0 0 0 6 100 0 15 255 15 255 117'
# msg = '209 255 1 124 123 255 108 78 0 0 0 0 0 0 0 0 0 0 0 0 0 6 100 0 15 255 15 255 57'
msg = '209 255 1 128 180 255 108 78 0 0 0 0 0 0 0 0 0 0 0 0 0 6 100 0 15 255 15 255 252'
buf = bytes([int(x) for x in msg.split()])
print(Camera.parse(buf))

msg1 = Camera.from_bytes(buf)
print(msg1)
print(Camera.parse(msg1.to_bytes()))

msg2 = Camera(pan=1.25, tilt=-2.48, zoom=1405, posx=13.54)
print(msg2)
print(Camera.parse(msg2.to_bytes()))
