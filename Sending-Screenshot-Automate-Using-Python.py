'''
Tips:- Script follows the following sequence
       ( Take-Screenshot -> Login -> Send -> Logout )
       EDIT - Email-Ids and Passwords
'''

# Mail Module
from   email.mime.multipart import MIMEMultipart
from   email.mime.image     import MIMEImage
import smtplib ,ssl


# General Modules
import pyscreenshot       # package for ss
import os, io


def sending_screenshot( method_sender,
                        method_password,
                        method_reciever,
                        msg_attach,
                        counter,
                        context 
                      ):
    '''
    Take Screenshot of current desktop
    make connection with gmail
    send it to the reciever
    '''
    
    # starting.
    mail = smtplib.SMTP_SSL( 'smtp.gmail.com', 
                             465,
                             context=context_data 
                           )

    #taking screenshot 
    stream = io.BytesIO()
    pyscreenshot.grab().save( stream, format='jpeg')

    # read and attach
    stream.seek(0)
    image_read = stream.read()
    image_ready = MIMEImage( image_read,
                             'jpg', 
                             name='Screenshot No. ' + str(counter)
                           )
    msg_attach.set_payload(image_ready)

    # Enable the debug option for what's going.
    #mail.set_debuglevel(1)
    
    ''' OUTPUT PROGRESS '''

    mail.login( method_sender , method_password )
    print(f'\nSuccessfully login {counter}')

    mail.sendmail( method_sender,
                   method_reciever, 
                   msg.as_string() )

    print('Mail No.{} Sended'.format(counter))

    mail.quit()


# Prepare Context Data

reciever = ['<type-your-email>@gmail.com']        

cc       = [ '<type-your-email>@gmail.com',              
             '<type-your-email>@gmail.com',
             '<type-your-email>@gmail.com' ]

sender         = '<type-your-email>@gmail.com'
msg            = MIMEMultipart()
msg['To']      = reciever[0]
msg['From']    = f'Python-Mail <{sender}>'
msg['Cc']      = ','.join(cc)
msg['Subject'] = 'Automate Screenshot'

context_data = ssl.create_default_context()
counter      = 1

while True:
    try:
        # calling method
        sending_screenshot( sender,
                            'type-your-password-here',
                            reciever+cc,
                            msg, 
                            counter,
                            context_data )

        input('Click Enter....')

    except KeyboardInterrupt:
        print('\nStop by user')
        break

    except Exception as e:
        print('Exception Raised - ',e, end='\n\n\n')

    counter += 1


print('\n\nCheckout Your Mails.\n')





















