import smtplib
import random
import string

# Generate a random OTP
def generate_otp(length=6):
    characters = string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Email configuration
sender_email = "adnan10tc39@gmail.com"
sender_password = "123@abc"  # Use an App Password if 2-step verification is enabled
receiver_email = "adnan10tc39@gmail.com"

# Generate OTP
otp = generate_otp()

# Email content
subject = "Your OTP Code"
message = f"Your OTP code is: {otp}"

# Sending email
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, f"Subject: {subject}\n\n{message}")
    print("OTP sent successfully.")
except Exception as e:
    print(f"Error sending OTP: {e}")
finally:
    server.quit()
