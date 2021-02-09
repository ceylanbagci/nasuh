from threading import Thread
from django.conf import settings
import core.custom_messages as custom_messages
from django.core.mail import send_mail,EmailMultiAlternatives
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def get_info_mail_template():
    return """<div style="background:#f5f5f5;">
    <div style="background-color:#f5f5f5;padding-top:80px;">

        <div style="margin:0 auto;max-width:600px;background:#FFFFFF;">
            <table role="presentation" style="font-size:0px;width:100%;background:#FFFFFF;border-top:3px solid #ed2a26;"
                   border="0" cellspacing="0" cellpadding="0" align="center">
                <tbody>
                <tr>
                    <td style="text-align:center;vertical-align:top;font-size:0px;padding:40px 30px 30px 30px;">

                        <div aria-labelledby="mj-column-per-100"
                             style="vertical-align:top;display:inline-block;font-size:13px;text-align:left;width:100%;">
                            <table role="presentation" border="0" cellspacing="0" cellpadding="0" width="100%">
                                <tbody>
                                <tr>
                                    <td style="font-size:0px;padding:0px;padding-bottom:30px;" align="center">
                                        <table role="presentation" style="border-collapse:collapse;border-spacing:0px;"
                                               border="0" cellspacing="0" cellpadding="0" align="center">
                                            <tbody>
                                            <tr>
                                                <td style="width:180px;">
                                                    <img alt="" title=""
                                                         style="border:none;display:block;text-decoration:none;width:100%;height:auto;"
                                                         src="{2}"
                                                         height="auto"
                                                         width="180">
                                                 </td>
                                                <td>
                                                </td>
                                            </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="font-size:0px;padding:0px;padding-bottom:30px;" align="center">
                                        <div style="cursor:auto;color:#55575d;font-family:Open Sans,Helvetica,Arial,sans-serif;font-size:22px;font-weight:700;line-height:22px;">
                                            {1} Info
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="font-size:0px;padding:0px;padding-bottom:35px;" align="center">
                                        <div style="cursor:auto;color:#8c8c8c;font-family:Roboto,Helvetica,Arial,sans-serif;font-size:14px;line-height:22px;">
                                            {0}
                                        </div>
                                    </td>
                                </tr>
                                </tbody>
                            </table>
                        </div>

                    </td>
                </tr>
                </tbody>
            </table>
        </div>


        <div style="margin:0 auto;max-width:600px;">
            <table role="presentation" style="font-size:0px;width:100%;" border="0" cellspacing="0" cellpadding="0"
                   align="center">
                <tbody>
                <tr>
                    <td style="text-align:center;vertical-align:top;font-size:0px;padding:30px;">

                        <div aria-labelledby="mj-column-per-100"
                             style="vertical-align:top;display:inline-block;font-size:13px;text-align:left;width:100%;">
                            <table role="presentation" border="0" cellspacing="0" cellpadding="0" width="100%">
                                <tbody>
                                <tr>
                                    <td style="font-size:0px;padding:0px;padding-bottom:10px;" align="center">
                                        <div style="cursor:auto;color:#8c8c8c;font-family:Roboto,Helvetica,Arial,sans-serif;font-size:12px;line-height:22px;">
                                            <span>Bu eposta size {1} tarafından gönderilmiştir.</span>
                                            <span>Eğer bir yanlışlık olduğunu düşünüyorsanız lütfen bize bildiriniz.</span>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="font-size:0px;padding:0px;padding-bottom:15px;" align="center">
                                        <div style="cursor:auto;color:#8c8c8c;font-family:Roboto,Helvetica,Arial,sans-serif;font-size:12px;line-height:22px;">
                                            © 2020 {1} - {3}
                                        </div>
                                    </td>
                                </tr>

                                </tbody>
                            </table>
                        </div>

                    </td>
                </tr>
                </tbody>
            </table>
        </div>

    </div>

</div>"""

def run_with_thread(fn):
    def check(*args, **kwargs):
        t = Thread(target=fn, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()

    return check

@run_with_thread
def send_email(message, subject, to_mail_list):
    """
    sistemde eposta atmayı sağlayan fonksiyon NOT burada mailjet servisini kullanıyoruz ücretsiz olarak
    :param message: eposta mesajı
    :param subject: epostanın konusu
    :param to_mail: eposta atılacak eposta
    :return: boolean değer başarılıysa True değilse False
    """
    print('^'*30)

    # from_email = 'from@xxx.com'
    #
    # html_content = render_to_string(get_info_mail_template(), {'varname': 'value'})  # render with dynamic value
    # print(html_content)
    # text_content = strip_tags(html_content)  # Strip the html tag. So people can see the pure text at least.
    # print(text_content)
    # # create the email, and attach the HTML version as well.
    # print('-'*30)
    # msg = EmailMultiAlternatives(subject, text_content, from_email, to_mail_list)
    # msg.send()
    # print('+'*30)

    from_email = 'Sistem'
    logo = '/static/assets/images/widgets/2.jpg'
    contact_mail = 'hotbird305@hotmail.com'
    text_content = 'This is an important message.'
    html_content = get_info_mail_template().format(message, from_email, logo, contact_mail)
    msg = EmailMultiAlternatives(subject, text_content, from_email, to_mail_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


    return True

