# Screening App for oTree (v5.x.x and higher)
This oTree app uses javascript to screen participants in three ways. First, it includes a reCAPTCHA (v2) that screens for bots. Second, it includes an adblock detection script. This part of the app ensures that the user accepts scripts to be run. Lastly, it includes a proxy/vpn detection script.

If any of the last two screening procedures are triggered, users are relocated to a separate page. They are instructed to either stop blocking scripts or drop their proxy/vpn connection before reclicking the invitation link.
 
## Usage
To use the oTree app, you must (1) create a v2 reCAPTCHA (see https://developers.google.com/recaptcha) and (2) sign up for a pro plan at https://members.ip-api.com/#pricing/. There are other (potentially free) ways to get access to an IP Geolocation API, but ip-api.com worked well for me and their data is accurate and up-to-date.

After creating (1) and (2), you'll receive two keys. First, you will receive the reCAPTCHA site key from Google. Please enter this site key under the "CAPTCHA" page class inside the python file of the screening app. Second, you will receive a pro ip-api key from ip-api.com. Please also enter this key at the same location. If you are unsure where to enter the key, please the location below.

```python
class Captcha(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            captcha_site_key="ENTER CAPTCHA SITE KEY HERE",
            pro_ip_api_key="ENTER PRO IP API KEY HERE"
        )
```        