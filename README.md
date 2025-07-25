# mini-project-serverless-api
Mini Project 1 (learning)
# Trigger Actions
# Mini Project 1: Production-Ready Serverless API with Full Observability

## ✅ Project Summary
This project is a fully production-ready **serverless API** built with AWS Lambda, API Gateway, DynamoDB, CloudWatch, and Secrets Manager. The entire infrastructure is defined using Terraform and deployed automatically using GitHub Actions CI/CD pipeline.

---

## 🌐 Live Demo
**API Endpoint:** [`https://33m9lcigzh.execute-api.ap-southeast-1.amazonaws.com`](https://33m9lcigzh.execute-api.ap-southeast-1.amazonaws.com)

---

## 🚀 Key Features

### 🏗️ Infrastructure as Code (Terraform)
- Modular Terraform for all AWS components
- Remote state management using **S3** and state locking via **DynamoDB**

### 🖥️ Serverless Backend
- **Lambda** function (`mini-api`) as the backend
- Triggered via **API Gateway**
- Supports HTTP requests with structured logging

### 🔐 Security Best Practices
- IAM roles with least privilege principle
- Secrets securely stored in **AWS Secrets Manager**
- No hardcoded sensitive data

### 🔄 CI/CD with GitHub Actions
- Full CI/CD pipeline:
  - `terraform init → fmt → validate → plan → apply`
  - Linting with **flake8**
  - Unit tests with **pytest**
  - Coverage enforcement with **pytest-cov**
- GitHub Secrets used for secure authentication

### 🧪 Testing & Code Quality
- Unit tests with **pytest** using `boto3` mocks
- Test coverage > 80%
- Enforced linting and code style with **flake8**

### 📊 Observability & Monitoring (CloudWatch)
- CloudWatch **Log Metric Filter** for `"ERROR"` patterns
- CloudWatch **Alarms** for:
  - High Invocation Count
  - High Duration
  - Lambda errors
- Custom **CloudWatch Dashboard**:
  - Invocation metrics
  - Error metrics
  - Average duration

---

## 🐞 Notable Issues & Fixes

### ❌ Issue: Dashboard Not Showing Data
- **Cause**: Terraform's `jsonencode` makes CloudWatch dashboards "dirty" and doesn't update unless forced
- **Fix**: Used `terraform taint aws_cloudwatch_dashboard.lambda_dashboard` to force refresh

### ❌ Issue: Metric Filter Not Updating
- **Cause**: Log group name mismatch or stale metric filter state
- **Fix**: Aligned exact Lambda log group name `/aws/lambda/mini-api` and redeployed

### ❌ Issue: `terraform apply` Errors
- **Cause**: Outdated or missing Terraform providers
- **Fix**: Re-ran `terraform init` to reinstall providers

### ❌ Issue: GitHub Actions Terraform State Lock
- **Cause**: Parallel apply or stale locks
- **Fix**: Cleaned up locks in DynamoDB or waited for expiration

---

## 📁 Project Structure
```
mini-project-serverless-api/
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── cloudwatch.tf
│   ├── cloudwatch-performance.tf
│   └── outputs.tf
├── src/
│   └── app.py
├── tests/
│   └── test_app.py
├── .github/
│   └── workflows/
│       └── deploy.yml
└── README.md
```

---

## ✅ Project Status
This project is **complete and production-ready**. It demonstrates hands-on expertise with:
- AWS infrastructure
- DevOps and CI/CD pipelines
- Serverless architecture
- Testing and quality assurance
- Monitoring and alerting

---

## 🧠 Next Steps
- Set up SNS Email alerts (currently alarm_actions configured but not subscribed)
- Extend API functionality with CRUD and DynamoDB integration
- Add performance tuning (cold start mitigation, concurrency control)

---

## 📣 Author
**Syamel Amri** — aspiring Cloud/DevOps Engineer

If you're reviewing this as part of an application or interview, please feel free to contact me for a walkthrough!

---

## 🏁 Final Thoughts
Building this project helped reinforce real-world AWS DevOps workflows: from IaC, secure deployments, CI/CD pipelines, error monitoring, to debugging unexpected production issues. It’s more than just a project — it’s a foundation for production-grade infrastructure.
