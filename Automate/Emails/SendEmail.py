import smtplib

conn = smtplib.SMTP("smtp.gmail.com", 587)
conn.ehlo()
conn.starttls()
conn.login("test@gmail.com", "password")
conn.sendmail("test@gmail.com", "johndoe@gmail.com", "Subject: Hello \n\n From the python world \n\n - Alan")
conn.quit()