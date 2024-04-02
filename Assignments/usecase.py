import json

# JSON data representing the training session
training_session_json = '''
{
  "name": "Python Training",
  "date": "April 19, 2024",
  "completed": true,
  "instructor": {
   "name": "XYZ",
   "website": "http://pqr.com/"
  },
  "participants": [
    {
      "name": "Participant 1",
      "email": "email1@example.com"
    },
    {
      "name": "Participant 2",
      "email": "email2@example.com"
    }
  ]
}
'''

# Load the JSON data into a Python dictionary
training_session = json.loads(training_session_json)

# Accessing boolean value
completed = training_session["completed"]

# Accessing string value
training_name = training_session["name"]

# Accessing date string
training_date = training_session["date"]

# Accessing dictionary values
instructor_name = training_session["instructor"]["name"]
instructor_website = training_session["instructor"]["website"]

# Accessing list values
participants = training_session["participants"]
participant_names = [participant["name"] for participant in participants]
participant_emails = [participant["email"] for participant in participants]

# Printing the values
print("Training Name:", training_name)
print("Date:", training_date)
print("Completed:", completed)
print("Instructor Name:", instructor_name)
print("Instructor Website:", instructor_website)
print("Participant Names:", participant_names)
print("Participant Emails:", participant_emails)
