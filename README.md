# AWS Scripts for Data Engineers

A collection of practical Python scripts for interacting with AWS services, designed to help data engineers automate common tasks like connecting to S3, uploading files, and managing cloud resources.

## 📂 Overview

This repository serves as a reference guide containing scripts that demonstrate:

- Connecting to AWS services (S3, etc.)
- Uploading files to S3
- Basic automation for data engineering workflows
- Common AWS operations using boto3

Ideal for beginners learning AWS and scripting for data engineering tasks.

## ⚙️ Prerequisites

- Python 3.7+
- AWS account with appropriate permissions
- AWS CLI configured or credentials in `~/.aws/credentials`
- boto3 Python library

Install boto3:
```bash
pip install boto3
```

## 📄 Scripts Reference

| Script | Description |
|--------|-------------|
| `connect_s3.py` | Connects to an S3 bucket using boto3 |
| `upload_file.py` | Uploads a file from your local machine to a specified S3 bucket |
| `list_buckets.py` | Lists all S3 buckets in your account |

## 📁 Repository Structure

```
aws_scripts_for_data_enginners/
├── connect_s3.py
├── upload_file.py
├── list_buckets.py
├── README.md
└── requirements.txt
```

## 🔐 Security Best Practices

- **Never commit AWS secret keys** to the repository
- Use **IAM roles** or **environment variables** to manage credentials securely
- Consider using AWS Secrets Manager or Parameter Store for sensitive data
- Add credential files to `.gitignore`

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Submit bug reports or feature requests via Issues
- Fork the repository and submit Pull Requests
- Improve documentation or add new scripts

## 📖 Resources

- [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/)
- [AWS CLI Configuration Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Vrishab Sharma**
- GitHub: [@SharmaVrishab](https://github.com/SharmaVrishab)

---

⭐ If you find this repository helpful, please consider giving it a star!
