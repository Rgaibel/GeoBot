import random
import requests


# Create the GeoBot Class
class GeoBot:
    #a dictionary with countries as keys and links corresponding
    country_dict = {
        "Afghanistan": "https://i.imgur.com/hQkWExw.png",
        "Albania": "https://i.imgur.com/5Unsq95.png",
        "Algeria": "https://i.imgur.com/hqXdSAJ.png",
        "American Samoa": "AS",
        "Andorra": "AD",
        "Angola": "https://i.imgur.com/A8r9E85.png",
        "Anguilla": "AI",
        "Antarctica": "AQ",
        "Antigua and Barbuda": "AG",
        "Argentina": "https://i.imgur.com/YokKpEr.png",
        "Armenia": "https://i.imgur.com/8dtCxt0.png",
        "Aruba": "AW",
        "Australia": "https://i.imgur.com/1hxxu0x.png",
        "Austria": "https://i.imgur.com/rpyzqMi.png",
        "Azerbaijan": "https://i.imgur.com/cSeQS3D.png",
        "Bahamas": "https://i.imgur.com/vYp6Kph.png",
        "Bahrain": "BH",
        "Bangladesh": "https://i.imgur.com/Nbs5GIM.png",
        "Barbados": "BB",
        "Belarus": "https://i.imgur.com/uNF92Hf.png",
        "Belgium": "https://i.imgur.com/svSLdJG.png",
        "Belize": "https://i.imgur.com/4At8GcE.png",
        "Benin": "https://i.imgur.com/sCGH0rd.png",
        "Bermuda": "BM",
        "Bhutan": "https://i.imgur.com/kLzuf0y.png",
        "Bolivia": "https://i.imgur.com/UT9XNkt.png",
        "Bosnia and Herzegovina": "https://i.imgur.com/BQRAM7v.png",
        "Botswana": "https://i.imgur.com/9HnXASR.png",
        "Bouvet Island": "BV",
        "Brazil": "https://i.imgur.com/e6AviEk.png",
        "British Indian Ocean Territory": "IO",
        "Brunei Darussalam": "https://i.imgur.com/5AONMwu.png",
        "Bulgaria": "https://i.imgur.com/ONZfFXb.png",
        "Burkina Faso": "https://i.imgur.com/YseGfDE.png",
        "Burundi": "https://i.imgur.com/VAPZPX6.png",
        "Cambodia": "https://i.imgur.com/msQnH6Z.png",
        "Cameroon": "https://i.imgur.com/YsIxzgw.png",
        "Canada": "https://i.imgur.com/ycfufCf.png",
        "Cape Verde": "https://i.imgur.com/VTTaN5H.png",
        "Cayman Islands": "KY",
        "Central African Republic": "https://i.imgur.com/sLwKZi3.png",
        "Chad": "https://i.imgur.com/s6quDoa.png",
        "Chile": "https://i.imgur.com/81VY4e4.png",
        "China": "https://i.imgur.com/FVZ1aJg.png",
        "Christmas Island": "CX",
        "Cocos (Keeling) Islands": "CC",
        "Colombia": "https://i.imgur.com/1eh2vpV.png",
        "Comoros": "KM",
        "Congo": "https://i.imgur.com/7o3RMUR.png",
        "Congo, The Democratic Republic of the": "CD",
        "Cook Islands": "CK",
        "Costa Rica": "https://i.imgur.com/pDJlqB0.png",
        "Cote Divoire": "https://i.imgur.com/EaIyNqX.png",
        "Croatia": "https://i.imgur.com/ZxVxV9W.png",
        "Cuba": "https://i.imgur.com/AMkkQS8.png",
        "Cyprus": "https://i.imgur.com/R7JxjQw.png",
        "Czech Republic": "https://i.imgur.com/YY9258b.png",
        "Denmark": "https://i.imgur.com/SFEdpz6.png",
        "Djibouti": "https://i.imgur.com/3vfIHiw.png",
        "Dominica": "DM",
        "Dominican Republic": "https://i.imgur.com/bYkQNwM.png",
        "Ecuador": "https://i.imgur.com/EIdRVWy.png",
        "Egypt": "https://i.imgur.com/6sN3qoR.png",
        "El Salvador": "https://i.imgur.com/3DWGX5c.png",
        "Equatorial Guinea": "https://i.imgur.com/Elagjkj.png",
        "Eritrea": "https://i.imgur.com/NMsRsaf.png",
        "Estonia": "https://i.imgur.com/1ZDvCdJ.png",
        "Ethiopia": "https://i.imgur.com/lTjyqZc.png",
        "Falkland Islands": "https://i.imgur.com/35u3dwn.png",
        "Faroe Islands": "FO",
        "Fiji": "https://i.imgur.com/gxiEJ4m.png",
        "Finland": "https://i.imgur.com/57AjgFg.png",
        "France": "https://i.imgur.com/cO2YZxh.png",
        "French Guiana": "https://i.imgur.com/xlqHvl8.png",
        "French Polynesia": "PF",
        "French Southern Territories": "TF",
        "Gabon": "https://i.imgur.com/zYzgOSL.png",
        "Gambia": "https://i.imgur.com/5X19rdH.png",
        "Georgia": "https://i.imgur.com/vJ81NfL.png",
        "Germany": "https://i.imgur.com/hpgQeNw.png",
        "Ghana": "https://i.imgur.com/F0tEpTe.png",
        "Gibraltar": "GI",
        "Greece": "https://i.imgur.com/mbAZ6Zd.png",
        "Greenland": "https://i.imgur.com/Sj5S060.png",
        "Grenada": "GD",
        "Guadeloupe": "GP",
        "Guam": "GU",
        "Guatemala": "https://i.imgur.com/ybXJE4L.png",
        "Guernsey": "GG",
        "Guinea": "https://i.imgur.com/itltwy2.png",
        "Guinea-Bissau": "https://i.imgur.com/BMm4DJR.png",
        "Guyana": "https://i.imgur.com/Q4mLn6X.png",
        "Haiti": "https://i.imgur.com/5MzD153.png",
        "Heard Island and Mcdonald Islands": "HM",
        "Holy See (Vatican City State)": "VA",
        "Honduras": "https://i.imgur.com/L8vecrn.png",
        "Hong Kong": "HK",
        "Hungary": "https://i.imgur.com/eV7hvaX.png",
        "Iceland": "https://i.imgur.com/cJqxJKf.png",
        "India": "https://i.imgur.com/cGSqi71.png",
        "Indonesia": "https://i.imgur.com/uMD54Ac.png",
        "Iran": "https://i.imgur.com/HDmrsEw.png",
        "Iraq": "https://i.imgur.com/4uKW9Yt.png",
        "Ireland": "https://i.imgur.com/jIjIZfh.png",
        "Isle of Man": "IM",
        "Israel": "https://i.imgur.com/NT3DzvR.png",
        "Italy": "https://i.imgur.com/0IAczOK.png",
        "Jamaica": "https://i.imgur.com/YbgCPiZ.png",
        "Japan": "https://i.imgur.com/yI1ab1P.png",
        "Jersey": "JE",
        "Jordan": "https://i.imgur.com/qnIyUsd.png",
        "Kazakhstan": "https://i.imgur.com/DQ4ttXo.png",
        "Kenya": "https://i.imgur.com/eGrkLa3.png",
        "Kiribati": "KI",
        "North Korea": "https://i.imgur.com/e15j7GQ.png",
        "South Korea": "https://i.imgur.com/J5JqckP.png",
        "Kuwait": "https://i.imgur.com/jyF0RTp.png",
        "Kyrgyzstan": "https://i.imgur.com/5WjaKEC.png",
        "Laos": "https://i.imgur.com/NYX4ltq.png",
        "Latvia": "https://i.imgur.com/ZBY8h7Q.png",
        "Lebanon": "https://i.imgur.com/PO2ySKx.png",
        "Lesotho": "https://i.imgur.com/bNYM7CT.png",
        "Liberia": "https://i.imgur.com/NFEvWt9.png",
        "Libya": "https://i.imgur.com/KPcnUpo.png",
        "Liechtenstein": "LI",
        "Lithuania": "https://i.imgur.com/iE58w0l.png",
        "Luxembourg": "https://i.imgur.com/TAX7ojv.png",
        "Macao": "MO",
        "Macedonia": "https://i.imgur.com/Zzb7lfz.png",
        "Madagascar": "https://i.imgur.com/YaC14GF.png",
        "Malawi": "https://i.imgur.com/xAC6E8U.png",
        "Malaysia": "https://i.imgur.com/GUPzerv.png",
        "Maldives": "MV",
        "Mali": "https://i.imgur.com/tGjHwx5.png",
        "Malta": "MT",
        "Marshall Islands": "MH",
        "Martinique": "MQ",
        "Mauritania": "https://i.imgur.com/N2RRSaM.png",
        "Mauritius": "MU",
        "Mayotte": "YT",
        "Mexico": "https://i.imgur.com/FBRzQQg.png",
        "Micronesia": "FM",
        "Moldova": "https://i.imgur.com/DBsHXyP.png",
        "Monaco": "MC",
        "Mongolia": "https://i.imgur.com/G8piWNH.png",
        "Montserrat": "MS",
        "Morocco": "https://i.imgur.com/8C0UI2U.png",
        "Mozambique": "https://i.imgur.com/MntxLF0.png",
        "Myanmar": "https://i.imgur.com/f8yj28m.png",
        "Namibia": "https://i.imgur.com/XZqioOA.png",
        "Nauru": "NR",
        "Nepal": "https://i.imgur.com/OqwOWYi.png",
        "Netherlands": "https://i.imgur.com/n5Pj6lR.png",
        "New Caledonia": "https://i.imgur.com/xN0m0fU.png",
        "New Zealand": "https://i.imgur.com/WEfKPJj.png",
        "Nicaragua": "https://i.imgur.com/TSO58EH.png",
        "Niger": "https://i.imgur.com/ZZycetN.png",
        "Nigeria": "https://i.imgur.com/65ONT0I.png",
        "Niue": "NU",
        "Norfolk Island": "NF",
        "Northern Mariana Islands": "MP",
        "Norway": "https://i.imgur.com/nQXqFGc.png",
        "Oman": "https://i.imgur.com/ZbcBoFY.png",
        "Pakistan": "https://i.imgur.com/a2uQNMg.png",
        "Palau": "PW",
        "Palestine": "https://i.imgur.com/RfNs41v.png",
        "Panama": "https://i.imgur.com/WBqfOad.png",
        "Papua New Guinea": "https://i.imgur.com/RNqtIWL.png",
        "Paraguay": "https://i.imgur.com/Zgj4t3b.png",
        "Peru": "https://i.imgur.com/oCXd1E5.png",
        "Philippines": "https://i.imgur.com/BxqZtvi.png",
        "Pitcairn": "PN",
        "Poland": "https://i.imgur.com/v6HBsq6.png",
        "Portugal": "https://i.imgur.com/2MJqXPD.png",
        "Puerto Rico": "https://i.imgur.com/LMY2nwm.png",
        "Qatar": "https://i.imgur.com/ciqAI0H.png",
        "Reunion": "RE",
        "Romania": "https://i.imgur.com/W8nRf3f.png",
        "Russian": "https://i.imgur.com/uhEPjVh.png",
        "RWANDA": "https://i.imgur.com/ayJzHMX.png",
        "Saint Helena": "SH",
        "Saint Kitts and Nevis": "KN",
        "Saint Lucia": "LC",
        "Saint Pierre and Miquelon": "PM",
        "Saint Vincent and the Grenadines": "VC",
        "Samoa": "WS",
        "San Marino": "SM",
        "Sao Tome and Principe": "ST",
        "Saudi Arabia": "https://i.imgur.com/LTsH5jl.png",
        "Senegal": "https://i.imgur.com/xs2RtnU.png",
        "Serbia": "https://i.imgur.com/JqUmbNe.png",
        "Montenegro": "https://i.imgur.com/weYD01D.png",
        "Seychelles": "SC",
        "Sierra Leone": "https://i.imgur.com/6xMCpVV.png",
        "Singapore": "SG",
        "Slovakia": "https://i.imgur.com/ZT3qBHw.png",
        "Slovenia": "https://i.imgur.com/tRHrQnr.png",
        "Solomon Islands": "https://i.imgur.com/AwMsJz6.png",
        "Somalia": "https://i.imgur.com/mn2OARG.png",
        "South Africa": "https://i.imgur.com/ea1vX2d.png",
        "South Georgia and the South Sandwich Islands": "GS",
        "Spain": "https://i.imgur.com/omnYaVF.png",
        "Sri Lanka": "https://i.imgur.com/BuA2yom.png",
        "Sudan": "https://i.imgur.com/RnnZgKK.png",
        "Suriname": "https://i.imgur.com/6aN33Gi.png",
        "Svalbard": "https://i.imgur.com/agGPZAa.png",
        "Swaziland": "https://i.imgur.com/IHyFgBK.png",
        "Sweden": "https://i.imgur.com/5yBN6sh.png",
        "Switzerland": "https://i.imgur.com/2ifgE4x.png",
        "Syria": "https://i.imgur.com/b8u1Wdu.png",
        "Taiwan": "https://i.imgur.com/KEqYSR5.png",
        "Tajikistan": "https://i.imgur.com/C3xCmZz.png",
        "Tanzania": "https://i.imgur.com/pIfJt00.png",
        "Thailand": "https://i.imgur.com/1A1GEva.png",
        "Timor-Leste": "https://i.imgur.com/1o0xR8J.png",
        "Togo": "https://i.imgur.com/gHKH9nQ.png",
        "Tokelau": "TK",
        "Tonga": "TO",
        "Trinidad and Tobago": "TT",
        "Tunisia": "https://i.imgur.com/I9VZCGq.png",
        "Turkey": "https://i.imgur.com/jiCHFAd.png",
        "Turkmenistan": "https://i.imgur.com/g8HEA2p.png",
        "Turks and Caicos Islands": "TC",
        "Tuvalu": "TV",
        "Uganda": "https://i.imgur.com/Nvt46if.png",
        "Ukraine": "https://i.imgur.com/wLanT5X.png",
        "United Arab Emirates": "https://i.imgur.com/Em19YYL.png",
        "United Kingdom": "https://i.imgur.com/gKzvkUp.png",
        "United States": "https://i.imgur.com/Rlnq0yk.png",
        "United States Minor Outlying Islands": "UM",
        "Uruguay": "https://i.imgur.com/SLhoaf4.png",
        "Uzbekistan": "https://i.imgur.com/mfVP8a6.png",
        "Vanuatu": "https://i.imgur.com/iZpPGrv.png",
        "Venezuela": "https://i.imgur.com/yX9wYFG.png",
        "Viet Nam": "https://i.imgur.com/wBYWSfi.png",
        "Virgin Islands, British": "VG",
        "Virgin Islands, U.S.": "VI",
        "Wallis and Futuna": "WF",
        "Western Sahara": "https://i.imgur.com/uTxhe5x.png",
        "Yemen": "https://i.imgur.com/Xl98scB.png",
        "Zambia": "https://i.imgur.com/eb1ZJin.png",
        "Zimbabwe": "https://i.imgur.com/Q3pwVSS.png"
                    }
