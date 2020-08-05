from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import carriers

def amtg():
    
 msg = MIMEMultipart()
 password = "mdxfefuiwystcyfu"
        
    
 message = carriers.rsting + carriers.amtg1
 msg['From'] = "y.korol93@gmail.com"
 msg['To'] = "jarko.korol@gmail.com"
 msg['Subject'] = "Jerich Deliveries AMTG"
    
    
 msg.attach(MIMEText(message, 'plain'))
        
    
 server = smtplib.SMTP('smtp.gmail.com: 587')
        
 server.starttls()
        
        
 server.login(msg['From'], password)
        
        
 server.sendmail(msg['From'], msg['To'], msg.as_string())
    
 server.quit()
 print("successfully sent email to %s:" % (msg['To']))

def bgxp():
    
 msg = MIMEMultipart()
 password = "mdxfefuiwystcyfu"
        
    
 message = carriers.rsting + carriers.bgxp1
 msg['From'] = "y.korol93@gmail.com"
 msg['To'] = "jarko.korol@gmail.com"
 msg['Subject'] = "Jerich Deliveries BGXP"
    
    
 msg.attach(MIMEText(message, 'plain'))
        
    
 server = smtplib.SMTP('smtp.gmail.com: 587')
        
 server.starttls()
        
        
 server.login(msg['From'], password)
        
        
 server.sendmail(msg['From'], msg['To'], msg.as_string())
    
 server.quit()
 print("successfully sent email to %s:" % (msg['To']))
  

def ceeg():

 msg = MIMEMultipart()
 password = "mdxfefuiwystcyfu"
        
    
 message = carriers.rsting + carriers.ceeg1
 msg['From'] = "y.korol93@gmail.com"
 msg['To'] = "jarko.korol@gmail.com"
 msg['Subject'] = "Jerich Deliveries CEEG"
    
    
 msg.attach(MIMEText(message, 'plain'))
        
    
 server = smtplib.SMTP('smtp.gmail.com: 587')
        
 server.starttls()
        
        
 server.login(msg['From'], password)
        
        
 server.sendmail(msg['From'], msg['To'], msg.as_string())
    
 server.quit()
 print("successfully sent email to %s:" % (msg['To']))

def echs():

 msg = MIMEMultipart()
 password = "mdxfefuiwystcyfu"
        
    
 message = carriers.rsting + carriers.echs1
 msg['From'] = "y.korol93@gmail.com"
 msg['To'] = "jarko.korol@gmail.com"
 msg['Subject'] = "Jerich Deliveries ECHS"
    
    
 msg.attach(MIMEText(message, 'plain'))
        
    
 server = smtplib.SMTP('smtp.gmail.com: 587')
        
 server.starttls()
        
        
 server.login(msg['From'], password)
        
        
 server.sendmail(msg['From'], msg['To'], msg.as_string())
    
 server.quit()
 print("successfully sent email to %s:" % (msg['To']))

def krlg():

 msg = MIMEMultipart()
 password = "mdxfefuiwystcyfu"
        
    
 message = carriers.rsting + carriers.krlg1
 msg['From'] = "y.korol93@gmail.com"
 msg['To'] = "jarko.korol@gmail.com"
 msg['Subject'] = "Jerich Deliveries KRLG"
    
    
 msg.attach(MIMEText(message, 'plain'))
        
    
 server = smtplib.SMTP('smtp.gmail.com: 587')
        
 server.starttls()
        
        
 server.login(msg['From'], password)
        
        
 server.sendmail(msg['From'], msg['To'], msg.as_string())
    
 server.quit()
 print("successfully sent email to %s:" % (msg['To']))

def luac():

 msg = MIMEMultipart()
 password = "mdxfefuiwystcyfu"
        
    
 message = carriers.rsting + carriers.luac1
 msg['From'] = "y.korol93@gmail.com"
 msg['To'] = "jarko.korol@gmail.com"
 msg['Subject'] = "Jerich Deliveries LUAC"
    
    
 msg.attach(MIMEText(message, 'plain'))
        
    
 server = smtplib.SMTP('smtp.gmail.com: 587')
        
 server.starttls()
        
        
 server.login(msg['From'], password)
        
        
 server.sendmail(msg['From'], msg['To'], msg.as_string())
    
 server.quit()
 print("successfully sent email to %s:" % (msg['To']))

def mode():

 msg = MIMEMultipart()
 password = "mdxfefuiwystcyfu"
        
    
 message = carriers.rsting + carriers.mode1
 msg['From'] = "y.korol93@gmail.com"
 msg['To'] = "jarko.korol@gmail.com"
 msg['Subject'] = "Jerich Deliveries MODE"
    
    
 msg.attach(MIMEText(message, 'plain'))
        
    
 server = smtplib.SMTP('smtp.gmail.com: 587')
        
 server.starttls()
        
        
 server.login(msg['From'], password)
        
        
 server.sendmail(msg['From'], msg['To'], msg.as_string())
    
 server.quit()
 print("successfully sent email to %s:" % (msg['To']))

def ntgo():

 msg = MIMEMultipart()
 password = "mdxfefuiwystcyfu"
        
    
 message = carriers.rsting + carriers.ntgo1
 msg['From'] = "y.korol93@gmail.com"
 msg['To'] = "jarko.korol@gmail.com"
 msg['Subject'] = "Jerich Deliveries NTGO"
    
    
 msg.attach(MIMEText(message, 'plain'))
        
    
 server = smtplib.SMTP('smtp.gmail.com: 587')
        
 server.starttls()
        
        
 server.login(msg['From'], password)
        
        
 server.sendmail(msg['From'], msg['To'], msg.as_string())
    
 server.quit()
 print("successfully sent email to %s:" % (msg['To']))

