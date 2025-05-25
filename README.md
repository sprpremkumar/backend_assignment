# **Gmail Rule-Based Email Processor**

This is a standalone Python script that connects to the Gmail API, fetches emails, stores them in a relational database,
and then applies custom rules defined in a rules.json file to perform actions like marking messages as read/unread or 
moving them to folders.


### Key Features
* Authenticate with Gmail using OAuth2 (Google's official Python client)

* Fetch emails via Gmail API (no IMAP used)

* Store emails in a local SQLite database

* Define rule-based conditions and actions in a rules.json file

* Take actions like marking emails as read/unread or moving them

### Getting Started

#### Clone the Repository
`git clone https://github.com/sprpremkumar/backend_assignment.git`

`cd gmail-rule-processor`

### Install requirements
`pip install -r requirements.txt`

### Setup

#### Create a Google API Project
   1. Go to Google console https://console.cloud.google.com/
   2. Create a new project if not exists
   3. Enable GMAIL API, by searching it in search bar
   4. Create OAuth 2.0 Client ID credentials
   5. Download the `credentials.json` file and place it in your project under `auth` folder.

### Rule Structure
Each `rules.json` must contain:
1. A top-level predicate: "all" or "any"

2. A list of conditions (field, predicate, value)

3. A list of actions

Sample `rule.json` file:

    {
    "predicate": "all",
    "rules": [
        {
            "field": "from",
            "predicate": "contains",
            "value": "noreply@example.com"
        },
        {
            "field": "subject",
            "predicate": "contains",
            "value": "Invoice"
        }
        ],
    "actions": [
        {
            "action": "mark_as_read"
        },
        {
            "action": "move_to_folder",
            "value": "Invoices"
        }
    ]
    }

### How to Run
In terminal RUN: `python main.py` 
