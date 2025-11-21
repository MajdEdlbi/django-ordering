import qrcode

image = qrcode.make('009988')
image.save('qrcode.png')