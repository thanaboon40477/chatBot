from linebot.models import FlexSendMessage

def flexuser(image, linename, firstname, email, company, tel, product):
    flexms = FlexSendMessage(
            alt_text='flex_message',
            contents={
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": f"{image}",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "width": "72px",
            "height": "72px",
            "cornerRadius": "100px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "contents": [
                  {
                    "type": "span",
                    "text": "สวัสดี คุณ",
                    "size": "md",
                    "color": "#000000",
                    "weight": "bold"
                  },
                  {
                    "type": "span",
                    "text": " ",
                    "weight": "bold"
                  },
                  {
                    "type": "span",
                    "text": f"{linename}",
                    "color": "#000000",
                    "weight": "bold",
                    "size": "md"
                  }
                ],
                "weight": "bold",
                "color": "#000000",
                "size": "sm",
                "wrap": True
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "ข้อมูลติดต่อ",
                    "size": "md",
                    "color": "#bcbcbc"
                  }
                ],
                "margin": "md",
                "spacing": "sm"
              }
            ],
            "spacing": "xl",
            "paddingAll": "20px"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "contents": [
                  {
                    "type": "span",
                    "text": f"ชื่อ : {firstname}"
                  }
                ]
              },
              {
                "type": "text",
                "contents": [
                  {
                    "type": "span",
                    "text": f"อีเมล : {email}"
                  }
                ]
              },
              {
                "type": "text",
                "contents": [
                  {
                    "type": "span",
                    "text": f"บริษัท :{company} "
                  }
                ]
              },
              {
                "type": "text",
                "contents": [
                  {
                    "type": "span",
                    "text": f"เบอร์ติดต่อ : {tel}"
                  }
                ]
              },
              {
                "type": "text",
                "contents": [
                  {
                    "type": "span",
                    "text": f"ผลิตภัณฑ์ : {product}"
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "xl",
        "margin": "20px"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "contents": [
                  {
                    "type": "span",
                    "text": "ข้อมูลเพิ่มเติม :"
                  }
                ]
              },
              {
                "type": "text",
                "margin": "md",
                "contents": [
                  {
                    "type": "span",
                    "text": " "
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "xl",
        "margin": "20px"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "www.mangoconsultant.com",
        "size": "xxs",
        "color": "#bcbcbc"
      }
    ],
    "paddingStart": "20px"
  },
  "styles": {
    "footer": {
      "backgroundColor": "#D1F2EB"
    }
  }
}
            )
    return flexms

def flexms_scaping(url):
  flexScp = FlexSendMessage(
    alt_text='ตาราง Bit Coin',
    contents={
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "ราคา Bit Coin",
        "weight": "bold"
      }
    ]
  },
  "hero": {
    "type": "image",
    "url": "https://www.crushpixel.com/big-static16/preview4/businessman-running-on-graphs-happy-2430875.jpg",
    "size": "full",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    },
    "aspectRatio": "16:10"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "ตารางราคา Bit Coin",
          "uri": f"{url}"
        },
        "color": "#FEFE5D",
        "style": "secondary"
      }
    ]
  }
}
)
  return flexScp

