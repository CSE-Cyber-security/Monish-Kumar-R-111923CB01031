# Cybersecurity Asset Inventory System

## Week-01 Mini Project

A Python-based cybersecurity asset inventory application for storing and managing organizational IT assets.

## Features

* Add a new IT asset
* Display all assets
* Search by Asset ID or Asset Name
* Update an existing asset
* Delete an asset
* Validate Asset Type, Risk Level and Security Status
* Validate IPv4 addresses
* Prevent duplicate Asset IDs
* Persist data in a JSON file
* Display cybersecurity risk and security summaries

## Asset Fields

|Field|Description|
|-|-|
|Asset ID|Unique identifier such as A101|
|Asset Name|Host/application name|
|Asset Type|Workstation, Server, Router, Switch, Application|
|IP Address|IPv4 address|
|Operating System|OS or platform|
|Department|Owner/department|
|Risk Level|Low, Medium, High, Critical|
|Security Status|Secure, Warning, Vulnerable|

## Repository Structure

```text
Week-01-Cybersecurity-Asset-Inventory/
│
├── src/
│   └── asset\_inventory.py
│
├── data/
│   └── assets.json
│
├── tests/
│   └── test\_cases.md
│
├── screenshots/
│   ├── 01-add-asset.png
│   ├── 02-display-assets.png
│   ├── 03-search-asset.png
│   ├── 04-update-asset.png
│   ├── 05-delete-asset.png
│   ├── 06-security-summary.png
│   └── 07-input-validation.png
│
└── README.md


## Requirements

* Python 3.9 or later
* No external Python packages are required.

## How to Run

Open a terminal in the project root:

bash
python src/asset\_inventory.py


On some systems use:

bash
python3 src/asset\_inventory.py


## Menu

text
1. Add Asset
2. Display All Assets
3. Search Asset
4. Update Asset
5. Delete Asset
6. Security Summary
7. Exit


## Sample Data

The included `data/assets.json` contains:

* A101 – HR-PC-01
* A102 – Web-Server
* A103 – Core-Router

The expected initial summary is:

text
Total Assets       : 3
Critical Assets    : 1
High Risk Assets   : 1
Medium Risk Assets : 1
Low Risk Assets    : 0
Vulnerable Assets  : 1


## Input Validation

The system validates:

1. Required fields cannot be empty.
2. Asset IDs must be unique.
3. Asset Type must be one of the five allowed values.
4. Risk Level must be Low, Medium, High or Critical.
5. Security Status must be Secure, Warning or Vulnerable.
6. IP Address must be a valid IPv4 address.

## Screenshots to Capture

Run the program and capture screenshots for these seven files:

1. 01-add-asset.png` – successful asset addition
2. 02-display-assets.png` – all assets and inventory summary
3. 03-search-asset.png` – successful search
4. 04-update-asset.png` – successful update
5. 05-delete-asset.png` – successful deletion
6. 06-security-summary.png` – security/risk summary
7. 07-input-validation.png` – invalid input being rejected

Save all screenshots inside the `screenshots/` folder with exactly these names.

## Suggested Demo Sequence

1. Start the application.
2. Display the three sample assets.
3. Add A104.
4. Search for A104.
5. Update A104's risk level.
6. Display the updated asset.
7. Delete A104.
8. Try an invalid asset type to demonstrate validation.
9. Open Security Summary.
10. Exit.



## Learning Outcomes

This project demonstrates:

* Python functions
* Lists and dictionaries
* File handling
* JSON data persistence
* CRUD operations
* Input validation
* Searching and updating records
* Basic cybersecurity risk classification
* Git/GitHub repository organization

## 

