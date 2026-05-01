# 🚀 AWS Cost Optimization Automation

## 📌 Overview

AWS Cost Optimization Automation is a serverless project designed to **reduce unnecessary cloud spending** by identifying and managing idle or unused AWS resources automatically.

The system leverages event-driven architecture to monitor resources, perform cleanup actions, and notify users—helping implement basic **FinOps practices** in a simple and scalable way.

---

## 🎯 Key Features

* 🔍 Detects and stops idle EC2 instances
* 🧹 Deletes unused EBS volumes
* 📊 (Optional) Generates cost usage reports
* 📩 Sends notifications via SNS (Email alerts)
* ⏱ Runs automatically on a defined schedule

---

## 🏗️ Architecture

```
Amazon EventBridge (Scheduler)
        ↓
AWS Lambda (Automation Logic)
        ↓
EC2 / EBS APIs (Resource Management)
        ↓
Amazon SNS (Notifications)
        ↓
Amazon S3 (Optional Report Storage)
```

---

## 🛠️ Tech Stack

* **Compute**: AWS Lambda
* **Scheduling**: Amazon EventBridge
* **Notifications**: Amazon SNS
* **Storage**: Amazon S3
* **Monitoring**: Amazon CloudWatch
* **Language**: Python (Boto3 SDK)

---

## 📂 Project Structure

```
aws-cost-optimizer/
│
├── lambda/
│   ├── idle_ec2.py
│   ├── unused_ebs.py
│   ├── snapshot_cleanup.py
│   └── cost_report.py
│
├── README.md
└── .gitignore
```

---

## ⚙️ How It Works

1. Amazon EventBridge triggers Lambda functions on a schedule (e.g., daily)
2. Lambda functions interact with AWS services using Boto3
3. Idle or unused resources are identified and managed
4. Notifications are sent via SNS
5. (Optional) Reports are stored in S3

---

## 🚀 Setup & Deployment

### 1. Prerequisites

* AWS account (Free Tier recommended)
* Basic knowledge of AWS services and Python

---

### 2. Create IAM Role

* Attach permissions:

  * AmazonEC2FullAccess
  * CloudWatchReadOnlyAccess
  * AmazonS3FullAccess
  * AmazonSNSFullAccess

---

### 3. Setup Services

* Create SNS topic and subscribe email
* Create S3 bucket (for reports)

---

### 4. Deploy Lambda Functions

* Create functions in AWS Lambda
* Upload code from `/lambda` folder
* Attach IAM role

---

### 5. Configure Automation

* Create rules in Amazon EventBridge
* Set schedule (e.g., rate: 1 day)
* Add Lambda functions as targets

---

## 🧪 Testing

* Use Lambda test events for manual execution
* Monitor logs in CloudWatch
* Verify email alerts via SNS

---

## 🔐 Best Practices Implemented

* ✔ Serverless architecture (cost-efficient)
* ✔ Event-driven automation
* ✔ Modular code structure
* ✔ Notification before/after actions
* ✔ Scalable and extensible design

---

## 🚧 Future Enhancements

* 💡 Auto right-sizing recommendations
* 💡 Tag-based filtering (e.g., dev/test resources)
* 💡 Web dashboard (React / Streamlit)
* 💡 Multi-account support (AWS Organizations)
* 💡 Cost anomaly detection
