# Test Cases – Cybersecurity Asset Inventory System

## TC-01: Add a valid asset
**Input:** A104, Finance-PC, Workstation, 192.168.1.30, Windows 11, Finance, Low, Secure  
**Expected:** Asset added successfully and saved to `data/assets.json`.

## TC-02: Add duplicate Asset ID
**Input:** Existing ID such as A101  
**Expected:** System displays `Asset ID already exists` and does not add a duplicate.

## TC-03: Display all assets
**Action:** Select menu option 2.  
**Expected:** All stored assets and the risk/security summary are displayed.

## TC-04: Search by Asset ID
**Input:** A102  
**Expected:** Web-Server details are displayed.

## TC-05: Search by Asset Name
**Input:** Core-Router  
**Expected:** A103 details are displayed.

## TC-06: Search for non-existing asset
**Input:** A999  
**Expected:** `No matching asset found.`

## TC-07: Update an asset
**Input:** A101 and change Risk Level to High.  
**Expected:** Asset is updated and saved.

## TC-08: Delete an asset
**Input:** A103 and confirmation `y`.  
**Expected:** Asset is deleted from the inventory and JSON file.

## TC-09: Invalid Asset Type
**Input:** Firewall  
**Expected:** System rejects the value and asks for a valid asset type.

## TC-10: Invalid Risk Level
**Input:** Extreme  
**Expected:** System rejects the value and asks for Low/Medium/High/Critical.

## TC-11: Invalid Security Status
**Input:** Unsafe  
**Expected:** System rejects the value and asks for Secure/Warning/Vulnerable.

## TC-12: Invalid IP address
**Input:** 192.168.1.999  
**Expected:** System rejects the IP address.

## TC-13: Empty required field
**Input:** Blank Asset Name  
**Expected:** System displays `This field cannot be empty`.

## TC-14: Security summary
**Action:** Select menu option 6.  
**Expected:** Total, Secure, Warning, Vulnerable and risk-level counts are displayed.

## TC-15: Exit
**Action:** Select menu option 7.  
**Expected:** Program exits normally.
