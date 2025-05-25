"""
Created By: Prem Kumar R on 24-05-2025 at 12 PM
"""

MESSAGE_MOCK = {
  "id": "19705b24f09c7f9e",
  "threadId": "19705b24f09c7f9e",
  "labelIds": [
    "UNREAD",
    "CATEGORY_UPDATES",
    "INBOX"
  ],
  "snippet": "Calendar App was granted access to your Google Account sprpremkumar@gmail.com If you did not grant access, you should check this activity and secure your account. Check activity You can also see",
  "payload": {
    "partId": "",
    "mimeType": "multipart/alternative",
    "filename": "",
    "headers": [
      {
        "name": "Subject",
        "value": "Security alert"
      },
      {
        "name": "From",
        "value": "Google \u003cno-reply@accounts.google.com\u003e"
      },
      {
        "name": "To",
        "value": "sprpremkumar@gmail.com"
      },
      {
        "name": "Content-Type",
        "value": "multipart/alternative; boundary=\"0000000000007d69610635ee402e\""
      }
    ],
    "body": {
      "size": 0
    },
    "parts": [
      {
        "partId": "0",
        "mimeType": "text/plain",
        "filename": "",
        "headers": [
          {
            "name": "Content-Type",
            "value": "text/plain; charset=\"UTF-8\"; format=flowed; delsp=yes"
          },
          {
            "name": "Content-Transfer-Encoding",
            "value": "base64"
          }
        ],
        "body": {
          "size": 663,
          "data": "W2ltYWdlOiBHb29nbGVdDQpDYWxlbmRhciBBcHAgd2FzIGdyYW50ZWQgYWNjZXNzIHRvIHlvdXIgR29vZ2xlIEFjY291bnQNCg0KDQpzcHJwcmVta3VtYXJAZ21haWwuY29tDQoNCklmIHlvdSBkaWQgbm90IGdyYW50IGFjY2VzcywgeW91IHNob3VsZCBjaGVjayB0aGlzIGFjdGl2aXR5IGFuZCBzZWN1cmUgeW91cg0KYWNjb3VudC4NCkNoZWNrIGFjdGl2aXR5DQo8aHR0cHM6Ly9hY2NvdW50cy5nb29nbGUuY29tL0FjY291bnRDaG9vc2VyP0VtYWlsPXNwcnByZW1rdW1hckBnbWFpbC5jb20mY29udGludWU9aHR0cHM6Ly9teWFjY291bnQuZ29vZ2xlLmNvbS9hbGVydC9udC8xNzQ4MTQ3MjYwMDAwP3JmbiUzRDEyNyUyNnJmbmMlM0QxJTI2ZWlkJTNENzYxMDY4NTM1ODI0NjIxNTU0MyUyNmV0JTNEMD4NCllvdSBjYW4gYWxzbyBzZWUgc2VjdXJpdHkgYWN0aXZpdHkgYXQNCmh0dHBzOi8vbXlhY2NvdW50Lmdvb2dsZS5jb20vbm90aWZpY2F0aW9ucw0KWW91IHJlY2VpdmVkIHRoaXMgZW1haWwgdG8gbGV0IHlvdSBrbm93IGFib3V0IGltcG9ydGFudCBjaGFuZ2VzIHRvIHlvdXINCkdvb2dsZSBBY2NvdW50IGFuZCBzZXJ2aWNlcy4NCsKpIDIwMjUgR29vZ2xlIExMQywgMTYwMCBBbXBoaXRoZWF0cmUgUGFya3dheSwgTW91bnRhaW4gVmlldywgQ0EgOTQwNDMsIFVTQQ0K"
        }
      },
      {
        "partId": "1",
        "mimeType": "text/html",
        "filename": "",
        "headers": [
          {
            "name": "Content-Type",
            "value": "text/html; charset=\"UTF-8\""
          },
          {
            "name": "Content-Transfer-Encoding",
            "value": "quoted-printable"
          }
        ],
        "body": {
          "size": 4709,
          "data": "PCFET0NUWVBFIGh0bWw-PGh0bWwgbGFuZz0iZW4iPjxoZWFkPjxtZXRhIG5hbWU9ImZvcm1hdC1kZXRlY3Rpb24iIGNvbnRlbnQ9ImVtYWlsPW5vIi8-PG1ldGEgbmFtZT0iZm9ybWF0LWRldGVjdGlvbiIgY29udGVudD0iZGF0ZT1ubyIvPjxzdHlsZSBub25jZT0iOVUwQUdMdExDUmdLcW9iRWZIMWE4USI-LmF3bCBhIHtjb2xvcjogI0ZGRkZGRjsgdGV4dC1kZWNvcmF0aW9uOiBub25lO30gLmFibWwgYSB7Y29sb3I6ICMwMDAwMDA7IGZvbnQtZmFtaWx5OiBSb2JvdG8tTWVkaXVtLEhlbHZldGljYSxBcmlhbCxzYW5zLXNlcmlmOyBmb250LXdlaWdodDogYm9sZDsgdGV4dC1kZWNvcmF0aW9uOiBub25lO30gLmFkZ2wgYSB7Y29sb3I6IHJnYmEoMCwgMCwgMCwgMC44Nyk7IHRleHQtZGVjb3JhdGlvbjogbm9uZTt9IC5hZmFsIGEge2NvbG9yOiAjYjBiMGIwOyB0ZXh0LWRlY29yYXRpb246IG5vbmU7fSBAbWVkaWEgc2NyZWVuIGFuZCAobWluLXdpZHRoOiA2MDBweCkgey52MnNwIHtwYWRkaW5nOiA2cHggMzBweCAwcHg7fSAudjJyc3Age3BhZGRpbmc6IDBweCAxMHB4O319IEBtZWRpYSBzY3JlZW4gYW5kIChtaW4td2lkdGg6IDYwMHB4KSB7Lm1kdjJydyB7cGFkZGluZzogNDBweCA0MHB4O319IDwvc3R5bGU-PGxpbmsgaHJlZj0iLy9mb250cy5nb29nbGVhcGlzLmNvbS9jc3M_ZmFtaWx5PUdvb2dsZStTYW5zIiByZWw9InN0eWxlc2hlZXQiIHR5cGU9InRleHQvY3NzIiBub25jZT0iOVUwQUdMdExDUmdLcW9iRWZIMWE4USIvPjwvaGVhZD48Ym9keSBzdHlsZT0ibWFyZ2luOiAwOyBwYWRkaW5nOiAwOyIgYmdjb2xvcj0iI0ZGRkZGRiI-PHRhYmxlIHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiIHN0eWxlPSJtaW4td2lkdGg6IDM0OHB4OyIgYm9yZGVyPSIwIiBjZWxsc3BhY2luZz0iMCIgY2VsbHBhZGRpbmc9IjAiIGxhbmc9ImVuIj48dHIgaGVpZ2h0PSIzMiIgc3R5bGU9ImhlaWdodDogMzJweDsiPjx0ZD48L3RkPjwvdHI-PHRyIGFsaWduPSJjZW50ZXIiPjx0ZD48ZGl2IGl0ZW1zY29wZSBpdGVtdHlwZT0iLy9zY2hlbWEub3JnL0VtYWlsTWVzc2FnZSI-PGRpdiBpdGVtcHJvcD0iYWN0aW9uIiBpdGVtc2NvcGUgaXRlbXR5cGU9Ii8vc2NoZW1hLm9yZy9WaWV3QWN0aW9uIj48bGluayBpdGVtcHJvcD0idXJsIiBocmVmPSJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20vQWNjb3VudENob29zZXI_RW1haWw9c3BycHJlbWt1bWFyQGdtYWlsLmNvbSZhbXA7Y29udGludWU9aHR0cHM6Ly9teWFjY291bnQuZ29vZ2xlLmNvbS9hbGVydC9udC8xNzQ4MTQ3MjYwMDAwP3JmbiUzRDEyNyUyNnJmbmMlM0QxJTI2ZWlkJTNENzYxMDY4NTM1ODI0NjIxNTU0MyUyNmV0JTNEMCIvPjxtZXRhIGl0ZW1wcm9wPSJuYW1lIiBjb250ZW50PSJSZXZpZXcgQWN0aXZpdHkiLz48L2Rpdj48L2Rpdj48dGFibGUgYm9yZGVyPSIwIiBjZWxsc3BhY2luZz0iMCIgY2VsbHBhZGRpbmc9IjAiIHN0eWxlPSJwYWRkaW5nLWJvdHRvbTogMjBweDsgbWF4LXdpZHRoOiA1MTZweDsgbWluLXdpZHRoOiAyMjBweDsiPjx0cj48dGQgd2lkdGg9IjgiIHN0eWxlPSJ3aWR0aDogOHB4OyI-PC90ZD48dGQ-PGRpdiBzdHlsZT0iYm9yZGVyLXN0eWxlOiBzb2xpZDsgYm9yZGVyLXdpZHRoOiB0aGluOyBib3JkZXItY29sb3I6I2RhZGNlMDsgYm9yZGVyLXJhZGl1czogOHB4OyBwYWRkaW5nOiA0MHB4IDIwcHg7IiBhbGlnbj0iY2VudGVyIiBjbGFzcz0ibWR2MnJ3Ij48aW1nIHNyYz0iaHR0cHM6Ly93d3cuZ3N0YXRpYy5jb20vaW1hZ2VzL2JyYW5kaW5nL2dvb2dsZWxvZ28vMngvZ29vZ2xlbG9nb19jb2xvcl83NHgyNGRwLnBuZyIgd2lkdGg9Ijc0IiBoZWlnaHQ9IjI0IiBhcmlhLWhpZGRlbj0idHJ1ZSIgc3R5bGU9Im1hcmdpbi1ib3R0b206IDE2cHg7IiBhbHQ9Ikdvb2dsZSI-PGRpdiBzdHlsZT0iZm9udC1mYW1pbHk6ICYjMzk7R29vZ2xlIFNhbnMmIzM5OyxSb2JvdG8sUm9ib3RvRHJhZnQsSGVsdmV0aWNhLEFyaWFsLHNhbnMtc2VyaWY7Ym9yZGVyLWJvdHRvbTogdGhpbiBzb2xpZCAjZGFkY2UwOyBjb2xvcjogcmdiYSgwLDAsMCwwLjg3KTsgbGluZS1oZWlnaHQ6IDMycHg7IHBhZGRpbmctYm90dG9tOiAyNHB4O3RleHQtYWxpZ246IGNlbnRlcjsgd29yZC1icmVhazogYnJlYWstd29yZDsiPjxkaXYgc3R5bGU9ImZvbnQtc2l6ZTogMjRweDsiPjxhPkNhbGVuZGFyIEFwcDwvYT4gd2FzIGdyYW50ZWQgYWNjZXNzIHRvIHlvdXIgR29vZ2xlJm5ic3A7QWNjb3VudCA8L2Rpdj48dGFibGUgYWxpZ249ImNlbnRlciIgc3R5bGU9Im1hcmdpbi10b3A6OHB4OyI-PHRyIHN0eWxlPSJsaW5lLWhlaWdodDogbm9ybWFsOyI-PHRkIGFsaWduPSJyaWdodCIgc3R5bGU9InBhZGRpbmctcmlnaHQ6OHB4OyI-PGltZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHN0eWxlPSJ3aWR0aDogMjBweDsgaGVpZ2h0OiAyMHB4OyB2ZXJ0aWNhbC1hbGlnbjogc3ViOyBib3JkZXItcmFkaXVzOiA1MCU7OyIgc3JjPSJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NLVW50dERwN0dSTVRRZnhKZ2h2SmFDVEY4UjFlcGxfZ3MxOHZhT3lKLW5vVWRfYldrZT1zOTYtYyIgYWx0PSIiPjwvdGQ-PHRkPjxhIHN0eWxlPSJmb250LWZhbWlseTogJiMzOTtHb29nbGUgU2FucyYjMzk7LFJvYm90byxSb2JvdG9EcmFmdCxIZWx2ZXRpY2EsQXJpYWwsc2Fucy1zZXJpZjtjb2xvcjogcmdiYSgwLDAsMCwwLjg3KTsgZm9udC1zaXplOiAxNHB4OyBsaW5lLWhlaWdodDogMjBweDsiPnNwcnByZW1rdW1hckBnbWFpbC5jb208L2E-PC90ZD48L3RyPjwvdGFibGU-IDwvZGl2PjxkaXYgc3R5bGU9ImZvbnQtZmFtaWx5OiBSb2JvdG8tUmVndWxhcixIZWx2ZXRpY2EsQXJpYWwsc2Fucy1zZXJpZjsgZm9udC1zaXplOiAxNHB4OyBjb2xvcjogcmdiYSgwLDAsMCwwLjg3KTsgbGluZS1oZWlnaHQ6IDIwcHg7cGFkZGluZy10b3A6IDIwcHg7IHRleHQtYWxpZ246IGxlZnQ7Ij48YnI-SWYgeW91IGRpZCBub3QgZ3JhbnQgYWNjZXNzLCB5b3Ugc2hvdWxkIGNoZWNrIHRoaXMgYWN0aXZpdHkgYW5kIHNlY3VyZSB5b3VyIGFjY291bnQuPGRpdiBzdHlsZT0icGFkZGluZy10b3A6IDMycHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxhIGhyZWY9Imh0dHBzOi8vYWNjb3VudHMuZ29vZ2xlLmNvbS9BY2NvdW50Q2hvb3Nlcj9FbWFpbD1zcHJwcmVta3VtYXJAZ21haWwuY29tJmFtcDtjb250aW51ZT1odHRwczovL215YWNjb3VudC5nb29nbGUuY29tL2FsZXJ0L250LzE3NDgxNDcyNjAwMDA_cmZuJTNEMTI3JTI2cmZuYyUzRDElMjZlaWQlM0Q3NjEwNjg1MzU4MjQ2MjE1NTQzJTI2ZXQlM0QwIiB0YXJnZXQ9Il9ibGFuayIgbGluay1pZD0ibWFpbi1idXR0b24tbGluayIgc3R5bGU9ImZvbnQtZmFtaWx5OiAmIzM5O0dvb2dsZSBTYW5zJiMzOTssUm9ib3RvLFJvYm90b0RyYWZ0LEhlbHZldGljYSxBcmlhbCxzYW5zLXNlcmlmOyBsaW5lLWhlaWdodDogMTZweDsgY29sb3I6ICNmZmZmZmY7IGZvbnQtd2VpZ2h0OiA0MDA7IHRleHQtZGVjb3JhdGlvbjogbm9uZTtmb250LXNpemU6IDE0cHg7ZGlzcGxheTppbmxpbmUtYmxvY2s7cGFkZGluZzogMTBweCAyNHB4O2JhY2tncm91bmQtY29sb3I6ICM0MTg0RjM7IGJvcmRlci1yYWRpdXM6IDVweDsgbWluLXdpZHRoOiA5MHB4OyI-Q2hlY2sgYWN0aXZpdHk8L2E-PC9kaXY-PC9kaXY-PGRpdiBzdHlsZT0icGFkZGluZy10b3A6IDIwcHg7IGZvbnQtc2l6ZTogMTJweDsgbGluZS1oZWlnaHQ6IDE2cHg7IGNvbG9yOiAjNWY2MzY4OyBsZXR0ZXItc3BhY2luZzogMC4zcHg7IHRleHQtYWxpZ246IGNlbnRlciI-WW91IGNhbiBhbHNvIHNlZSBzZWN1cml0eSBhY3Rpdml0eSBhdDxicj48YSBzdHlsZT0iY29sb3I6IHJnYmEoMCwgMCwgMCwgMC44Nyk7dGV4dC1kZWNvcmF0aW9uOiBpbmhlcml0OyI-aHR0cHM6Ly9teWFjY291bnQuZ29vZ2xlLmNvbS9ub3RpZmljYXRpb25zPC9hPjwvZGl2PjwvZGl2PjxkaXYgc3R5bGU9InRleHQtYWxpZ246IGxlZnQ7Ij48ZGl2IHN0eWxlPSJmb250LWZhbWlseTogUm9ib3RvLVJlZ3VsYXIsSGVsdmV0aWNhLEFyaWFsLHNhbnMtc2VyaWY7Y29sb3I6IHJnYmEoMCwwLDAsMC41NCk7IGZvbnQtc2l6ZTogMTFweDsgbGluZS1oZWlnaHQ6IDE4cHg7IHBhZGRpbmctdG9wOiAxMnB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48ZGl2PllvdSByZWNlaXZlZCB0aGlzIGVtYWlsIHRvIGxldCB5b3Uga25vdyBhYm91dCBpbXBvcnRhbnQgY2hhbmdlcyB0byB5b3VyIEdvb2dsZSBBY2NvdW50IGFuZCBzZXJ2aWNlcy48L2Rpdj48ZGl2IHN0eWxlPSJkaXJlY3Rpb246IGx0cjsiPiZjb3B5OyAyMDI1IEdvb2dsZSBMTEMsIDxhIGNsYXNzPSJhZmFsIiBzdHlsZT0iZm9udC1mYW1pbHk6IFJvYm90by1SZWd1bGFyLEhlbHZldGljYSxBcmlhbCxzYW5zLXNlcmlmO2NvbG9yOiByZ2JhKDAsMCwwLDAuNTQpOyBmb250LXNpemU6IDExcHg7IGxpbmUtaGVpZ2h0OiAxOHB4OyBwYWRkaW5nLXRvcDogMTJweDsgdGV4dC1hbGlnbjogY2VudGVyOyI-MTYwMCBBbXBoaXRoZWF0cmUgUGFya3dheSwgTW91bnRhaW4gVmlldywgQ0EgOTQwNDMsIFVTQTwvYT48L2Rpdj48L2Rpdj48L2Rpdj48L3RkPjx0ZCB3aWR0aD0iOCIgc3R5bGU9IndpZHRoOiA4cHg7Ij48L3RkPjwvdHI-PC90YWJsZT48L3RkPjwvdHI-PHRyIGhlaWdodD0iMzIiIHN0eWxlPSJoZWlnaHQ6IDMycHg7Ij48dGQ-PC90ZD48L3RyPjwvdGFibGU-PC9ib2R5PjwvaHRtbD4="
        }
      }
    ]
  },
  "sizeEstimate": 12130,
  "historyId": "3119547",
  "internalDate": "1748147260000"
}
