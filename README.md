# Football Matchday Fixtures Notifications and Alerts 

## **Project Overview**
This project is an alert / notifcations system that sends football fixtures from known leagues like EPL, Laliga, etc.  to subscribed users via Email. It leverages **Amazon SNS**, **AWS Lambda and Python**, **Amazon EvenBridge** and **footballAPIs** to provide football fans with up-to-date fixture information. The project demonstrates cloud computing principles and efficient notification mechanisms, leveraging the use of AWS Cloud Infrastructure System.

---

## **Features**
- Fetches football fixtures from known leagues like EPL, Laliga, etc an external API.
- Sends formatted fixture updates to subscribers via Email using Amazon SNS.
- Scheduled automation for regular updates using Amazon EventBridge at 1 hour update time.
- Designed with security in mind, following the principle of least privilege for IAM roles.

## **Prerequisites**
- Free account with subscription and API Key at [football-data.org]
- Personal AWS account with basic understanding of AWS and Python scripting.

---

## **Technologies**
- **Cloud Provider**: AWS
- **Core Services**: SNS, Lambda, EventBridge
- **External API**: NBA Game API (football-data.org)
- **Programming Language**: Python 3.x
- **IAM Security**:
  - Least privilege policies for Lambda, SNS, and EventBridge.

---

## **Project Structure**
```bash
game-day-notifications/
├── src/
│   ├── lambda_functions.py          # Main Lambda function code
├── policies/
│   ├── matchday_sns_policy.json           # SNS publishing permissions
│   ├── matchdayfootball_rule.json   # EventBridge to Lambda permissions
│   └── matchdayfootball_role.json        # Lambda execution role permissions
├── .gitignore
└── README.md                        # Project documentation
```

## **Setup Instructions**

This project walk through was guided from REX TECH, although its repo project was centered on NBA live scores update, but still clone the repo to get started and veiw the walk through steps.

### **Clone the Repository**
```bash
git clone https://github.com/ifeanyiro9/game-day-notifications.git
cd game-day-notifications
```

### **Challenges**

Challenges is a core of devops encounter, it helps gain indepth understamding of whatever project is being worked on, i encountered a few configuring the API call from football-data.org, but after taking a break and coming back to it with some chatgpt reviews and reading, the ride was made possible and delivered successfully.

A screenshot of AWS SNS alert received from the API call is attached to this repo.

Have fun coding in the Cloud!!!