#black dress shoes, jeans, black shirt with a colar and short sleezez, black sun glasses, looks like uzan from the army tan. with a note pad, sitting and staring at me writing down comments.probably my own imagination, black head phones, and a place wrist watch (apple) mottor cycle helmet and bag


    # The constructor for the class. It takes the channel name as the a
    # parameter and then sets it as an instance variable
    def __init__(self, channel):
        self.channel = channel
        self.country = None

    def _winner(self):

        text = f"Correct. You are the king of the world!!"

        return {"type": "section", "text": {"type": "mrkdwn", "text": text}},

    def _loser(self, country: str):

        text = f"Oh... nice try... The right answer was {country}!"

        return {"type": "section", "text": {"type": "mrkdwn", "text": text}},

    # Craft and return the entire message payload as a dictionary.
    def get_message_winner(self):
        return {
            "channel": self.channel,
            "blocks": [
                *self._winner(),
            ],
        }

    def get_message_loss(self, country_name: str):
        return {
            "channel": self.channel,
            "blocks": [
                *self._loser(country_name),
            ],
        }

    def get_random_country(self) -> str:
        country_code = random.choice(list(requests.get("http://www.geognos.com/api/en/countries/info/all.json").json()["Results"].keys()))
        self.country = requests.get(f"http://www.geognos.com/api/en/countries/info/{country_code}.json").json()["Results"]["Name"]
        return country_code

    def get_message_flag(self, country: str):
        return {
            "channel": self.channel,
            "blocks": [
                {
                    "type": "image",
                    "title": {
                        "type": "plain_text",
                        "text": f"Can you guess the name of the country this flag belongs to"
                            #{self.country}
                    },
                    "block_id": "image4",
                    "image_url": f"http://www.geognos.com/api/en/countries/flag/{country}.png",
                    "alt_text": "country_flag"
                }
            ],
        }
    def get_message_picture(self):
        link = self.country_dict.get(f"{self.country}")
        return {
            "channel": self.channel,
            "blocks": [
                {
                    "type": "image",
                    "title": {
                        "type": "plain_text",
                        "text": f"Can you guess the name of this country?{self.country}"
                    },
                    "block_id": "image4",
                    "image_url": f"{link}",
                    "alt_text": "country_flag"
                }
            ],
        }
