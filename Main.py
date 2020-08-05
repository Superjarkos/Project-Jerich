from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import carriers
import ema

if len(carriers.amtg) > 0:
     ema.amtg()
else:
     pass

if len(carriers.bgxp) > 0:
     ema.bgxp()
else:
     pass

if len(carriers.ceeg) > 0:
     ema.ceeg()
else:
     pass

if len(carriers.echs) > 0:
     ema.echs()
else:
     pass

if len(carriers.krlg) > 0:
     ema.krlg()
else:
     pass

if len(carriers.luac) > 0:
     ema.luac()
else:
     pass

if len(carriers.mode) > 0:
     ema.mode()
else:
     pass

if len(carriers.ntgo) > 0:
     ema.ntgo()
else:
     pass

if len(carriers.prcn) > 0:
     ema.prcn()
else:
     pass

if len(carriers.scnn) > 0:
     ema.scnn()
else:
     pass

if len(carriers.tcfp) > 0:
     ema.tcfp()
else:
     pass

if len(carriers.todl) > 0:
     ema.todl()
else:
     pass

if len(carriers.wfli) > 0:
     ema.wfli()
else:
     pass

if len(carriers.bthd) > 0:
     ema.bthd()
else:
     pass

if len(carriers.btth) > 0:
     ema.btth()
else:
     pass

if len(carriers.satn) > 0:
     ema.satn()
else:
     pass