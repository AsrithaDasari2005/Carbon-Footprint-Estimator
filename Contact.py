import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.set_page_config(page_title="Contact Us", layout="wide")

st.title("Contact Us")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1501004318641-b39e6451bec6");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        color: #ffffff;
    }
    .block-container {
        background-color: rgba(0, 100, 0, 0.4);
        padding: 2rem;
        border-radius: 10px;
    }
    h1, h2, h3 {
        color: #e6ffe6;
    }
    .contact-section {
        background-color: rgba(0, 100, 0, 0.4);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .form-section {
        background-color: rgba(0, 100, 0, 0.4);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .contact-info {
        margin-bottom: 1rem;
        font-size: 1.1rem;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="contact-section">
        <h2>Get in Touch</h2>
        <p>
            We'd love to hear from you! If you have any questions, feedback, or suggestions, please feel free to reach out to us using the
            contact form below or through our contact information.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

def send_email(to_email, subject, body):
    """
    Sends an email using a temporary, insecure approach (for demonstration purposes ONLY).
    DO NOT USE THIS IN PRODUCTION.  Use a proper email sending service.

    Args:
        to_email (str): The recipient's email address.
        subject (str): The email subject.
        body (str): The email body.
    """
    # WARNING:  This is insecure.  Never hardcode credentials in real code.
    from_email = "your_email@gmail.com"  # Replace with your email
    password = "your_password"  # Replace with your password
    smtp_server = "smtp.gmail.com" # Or your mail server
    smtp_port = 587

    try:
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

name = st.text_input("Name")
email = st.text_input("Email")
subject = st.text_input("Subject")
message = st.text_area("Message")

if st.button("Send Email"):
    if not name or not email or not subject or not message:
        st.error("Please fill in all fields.")
    else:
        #  In a real application, you would use a secure method to send emails.
        #  This example is for demonstration ONLY and INSECURE.
        email_body = f"Name: {name}\nEmail: {email}\n\n{message}"
        if send_email(email, subject, email_body):
            st.success("Email sent successfully! We will get back to you soon.")
        else:
            st.error("Failed to send email. Please try again later.")

st.markdown(
    """
    <div class="contact-section">
        <h2>Contact Information</h2>
        <div class="contact-info">
            <p><strong>Email:</strong> carbonfootprint@example.com</p>
            <p><strong>Phone:</strong> +123 456 7890</p>
            <p><strong>Address:</strong> 123 Engineers Street, Anytown, Andhra Pradesh, India</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)