def prcn():

 msg = MIMEMultipart()
 password = "mdxfefuiwystcyfu"
        
    
 message = carriers.rsting + carriers.prcn1
 msg['From'] = "y.korol93@gmail.com"
 msg['To'] = "jarko.korol@gmail.com"
 msg['Subject'] = "Jerich Deliveries PRCN"
    
    
 msg.attach(MIMEText(message, 'plain'))
        
    
 server = smtplib.SMTP('smtp.gmail.com: 587')
        
 server.starttls()
        
        
 server.login(msg['From'], password)
        
        
 server.sendmail(msg['From'], msg['To'], msg.as_string())
    
 server.quit()
 print("successfully sent email to %s:" % (msg['To']))

def scnn():

 msg = MIMEMultipart()
 password = "mdxfefuiwystcyfu"
        
    
 message = carriers.rsting + carriers.scnn1
 msg['From'] = "y.korol93@gmail.com"
 msg['To'] = "jarko.korol@gmail.com"
 msg['Subject'] = "Jerich Deliveries SCNN"
    
    
 msg.attach(MIMEText(message, 'plain'))
        
    
 server = smtplib.SMTP('smtp.gmail.com: 587')
        
 server.starttls()
        
        
 server.login(msg['From'], password)
        
        
 server.sendmail(msg['From'], msg['To'], msg.as_string())
    
 server.quit()
 print("successfully sent email to %s:" % (msg['To']))

def tcfp():

 msg = MIMEMultipart()
 password = "mdxfefuiwystcyfu"
        
    
 message = carriers.rsting + carriers.tcfp1
 msg['From'] = "y.korol93@gmail.com"
 msg['To'] = "jarko.korol@gmail.com"
 msg['Subject'] = "Jerich Deliveries TCFP"
    
    
 msg.attach(MIMEText(message, 'plain'))
        
    
 server = smtplib.SMTP('smtp.gmail.com: 587')
        
 server.starttls()
        
        
 server.login(msg['From'], password)
        
        
 server.sendmail(msg['From'], msg['To'], msg.as_string())
    
 server.quit()
 print("successfully sent email to %s:" % (msg['To']))

def todl():

 msg = MIMEMultipart()
 password = "mdxfefuiwystcyfu"
        
    
 message = carriers.rsting + carriers.todl1
 msg['From'] = "y.korol93@gmail.com"
 msg['To'] = "jarko.korol@gmail.com"
 msg['Subject'] = "Jerich Deliveries TODL"
    
    
 msg.attach(MIMEText(message, 'plain'))
        
    
 server = smtplib.SMTP('smtp.gmail.com: 587')
        
 server.starttls()
        
        
 server.login(msg['From'], password)
        
        
 server.sendmail(msg['From'], msg['To'], msg.as_string())
    
 server.quit()
 print("successfully sent email to %s:" % (msg['To']))

def wfli():

 msg = MIMEMultipart()
 password = "mdxfefuiwystcyfu"
        
    
 message = carriers.rsting + carriers.wfli1
 msg['From'] = "y.korol93@gmail.com"
 msg['To'] = "jarko.korol@gmail.com"
 msg['Subject'] = "Jerich Deliveries WFLI"
    
    
 msg.attach(MIMEText(message, 'plain'))
        
    
 server = smtplib.SMTP('smtp.gmail.com: 587')
        
 server.starttls()
        
        
 server.login(msg['From'], password)
        
        
 server.sendmail(msg['From'], msg['To'], msg.as_string())
    
 server.quit()
 print("successfully sent email to %s:" % (msg['To']))


def bthd():

 msg = MIMEMultipart()
 password = "mdxfefuiwystcyfu"
        
    
 message = carriers.rsting + carriers.bthd1
 msg['From'] = "y.korol93@gmail.com"
 msg['To'] = "jarko.korol@gmail.com"
 msg['Subject'] = "Jerich Deliveries BTHD"
    
    
 msg.attach(MIMEText(message, 'plain'))
        
    
 server = smtplib.SMTP('smtp.gmail.com: 587')
        
 server.starttls()
        
        
 server.login(msg['From'], password)
        
        
 server.sendmail(msg['From'], msg['To'], msg.as_string())
    
 server.quit()
 print("successfully sent email to %s:" % (msg['To']))

def btth():

 msg = MIMEMultipart()
 password = "mdxfefuiwystcyfu"
        
    
 message = carriers.rsting + carriers.btth1
 msg['From'] = "y.korol93@gmail.com"
 msg['To'] = "taras.viter27@gmail.com"
 msg['Subject'] = "Jerich Deliveries BTTH"
    
    
 msg.attach(MIMEText(message, 'plain'))
        
    
 server = smtplib.SMTP('smtp.gmail.com: 587')
        
 server.starttls()
        
        
 server.login(msg['From'], password)
        
        
 server.sendmail(msg['From'], msg['To'], msg.as_string())
    
 server.quit()
 print("successfully sent email to %s:" % (msg['To']))

def satn():

 msg = MIMEMultipart()
 password = "mdxfefuiwystcyfu"
        
    
 message = carriers.rsting + carriers.satn1
 msg['From'] = "y.korol93@gmail.com"
 msg['To'] = "taras.viter27@gmail.com"
 msg['Subject'] = "Jerich Deliveries SATN"
    
    
 msg.attach(MIMEText(message, 'plain'))
        
    
 server = smtplib.SMTP('smtp.gmail.com: 587')
        
 server.starttls()
        
        
 server.login(msg['From'], password)
        
        
 server.sendmail(msg['From'], msg['To'], msg.as_string())
    
 server.quit()
 print("successfully sent email to %s:" % (msg['To']))
