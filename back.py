import qrcode
# import end as End
from PIL import Image,ImageTk
from MyQR import myqr as mq


def Source ( x,y,z ) :
    # taking image which user wants
    # in the QR code center
    Logo_link = z
    logo = Image.open(Logo_link)
    # taking base width
    basewidth = 100
    # adjust image size
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize))
    QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    # taking url or text
    url= x
    # adding URL or text to QRcode
    QRcode.add_data(url)
    # generating QR code
    QRcode.make()
    # taking color name from user
    QRcolor = y
    # adding color to QR code
    QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')
    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,(QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
    # save the QR code generated
    
    print('QR code generated!')
    QRimg.show()
    # mimg="done.jpg"
    # QRimg.save(mimg)
    # End.img(mimg)


def Source2 ( p,q,r ) :
    
    # a="g22.png"
    mq.run(words = p,
    version = 6,
    picture = q,
    colorized = True,
    save_name = r
    )
    # End.img(r)
    img = Image.open(r)
    img.show()
